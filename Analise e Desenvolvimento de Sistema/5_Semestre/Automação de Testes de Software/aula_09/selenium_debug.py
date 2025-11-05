from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
try:
    driver.get('http://www.duckduckgo.com')
    time.sleep(2)
    try:
        el = driver.find_element(
            By.CSS_SELECTOR, "input#searchbox_input, input#search_form_input, input[name='q'], input[type='search']")
        print("found input: id=", el.get_attribute(
            'id'), "name=", el.get_attribute('name'))
    except Exception as e:
        print('input not found:', e)
    try:
        el.send_keys('Page Object')
        el.submit()
    except Exception as e:
        print('submit failed:', e)
    time.sleep(3)
    print('URL:', driver.current_url)
    print('title:', driver.title)
    page_len = len(driver.page_source)
    print('page length:', page_len)
    counts = driver.execute_script(
        "return {links: document.querySelectorAll('#links').length, results: document.querySelectorAll('#links .result, #links > div, .result__body, .result__title').length};")
    print('counts:', counts)
    with open('debug_page.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source[:10000])
    print('saved first 10000 chars to debug_page.html')
finally:
    driver.quit()
