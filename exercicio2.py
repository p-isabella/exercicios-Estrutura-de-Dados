# O método reverse inverte os elementos da lista. Defina uma função chamada reverse
# que inverte os elementos no argumento de lista (sem usar o método reverse). Tente
# tornar essa função a mais eficiente possível e indique sua complexidade
# computacional usando a notação Big-O. 

class No():
    def __init__(self, dado, proximo=None):
        self.dado = dado
        self.proximo = proximo

class ListaLigada():
    def __init__(self):
        self.head = None
    
    def AdicionarNo(self, dado):
        novo = No(dado)

        if (not self.head):
            self.head = novo
            return
        
        atual = self.head

        while (atual.proximo):
            atual = atual.proximo
        atual.proximo = novo

    def reverse(self):
        inverso = None
        atual = self.head
        while atual:
            proximo = atual.proximo
            atual.proximo = inverso
            inverso = atual
            atual = proximo
        self.head = inverso

    def exibir(self):
        atual = self.head

        while (atual):
            print(atual.dado, " ")
            atual = atual.proximo
        

lista = ListaLigada()
lista.AdicionarNo(5)
lista.AdicionarNo(6)
lista.AdicionarNo(7)
lista.AdicionarNo(9)
lista.reverse()
lista.exibir()