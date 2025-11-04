from selenium.webdriver.common.by import By


def test_localizar_campo_nome(form_aluno):
    campo_nome = form_aluno.find_element(By.NAME, 'nome_aluno')
    assert campo_nome.tag_name == 'input'
    assert campo_nome.get_attribute('placeholder') == 'Nome do Aluno'
    assert campo_nome.get_attribute('type') == 'text'


def test_localizar_campo_email(form_aluno):
    campo_email = form_aluno.find_element(By.NAME, 'email')
    assert campo_email.tag_name == 'input'
    assert campo_email.get_attribute('placeholder') == 'E-mail do Aluno'
    assert campo_email.get_attribute('type') == 'email'


def test_localizar_campo_login(form_aluno):
    campo_login = form_aluno.find_element(By.NAME, 'login')
    assert campo_login.tag_name == 'input'
    assert campo_login.get_attribute('type') == 'submit'
    assert campo_login.get_attribute('value') == 'Login'


def test_localizar_form_aluno(form_aluno):
    form_aluno = form_aluno.find_element(By.ID, 'FormAluno')
    assert form_aluno.tag_name == 'form'


def test_verificar_titulo_do_form(form_aluno):
    assert form_aluno.title == 'Cadastro de Alunos'
