'''1. Uma pesquisa sequencial de uma lista ordenada pode ser interrompida quando o alvo
é menor que determinado elemento na lista. Defina uma versão modificada desse
algoritmo e indique a complexidade computacional, usando a notação Big-O, do
desempenho nos casos melhor, pior e médio. '''

class no():
    def __init__(self, dado, proximo=None):
        self.dado = dado
        self.proximo = proximo
    
class ListaLigada():
    def __init__(self):
        self.head = None
    
    def AdicionarNo(self, dado):
        novo = no(dado)

        if (not self.head):
            self.head = novo
            return
        
        atual = self.head

        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo

    def Exibicao(self):
        atual = self.head
        while (atual):
            print(atual.dado, " ")
            atual = atual.proximo
    
    def busca(self, alvo):
        atual = self.head
        posicao = 0
        while (atual):
            
            if atual.dado == alvo:
                print(f"Achei! O número {atual.dado}")
                print("Está na posição:", posicao)
                print("-"*50)
                return 0
            if atual.dado > alvo:
                print("Inexistente.")

            posicao += 1
            atual = atual.proximo

        print("Inexistente. Chegou ao fim da lista.")
                

# Melhor caso: Quando o elemento está na primeira posição.
lista1 = ListaLigada()
lista1.AdicionarNo(2)
lista1.AdicionarNo(5)
lista1.AdicionarNo(8)
lista1.AdicionarNo(14)
lista1.busca(2)

# Caso mediano: Quando está no meio da lista.
lista2 = ListaLigada()
lista2.AdicionarNo(7)
lista2.AdicionarNo(10)
lista2.AdicionarNo(12)
lista2.AdicionarNo(14)
lista2.AdicionarNo(21)
lista2.busca(12)

# Pior caso: Quando está no fim da lista ou quando não existe:
lista3 = ListaLigada()
lista3.AdicionarNo(7)
lista3.AdicionarNo(10)
lista3.AdicionarNo(12)
lista3.AdicionarNo(14)
lista3.AdicionarNo(21)
lista3.busca(21)
lista3.busca(26)