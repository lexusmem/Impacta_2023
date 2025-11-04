import os
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome = Chrome()

local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}/pagina01.html'

chrome.get(local_path)

select_element = chrome.find_element(By.NAME, 'opcoes')
select_object = Select(select_element)

select_object.select_by_index(1)
time.sleep(2)

select_object.select_by_value('3')
time.sleep(2)

select_object.select_by_visible_text('PHP')
time.sleep(2)

select_object.select_by_visible_text('Python')
time.sleep(2)
