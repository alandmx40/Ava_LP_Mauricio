import Pedido
import Produto

def pagar(codPed):
    total = 0

    for x in range(len(Pedido.listaItens)):
        if Pedido.listaItens[x][0] == codPed:
            for y in range(len(Produto.listaProdutos)):
                if Pedido.listaItens[x][1] == Produto.listaProdutos[y][0]:
                    total = total + ((Pedido.listaItens[x][2])*(Produto.listaProdutos[y][2]))

    print(f'TOTAL do PEDIDO: {total}')        