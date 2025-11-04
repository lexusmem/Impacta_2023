from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get('http://google.com.br')
chrome.maximize_window()
print('título:', chrome.title)
print('endereço URL:', chrome.current_url)
print('código fonte:', chrome.page_source[:100])
chrome.close()
