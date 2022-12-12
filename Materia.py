listaMateria = list()

def cadastrar(codigo, nome, quant, val):

    materia = [codigo, nome, quant, val]
    listaMateria.append(materia[:])
    print("MATERIA CADASTRADA COM SUCESSO!")

def listar():
    for x in range(len(listaMateria)):
        print(f'Código: {listaMateria[x][0]} | Nome: {listaMateria[x][1]} | Quantidade: {listaMateria[x][2]} | Validade: {listaMateria[x][3]}')

def alterar():
    op = int(input("1 - ALTERAR DADOS | 2 - EXCLUIR MATERIA\n"))
    
    
    if op == 1:
        
        op2 = int(input("\n\n1 - EDITAR NOME | 2 - EDITAR QUANTIDADE | 3 - EDITAR VALIDADE \n"))
        codMat = int(input("DIGITE O CODIGO DA MATERIA\n"))
        esc = input(f'Essa é materia que deseja alterar? Nome: {listaMateria[codMat-1][1]} Quantidade: {listaMateria[codMat-1][2]} | S - Sim /N - Não\n')
        if esc == 'S' or esc == 's':
            if op2 == 1:
                nome = input("DIGITE O NOVO NOME: \n")
                listaMateria[codMat-1][1] = nome
                print("ALTERADO COM SUCESSO!")
            elif op2 == 2:
                quant = input("DIGITE A NOVA QUANTIDADE: \n")
                listaMateria[codMat-1][2] = quant
                print("ALTERADO COM SUCESSO!")
            elif op2 == 3:
                val = input("DIGITE A NOVA DATA DE VALIDADE: \n")
                listaMateria[codMat-1][3] = val
                print("ALTERADO COM SUCESSO!")
        else:
            print("VERIFIQUE O CÓDIGO DA MATÉRIA E TENTE NOVAMENTE!\n")
    elif op == 2:
        codMat = int(input("Digite o codigo da matéria: "))
        esc = input(f'Esse é a matéria que deseja excluir? Nome: {listaMateria[codMat-1][1]} Quantidade: {listaMateria[codMat-1][2]} | S - Sim /N - Não\n')
        if esc == 'S' or 's':
            listaMateria.remove(listaMateria[codMat-1])
            print("MATERIA EXCLUIDA COM SUCESSO!")
        else:
            print("VERIFIQUE O CÓDIGO DMATERIA E TENTE NOVAMENTE!\n")