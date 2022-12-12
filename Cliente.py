
listaClientes = list()

def cadastrar(codigo, nome, cpf, celular, endereco):

    cliente = [codigo, nome, cpf, celular, endereco]
    listaClientes.append(cliente[:])
    print("CLIENTE CADASTRADO COM SUCESSO!")

def listar():
    for x in range(len(listaClientes)):
        print(f'Codigo: {listaClientes[x][0]} | Nome: {listaClientes[x][1]} | CPF: {listaClientes[x][2]} | CELULAR: {listaClientes[x][3]} | CELULAR: {listaClientes[x][4]} ')

def alterar():
    op = int(input("1 - ALTERAR DADOS | 2 - EXCLUIR CLIENTE\n"))
    
    
    if op == 1:
        
        op2 = int(input("\n\n1 - EDITAR NOME | 2 - EDITAR CPF | 3 - EDITAR CELULAR | 4 - EDITAR ENDERECO\n"))
        codCli = int(input("DIGITE O CODIGO DO CLIENTE\n"))
        esc = input(f'Esse é o cliente que deseja alterar? Nome: {listaClientes[codCli-1][1]} CPF: {listaClientes[codCli-1][2]} | S - Sim /N - Não\n')
        if esc == 'S' or esc == 's':
            if op2 == 1:
                nome = input("DIGITE O NOVO NOME: \n")
                listaClientes[codCli-1][1] = nome
                print("ALTERADO COM SUCESSO!")
            elif op2 == 2:
                cpf = input("DIGITE O NOVO CPF: \n")
                listaClientes[codCli-1][2] = cpf
                print("ALTERADO COM SUCESSO!")
            elif op2 == 3:
                celular = input("DIGITE O NOVO CELULAR: \n")
                listaClientes[codCli-1][3] = celular
                print("ALTERADO COM SUCESSO!")
            elif op2 == 4:
                endereco = input("DIGITE O NOVO ENDEREÇO: \n")
                listaClientes[codCli-1][4] = endereco
                print("ALTERADO COM SUCESSO!")
        else:
            print("VERIFIQUE O CÓDIGO DO CLIENTE E TENTE NOVAMENTE!\n")
    elif op == 2:
        codCli = int(input("Digite o codigo do cliente: "))
        esc = input(f'Esse é o cliente que deseja excluir? Nome: {listaClientes[codCli-1][1]} CPF: {listaClientes[codCli-1][2]} | S - Sim /N - Não\n')
        if esc == 'S' or 's':
            listaClientes.remove(listaClientes[codCli-1])
            print("CLIENTE EXCLUIDO COM SUCESSO!")
        else:
            print("VERIFIQUE O CÓDIGO DO CLIENTE E TENTE NOVAMENTE!\n")