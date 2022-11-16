class Node:

    def __init__(self, chave):
        self.dado = chave
        self.esq = None
        self.dir = None


def inserir(raiz, x):
    if raiz is None:
        return Node(x)
    if x < raiz.dado:
        raiz.esq = inserir(raiz.esq, x)
    elif x > raiz.dado:
        raiz.dir = inserir(raiz.dir, x)
    return raiz


def kesimomenor(raiz):
    global k

    if raiz is None:
        return None

    esquerda = kesimomenor(raiz.esq)

    if esquerda is not None:
        return esquerda

    k -= 1
    if k == 0:
        return raiz

    return kesimomenor(raiz.dir)


def printar(raiz):
    res = kesimomenor(raiz)

    if res is None:
        print("Há menos que k nós na árvore.")
    else:
        print("O elemento é", res.dado)


if __name__ == '__main__':

    raiz = None
    chaves = [16, 11, -5, 13, 15, 18, 20]

    for x in chaves:
        raiz = inserir(raiz, x)

    k = 4

    printar(raiz)
