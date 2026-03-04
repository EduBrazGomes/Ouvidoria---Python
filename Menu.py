from jupyter_server.auth import passwd

import Ouvidoria
import operacoesbd
opcao = -1

conexao = operacoesbd.criarConexao("localhost","root","$$EduardoGomes#2025$$","locadora_1")
while opcao != 6 :
    print('''
    Opções:
    1) Listagem das manifestações  
    2) Pesquisar uma manifestação por código
    3) Adicionar uma nova manifestação
    4) Quantidade total de manifestações
    5) Remover manifestação por código  
    6) Sair 
    ''')

    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        Ouvidoria.listar_filmes(conexao)

    elif opcao == 2:
        Ouvidoria.pesquisar_por_codigo(conexao)

    elif opcao == 3:
        Ouvidoria.adicionar_manifestacao(conexao)

    elif opcao == 4:
        Ouvidoria.quantidade_manifestacoes(conexao)

    elif opcao == 5:
        Ouvidoria.remover_por_codigo(conexao)

    elif opcao != 6:
        print("Opção inválida")

operacoesbd.encerrarConexao(conexao)
print("Agradecemos a oportunidade de atendê-lo(a)")
