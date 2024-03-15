import requests

caminho = '.\\Impacta_2023\\Analise e Desenvolvimento de Sistema\\2_Semestre\\Programação_Orientada_a_Objetos\\'

url_logo_google = (
    'https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_r5.png'
)

response = requests.get(url_logo_google)
print(response)

with open(f'{caminho}logo_google_12.png', 'wb') as f:
    f.write(response.content)
