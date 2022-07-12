#Usando conceitos de programação estruturada (Vetor), criar em pseudocódigo um menu para simular um cadastro para uma agência de viagens com as seguintes funções: cadastro de cliente e cadastro de destino, criar também uma consulta para cada estrutura de dados.

"""
    Primeiramente peço sinceras desculpas, mas tive um terrível problema no meu visualG (ou na minha máquina) pouco antes de desenvolver a solução. Tive muitos contratempos nesses últimos dias, e reconheço que talvez não haja desculpa pelo que vou apresentar, porém dou-llhes no mínimo uma justificativa mesmo assim. De tal forma que envio este páreo em Python. Ao menos o que tentei de última hora. Mais uma vez peço desculpas e me ponho à disposição...
"""

while True:
    print("Bem vindo!")
    print("""Entre com sua opção por favor:
    1-Cadastrar clientes
    2-Cadastrar destinos
    3-Consultar clientes
    4-Consultar destinos
    5-Sair
    """)
    tabela_cliente = [["", "", ""], ["", "",  ""], ["", "", ""]]
    tabela_destino = [["", "", ""], ["", "", ""], ["", "", ""]]
    l = c = 0
    escolha = int(input())
    if escolha == 5:
        break
    else:


        if escolha == 1:
            print("Digite em sequência: Nome, Telefone e CPF\n")
            for l in range(0, 3):
                for c in range(0, 3):
                    tabela_cliente[l][c] = str(input(f'Digite {l} x {c}  '))

        elif escolha == 2:
            print("Digite em sequência: Local, Hospedagem e Período\n")
            for l in range(0, 3):
                for c in range(0, 3):
                    tabela_destino[l][c] = str(input(f'Digite {l} x {c}  '))

        elif escolha == 3:
            for l in range(0, 3):
                for c in range(0, 3):
                    print(f'[{tabela_cliente[l][c]:^20}]', end='')
                print()

        elif escolha == 4:
            for l in range(0, 3):
                for c in range(0, 3):
                    print(f'[{tabela_destino[l][c]:^20}]', end='')
                print()


        else:
            print("Opção errada!")



