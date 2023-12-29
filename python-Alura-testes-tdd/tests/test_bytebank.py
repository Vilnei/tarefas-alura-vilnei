from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        assert resultado == esperado

    # Arrange-Act-Assert   /    Given-When-Then

    def test_quando_nome_completo_retornar_apenas_ultimo_nome(self):
        entrada = 'vilnei martins de lima'
        esperado = 'lima'

        funcionario_teste2 = Funcionario(entrada, '09/04/1989', 1111)
        resultado = funcionario_teste2.sobrenome()

        assert resultado == esperado
