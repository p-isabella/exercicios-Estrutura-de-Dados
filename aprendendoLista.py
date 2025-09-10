class No():
    def __init__(self, dado, next=None):
        self.data = dado
        self.next = next

class ListaLigada():
    def __init__(self):
        self.head = None 

    def AdicionarNo(self, dado):
        novo = No(dado)

        if not self.head:
            self.head = novo
            return
        
        atual = self.head

        while atual.next: 
            atual = atual.next
        atual.next = novo

    def exibir(self):
        atual = self.head
        while atual:
            print(atual.data, " ")
            atual = atual.next

    # def reverse(self):
    #     variavel = self.head
    #     anterior = None
    #     while (variavel.proximo):
    #         print(variavel.dado)
    #         variavel = variavel.proximo
    #         inversoVariavel = variavel
    #         inversoVariavel = variavel.proximo
    #         print(inversoVariavel.dado)
        


lista = ListaLigada()
lista.AdicionarNo(2)
lista.AdicionarNo(5)
lista.AdicionarNo(8)
lista.exibir()