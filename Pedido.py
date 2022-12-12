listaPedidos = list()
listaItens = list()

def cadastrar(codigo, codCli):
    op = 1
    while op == 1:
      codPro = int(input("Digite o Código do Produto: \n"))
      quant = int(input("Digite a quantidade: \n"))
      item = [codigo, codPro, quant]
      listaItens.append(item[:])
      op = int(input("DESEJA INCLUIR OUTRO PRODUTO? 1 - SIM | 2 - NÃO\n"))
      

    pedido = [codigo, codCli, listaItens]
    listaPedidos.append(pedido[:])
    print("PEDIDO CADASTRADO COM SUCESSO!")

def listar():
    for x in range(len(listaPedidos)):
        print(f'Código do Pedido: {listaPedidos[x][0]} | Código do Cliente: {listaPedidos[x][1]} \n')
        for y in range(len(listaItens)):
          if listaItens[y][0] == listaPedidos[x][0]:
            print(f'Código do Produto: {listaItens[y][1]} | Quantidade: {listaItens[y][2]} \n')
        print("___________________________________________")
          
def alterar():
    op = int(input("1 - ALTERAR PEDIDO | 2 - EXCLUIR PEDIDO\n"))
    
    
    if op == 1:
        
        op2 = int(input("\n\n1 - EDITAR CLIENTE | 2 - EDITAR PRODUTO | 3 - EDITAR QUANTIDADE | 4 - ADICIONAR PRODUTOS \n"))
        codPedido = int(input("DIGITE O CODIGO DO PEDIDO\n"))
        esc = input(f'Esse é o pedido que deseja alterar? Código do Cliente: {listaPedidos[codPedido-1][1]}| S - Sim /N - Não\n')
        if esc == 'S' or esc == 's':
            if op2 == 1:
                codCliente = int(input("DIGITE O NOVO CÓDIGO DO CLIENTE: \n"))
                listaPedidos[codPedido-1][1] = codCliente
                print("ALTERADO COM SUCESSO!")
            elif op2 == 2:
                codantigo = int(input("DIGITE O ATUAL CÓDIGO DO PRODUTO QUE CONSTA NO PEDIDO: \n"))
                nCodProduto = int(input("DIGITE O NOVO CÓDIGO DO PRODUTO: \n"))
                for y in range(len(listaItens)):
                  if listaItens[y][0] == codPedido and listaItens[y][1] == codantigo:
                    listaItens[y][1] = nCodProduto
                    print("ALTERADO COM SUCESSO!")
            elif op2 == 3:
                aux = int(input("DIGITE O CÓDIGO DO PRODUTO: \n"))
                nquant = int(input("DIGITE A NOVA QUANTIDADE DO PRODUTO: \n"))
                for y in range(len(listaItens)):
                  if listaItens[y][0] == codPedido and listaItens[y][1] == aux:
                    listaItens[y][2] = nquant
                    print("ALTERADO COM SUCESSO!")
            elif op2 == 4:
                op = 1
                while op == 1:
                  codPro = int(input("Digite o Código do Produto: \n"))
                  quant = int(input("Digite a quantidade: \n"))
                  op = int(input("DESEJA INCLUIR OUTRO PRODUTO? 1 - SIM | 2 - NÃO\n"))
                  item = [codPedido, codPro, quant]
                  listaItens.append(item[:])
                  print("INCLUIDO COM SUCESSO!")
        else:
            print("VERIFIQUE O CÓDIGO DO PEDIDO E TENTE NOVAMENTE!\n")
    elif op == 2:
        codPedEx = int(input("Digite o código do pedido: "))
        esc = input(f'Esse é o pedido que deseja excluir? Código do Cliente: {listaPedidos[codPedEx-1][1]} | S - Sim /N - Não\n')
        if esc == 'S' or 's':
            listaPedidos.remove(listaPedidos[codPedEx-1])
            print("PEDIDO EXCLUIDO COM SUCESSO!")
        else:
            print("VERIFIQUE O CÓDIGO DO PEDIDO E TENTE NOVAMENTE!\n")

