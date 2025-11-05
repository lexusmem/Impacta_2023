from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import os
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_busca_site_duckduckgo():
    # inicializa o Chrome usando webdriver-manager para evitar problemas de versão
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # descomente para CI/headless
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                 options=options)

    palavras_busca = "Page Object"

    try:
        navegador.get('http://www.duckduckgo.com')

        # 1. Espera para a caixa de busca carregar (tenta vários seletores comuns)
        WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "input#searchbox_input, input#search_form_input, input[name='q'], input[type='search']")
            )
        )

        # localizar a caixa de busca por uma lista de seletores (tornando o teste mais resiliente)
        possible_selectors = [
            (By.ID, 'searchbox_input'),
            (By.ID, 'search_form_input'),
            (By.NAME, 'q'),
            (By.CSS_SELECTOR, "input[type='search']"),
        ]

        caixa = None
        for sel in possible_selectors:
            try:
                caixa = navegador.find_element(*sel)
                if caixa:
                    break
            except Exception:
                caixa = None

        assert caixa is not None, 'Não foi possível localizar a caixa de busca.'

        caixa.clear()
        caixa.send_keys(palavras_busca)
        caixa.submit()

        # 2. Espera pelos resultados aparecerem: alguns sites (DuckDuckGo) podem não
        # expor imediatamente um container com id '#links'. Em vez de depender apenas
        # desse id, aguardamos que UMA das condições abaixo ocorra dentro do timeout:
        # - exista o elemento '#links' OU
        # - existam elementos que pareçam resultados (vários seletores comuns)
        WebDriverWait(navegador, 20).until(lambda d: d.execute_script(
            "return document.querySelector('#links') !== null || "
            "document.querySelectorAll('.result, #links .result, #links > div, "
            ".result__body, .result__title, .result__a, .result__snippet').length > 0"
        ))

        # coleta elementos que parecem resultados usando vários seletores comuns
        link_divs = navegador.find_elements(
            By.CSS_SELECTOR,
            '#links .result, #links > div, .result, '
            '.result__body, .result__title, .result__a, .result__snippet'
        )
        assert len(link_divs) > 0, 'Nenhum resultado encontrado na página.'

        # filtra os elementos de resultado pelo texto pesquisado
        busc_lower = palavras_busca.lower()
        resultados_texto = [
            el for el in link_divs
            if el.text and busc_lower in el.text.lower()
        ]
        assert len(
            resultados_texto) > 0, 'Nenhum resultado contendo o texto esperado foi encontrado.'

        # Re-obtem o campo de busca (garante que estamos verificando o elemento correto) e valida o valor
        caixa_de_busca = navegador.find_element(
            By.CSS_SELECTOR, "input#search_form_input, input#searchbox_input, input[name='q'], input[type='search']")
        assert caixa_de_busca.get_attribute('value') == palavras_busca

    except Exception:
        # ao ocorrer erro, salva artefatos para diagnóstico
        try:
            base = os.path.dirname(__file__)
            artifacts_dir = os.path.join(base, 'test_artifacts')
            os.makedirs(artifacts_dir, exist_ok=True)
            ts = time.strftime('%Y%m%d_%H%M%S')
            png = os.path.join(artifacts_dir, f'failure_{ts}.png')
            html = os.path.join(artifacts_dir, f'failure_{ts}.html')
            try:
                navegador.save_screenshot(png)
            except Exception:
                # se screenshot falhar, continuar para salvar page source
                pass
            try:
                with open(html, 'w', encoding='utf-8') as f:
                    f.write(navegador.page_source)
            except Exception:
                pass
        except Exception:
            pass
        raise
    finally:
        try:
            navegador.close()
        except Exception:
            pass
        try:
            navegador.quit()
        except Exception:
            pass
