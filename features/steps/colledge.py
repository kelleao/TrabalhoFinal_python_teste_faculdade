from behave import *
from homepage import HomePage
from selenium import webdriver


# @given(u'que um aluno é criado')
# def step_impl(context):
#     driver = webdriver.Chrome()
#     vars = {} 
#     hp = HomePage(driver)
#     driver.get("https://tdd-detroid.onrender.com/")
#     driver.set_window_size(970, 555)
#     hp.wait_page_load()
#     context.homepage = hp
         
#     hp.add_student("raquel leao")

# @given(u'1 curso é software de Teste')
# def step_impl(context):
#     hp = context.homepage
#     hp.add_course_temp("Software de testes")


# @when(u'o aluno é matriculado em um software de Teste com id 1')
# def step_impl(context):
#      hp = context.homepage
#      hp.add_student_to_course()


# @when(u'a disciplina é adicionada ao software de Teste com id 1')
# def step_impl(context):
#      hp = context.homepage
#      hp.add_discipline_temp("Automacao de Teste")    
#      hp.subcribe_discipline_to_course()


# @then(u'o aluno é matriculado em disciplinas com id 1,2,3')
# def step_impl(context):
#     hp = context.homepage
#     hp.subscribe_student_to_discipline(1, 2)
#     hp.subscribe_student_to_discipline(2, 3)
#     hp.subscribe_student_to_discipline(3, 4)


# @given(u'2 curso é Teste de API')
# def step_impl(context):
#     hp = context.homepage
#     hp.add_course_temp("Teste de API")


# @when(u'o aluno é matriculado em um Teste de API com id 1')
# def step_impl(context):
#      hp = context.homepage
#      hp.add_student_to_course()


# @when(u'a disciplina é adicionadas ao Teste de API com id 1')
# def step_impl(context):
#      hp = context.homepage
#      hp.add_discipline_temp("Teste api")    
#      hp.subcribe_discipline_to_course()


# @given(u'3 curso é Teste de Aplicacao Mobile')
# def step_impl(context):
#     hp = context.homepage
#     hp.add_course_temp("Teste de Aplicacao Mobile")

# @when(u'o aluno é matriculado em um Teste de Aplicacao Mobile com id 1')
# def step_impl(context):
#     hp = context.homepage
#     hp.add_student_to_course()


# @when(u'a disciplina é adicionadas ao Teste de Aplicacao Mobile com id 1')
# def step_impl(context):
#      hp = context.homepage
#      hp.add_discipline_temp("Teste api")    
#      hp.subcribe_discipline_to_course()


# @then(u'o aluno é matriculado em disciplina2 com id 1,2,3')
# def step_impl(context):
#     hp = context.homepage
#     hp.subscribe_student_to_discipline(1,3)
#     hp.subscribe_student_to_discipline(1,4)

@given(u'que existe um aluno com nome "Raquel Leao"')
def step_create_student(context):
    driver = webdriver.Chrome()
    vars = {} 
    hp = HomePage(driver)
    driver.get("https://tdd-detroid.onrender.com/")
    driver.set_window_size(970, 555)
    hp.wait_page_load()
    context.homepage = hp
         
    hp.add_student("raquel leao")


@given(u'existem os cursos "Teste de Software", "Teste de seguranca", "Teste de seguranca"')
def step_create_courses(context):
    hp = context.homepage
    hp.add_course_temp("Software de testes")
    hp.add_course_temp("Teste de seguranca")
    hp.add_course_temp("Teste de seguranca")


@when(u'o aluno é inscrito no curso com id 1')
def step_impl(context):
    hp = context.homepage
    hp.add_student_to_course()


@when(u'o curso com id 1 possui as disciplinas')
def step_impl(context):
    hp = context.homepage
    hp.add_discipline_temp("Automacao de Teste")    
    hp.subcribe_discipline_to_course()


@when(u'o aluno é inscrito nas disciplinas com ids 1, 2, 3')
def step_student_in_disciplines(context):
    hp = context.homepage
    hp.subscribe_student_to_discipline(1, 1)
    hp.subscribe_student_to_discipline(2, 3)
    hp.subscribe_student_to_discipline(3, 4)


@then(u'o aluno deve estar inscrito no curso "Teste de API", "Teste de Aplicacao Moblie", "Teste de Nuvem"')
def step_verify_student_in_course(context):
    hp = context.homepage
    hp.add_discipline_temp("Teste de API")   
    hp.add_discipline_temp("Teste de Aplicacao Moblie")     
    hp.add_discipline_temp("Teste de Nuvem")      
    hp.subcribe_discipline_to_course()

@then(u'o aluno deve estar inscrito nas disciplinas')
def step_verify_student_in_disciplines(context):
    hp = context.homepage
    hp.subscribe_student_to_discipline(2, 1)
    hp.subscribe_student_to_discipline(2, 1)
    hp.subscribe_student_to_discipline(2, 4)