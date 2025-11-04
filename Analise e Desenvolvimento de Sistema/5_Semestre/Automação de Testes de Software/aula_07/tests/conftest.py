import os
from pytest import fixture
from selenium import webdriver
from pathlib import Path


@fixture
def form_aluno():
    chrome = webdriver.Chrome()
    pasta_conftest = Path(__file__).parent
    caminho_absoluto = pasta_conftest.parent / 'app' / 'aluno.html'
    url_local = caminho_absoluto.as_uri()
    chrome.get(f'{url_local}')
    yield chrome
    chrome.close()
