listaProdutos = list()

def cadastrar(codigo, nome, valor):

    produto = [codigo, nome, valor]
    listaProdutos.append(produto[:])
    print("PRODUTO CADASTRADO COM SUCESSO!")


def listar():
    for x in range(len(listaProdutos)):
        print(f'Código: {listaProdutos[x][0]} | Nome: {listaProdutos[x][1]} | Valor: {listaProdutos[x][2]}')

def alterar():
    op = int(input("1 - ALTERAR DADOS | 2 - EXCLUIR PRODUTO\n"))
    
    
    if op == 1:
        
        op2 = int(input("\n\n1 - EDITAR NOME | 2 - EDITAR VALOR \n"))
        codPro = int(input("DIGITE O CODIGO DO PRODUTO\n"))
        esc = input(f'Esse é o produto que deseja alterar? Nome: {listaProdutos[codPro-1][1]} Valor: {listaProdutos[codPro-1][2]} | S - Sim /N - Não\n')
        if esc == 'S' or esc == 's':
            if op2 == 1:
                nome = input("DIGITE O NOVO NOME: \n")
                listaProdutos[codPro-1][1] = nome
            elif op2 == 2:
                valor = float(input("DIGITE O NOVO VALOR: \n"))
                listaProdutos[codPro-1][2] = valor
        else:
            print("VERIFIQUE O CÓDIGO DO PRODUTO E TENTE NOVAMENTE!\n")
    elif op == 2:
        codPro = int(input("Digite o codigo do produto: "))
        esc = input(f'Esse é o produto que deseja excluir? Nome: {listaProdutos[codPro-1][1]} Valor: {listaProdutos[codPro-1][2]} | S - Sim /N - Não\n')
        if esc == 'S' or 's':
            listaProdutos.remove(listaProdutos[codPro-1])
            print("PRODUTO EXCLUIDO COM SUCESSO!")
        else:
            print("VERIFIQUE O CÓDIGO DO PRODUTO E TENTE NOVAMENTE!\n")