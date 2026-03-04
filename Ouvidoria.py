import operacoesbd

def listar_filmes(conexao):
    consulta_listar = "select * from manifestacoes"
    lista_manifestacoes = operacoesbd.listarBancoDados(conexao, consulta_listar)

    if len(lista_manifestacoes) == 0:
        print("Até o momento, o sistema não possui nenhuma manifestação")
    else:
        print("Lista de manifestações em banco de dados: ")
        for manifestacao in lista_manifestacoes:
            print(f"Manifestação: {manifestacao[1]}, Código: {manifestacao[0]}")


def pesquisar_por_codigo(conexao):
    consulta_pesquisar = "select * from manifestacoes where codigo = %s"
    codigo_manifestacao= int(input("Digite o código da manifestação: "))
    dados = [codigo_manifestacao]

    lista_manifestacoes = operacoesbd.listarBancoDados(conexao, consulta_pesquisar, dados)

    if len(lista_manifestacoes) == 0:
        print("Não existe manifestação para o código informado.")
    else:
        print(f"Manifestação: {lista_manifestacoes[0][1]}, Código: {lista_manifestacoes[0][0]} ")


def adicionar_manifestacao(conexao):
    consulta_adicionar = "insert into manifestacoes (manifestacao) values(%s);"
    nova_manifestacao = input("Por favor, apresente a sua manifestação: ")

    dados = [nova_manifestacao]

    codigo_manifestacao = operacoesbd.insertNoBancoDados(conexao, consulta_adicionar, dados)
    print(f"Manifestação cadastrada com sucesso! o código da manifestação é '{codigo_manifestacao}'")

def quantidade_manifestacoes(conexao):
    consulta_quantidade = "select count(*) from manifestacoes"

    quantidade_manifestacoes = operacoesbd.listarBancoDados(conexao, consulta_quantidade)
    print(f"A quantidade de manifestações é: {quantidade_manifestacoes[0][0]} ")

def remover_por_codigo(conexao):
    codigo_manifestacao = int(input("Digite o código da manifestação: "))

    consulta = "delete from manifestacoes where codigo = %s"
    dados = [codigo_manifestacao]
    manifestacoes_removidas = operacoesbd.excluirBancoDados(conexao, consulta, dados)

    if manifestacoes_removidas == 0:
        print("Não existe manifestação para o código informado.")

    else:
        print("A manifestação foi excluída com sucesso.")


