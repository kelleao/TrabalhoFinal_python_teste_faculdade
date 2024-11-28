# Feature: Criar do aluno e dos cursos 


# Scenario: Criar aluno e curso software de Teste 
# Given que um aluno é criado 
# And 1 curso é software de Teste 
# When o aluno é matriculado em um software de Teste com id 1 
# And a disciplina é adicionada ao software de Teste com id 1 
# Then o aluno é matriculado em disciplinas com id 1,2,3 


# Scenario: criar curso Teste de API 
# Given 2 curso é Teste de API
# When o aluno é matriculado em um Teste de API com id 1 
# And a disciplina é adicionadas ao Teste de API com id 1 
# Then o aluno é matriculado em disciplinas com id 1,2,3 


# Scenario: criar curso Teste de Aplicacao Mobile 
# Given 3 curso é Teste de Aplicacao Mobile 
# When o aluno é matriculado em um Teste de Aplicacao Mobile com id 1 
# And a disciplina é adicionadas ao Teste de Aplicacao Mobile com id 1 
# Then o aluno é matriculado em disciplina2 com id 1,2,3 

Feature: Gerenciamento de Alunos e Cursos

Scenario: Criar um aluno, cursos, disciplinas realizar inscrições
    Given que existe um aluno com nome "Raquel Leao"
    And existem os cursos "Teste de Software", "Teste de seguranca", "Teste de seguranca"
    When o aluno é inscrito no curso com id 1
    And o curso com id 1 possui as disciplinas 
    And o aluno é inscrito nas disciplinas com ids 1, 2, 3
    Then o aluno deve estar inscrito no curso "Teste de API", "Teste de Aplicacao Moblie", "Teste de Nuvem"
    And o aluno deve estar inscrito nas disciplinas
