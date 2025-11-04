from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver  # Certifique-se de ter esta importação


def test_busca_site_duckduckgo():
    navegador = webdriver.Chrome()
    navegador.get('http://www.duckduckgo.com')
    palavras_busca = "Page Object"

    # 1. Espera para a caixa de busca carregar (Boa Prática)
    WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.ID, 'searchbox_input'))
    )

    caixa = navegador.find_element(By.ID, 'searchbox_input')
    caixa.send_keys(palavras_busca)
    caixa.submit()

    # 2. ESPERA CRÍTICA: Espera pelos resultados aparecerem
    # Tentaremos com o seu seletor original primeiro.
    # Espera até 10 segundos até que os elementos estejam presentes no DOM.
    try:
        WebDriverWait(navegador, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#links > div'))
        )
    except:
        print("Atenção: Tempo esgotado (10s) aguardando os resultados. Tentando seletor alternativo.")
        # Se falhar, tenta o seletor alternativo (#links .result)
        WebDriverWait(navegador, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#links .result'))
        )

    # link_divs = navegador.find_elements(By.CSS_SELECTOR, '#links > div')
    link_divs = navegador.find_elements(By.CSS_SELECTOR, '#links .result')

    assert len(link_divs) > 0
    xpath = f"//div[@id='links']//*[contains(text(), '{palavras_busca}')]"
    resultados = navegador.find_elements(By.XPATH, xpath)
    assert len(resultados) > 0
    caixa_de_busca = navegador.find_element(By.ID, 'search_form_input')
    assert caixa_de_busca.get_attribute('value') == palavras_busca
    navegador.close()
    navegador.quit()
