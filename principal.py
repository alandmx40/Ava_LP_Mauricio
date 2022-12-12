import os
clear = lambda: os.system('cls')
import time

opcao = 1
codigo = 0
cod = 0
codigopedido = 0
codigoproduto = 0

while opcao == 1:
    
    print("LANCHONETE DOIS IRMÃOS - SEJA BEM VINDO\n")
    print("DIGITE A OPÇÃO DESEJADA: \n\n")
    print(
    "1 - CADASTRAR CLIENTE\n2 - ALTERAR/EXCLUIR CLIENTE\n3 - CONSULTAR CLIENTES\n4 - CADASTRAR MATERIA-PRIMA\n5 - ALTERAR/EXCLUIR MATERIA-PRIMA\n6 - CONSULTAR ESTOQUE DE MATÉRIA-PRIMA\n7 - CADASTRAR PRODUTO\n8 - ALTERAR/EXCLUIR PRODUTO\n9 - CONSULTAR PRODUTOS\n10 - CADASTRAR PEDIDO\n11 - ALTERAR/EXCLUIR PEDIDO\n12 - CONSULTAR PEDIDOS\n13 - PAGAMENTO\n14 - SAIR"
    )

    #TELA INICIAL ONDE O USUARIO E DIRECIONADO PARA TELA DESEJADA

    tela = int(input())

    if tela == 1:
        import Cliente
        
        op = 1
        
        while op == 1:

            codigo = codigo + 1
            nome = input("\nNOME COMPLETO: ")
            cpf = input("CPF (APENAS NUMEROS):")
            celular = input("CELULAR:")
            endereco = input("ENDERECO: ")
            Cliente.cadastrar(codigo, nome, cpf, celular, endereco)

            op = int(input("\n\nDESEJA CADASTRAR OUTRO CLIENTE: 1 - SIM | 2 - NAO\n\n"))
            
    elif tela == 2:
        import Cliente
        Cliente.alterar()
        os.system('pause')
    elif tela == 3:
        import Cliente
        print("\n")
        Cliente.listar()
        print("\n")
        os.system('pause')
    elif tela == 4:
        import Materia
        op = 1
        

        while op == 1:
            cod = cod + 1 
            nome = input("Nome da matéria-prima: \n")
            quant = int(input("Quantidade: \n"))
            val = input("Validade \n")
            Materia.cadastrar(cod, nome, quant, val)

            op = int(input("\n\nDESEJA CADASTRAR OUTRA MATERIA: 1 - SIM | 2 - NAO\n\n"))
    elif tela == 5:
        import Materia
        Materia.alterar()
        os.system('pause')
    elif tela == 6:
        import Materia
        print("\n")
        Materia.listar()
        print("\n")
        os.system('pause')
    elif tela == 7:
        import Produto
        op = 1
        

        while op == 1:
            codigoproduto = codigoproduto + 1
            nome = input("\nNOME: ")
            valor = float(input("VALOR:"))
            Produto.cadastrar(codigoproduto, nome, valor)
            op = int(input("\n\nDESEJA CADASTRAR OUTRO PRODUTO: 1 - SIM | 2 - NAO\n\n"))
            
    elif tela == 8:
        import Produto
        Produto.alterar()
        os.system('pause')
    elif tela == 9:
        import Produto
        print("\n")
        Produto.listar()
        print("\n")
        os.system('pause')
    elif tela == 10:

        import Pedido
        codCli = int(input("Digite o Código do Cliente: \n"))
        codigopedido = codigopedido + 1
        op = 1
        Pedido.cadastrar(codigopedido, codCli)

    elif tela == 11:
        import Pedido
        Pedido.alterar()
        os.system('pause')
    elif tela == 12:
        print("\n")
        import Pedido
        Pedido.listar()
        print("\n")
        os.system('pause')
    elif tela == 13:
        import pagamento
        pagarped = int(input("Digite o código do pedido: \n"))
        pagamento.pagar(pagarped)
        os.system('pause')
    elif tela == 14:
        opcao = 2
    clear()
clear()