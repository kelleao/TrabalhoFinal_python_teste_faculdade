Feature: Gerenciamento de Alunos e Cursos

Scenario: Criar um aluno, cursos, disciplinas realizar inscrições
    Given que existe um aluno com nome "Raquel Leao"
    And existem os cursos "Teste de Software", "Teste de seguranca", "Teste de seguranca"
    When o aluno é inscrito no curso com id 1
    And o curso com id 1 possui as disciplinas 
    And o aluno é inscrito nas disciplinas com ids 1, 2, 3
    Then o aluno deve estar inscrito no curso "Teste de API", "Teste de Aplicacao Moblie", "Teste de Nuvem"
    And o aluno deve estar inscrito nas disciplinas
