from random import shuffle

class Card:

    naipes = ("espadas", "copas", "ouros", "paus")

    valores = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei", "Ás")

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        
    def __gt__(self, card2):
        if self.valor > card2.valor:
            return True
        if self.valor == card2.valor:
            if self.naipe > card2.naipe:
                return True
            else:
                return False
            
    def __lt__(self, card2):
        if self.valor < card2.valor:
            return True
        if self.valor == card2.valor:
            if self.naipe < card2.naipe:
                return True
            else:
                return False
            
    def __repr__(self):
        rep = self.valores[self.valor] + " de " + self.naipes[self.naipe]
        return rep

class Baralho:
    lista_baralho = []

    def __init__(self):
        for i in range(2, 15):
            for j in range(4):
                self.lista_baralho.append(Card(i, j))


        shuffle(self.lista_baralho)    

    def remover_cartas(self):
        if len(self.lista_baralho) == 0:
            return
        return self.lista_baralho.pop()  
    
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vitorias = 0
        self.cartas = None

class Jogo:
    def __init__(self):
        nome1 = input("J1, insira seu nome: ")
        nome2 = input("J2, insira seu nome: ")
        self.baralho = Baralho()
        self.j1 = Jogador(nome1)
        self.j2 = Jogador(nome2)

    
    def jogar(self):
        bj = self.baralho.lista_baralho
        resposta = None
        print("\nQUE COMECE A GUERRA!!")

        while len(bj) >= 2 and resposta != 'q'.lower:
            resposta = input("\nPressione Q para sair ou qualquer outra tecla para continuar ")
            cj1 = self.baralho.remover_cartas()
            cj2 = self.baralho.remover_cartas()
            print(f"\n{self.j1.nome} tirou {cj1}  e  {self.j2.nome} tirou {cj2}")

            if cj1 > cj2:
                self.j1.vitorias += 1
                print(f"\n{self.j1.nome} ganhou essa rodada")
                print(f"placar: {self.j1.nome} {self.j1.vitorias}  x  {self.j2.nome} {self.j2.vitorias}")
            else:
                self.j2.vitorias += 1
                print(f"\n{self.j2.nome} ganhou essa rodada")
                print(f"placar: {self.j1.nome} {self.j1.vitorias}  x  {self.j2.nome} {self.j2.vitorias}")


            if len(bj) < 2:
                if self.j1.vitorias > self.j2.vitorias:
                    print("\nO jogo ababou. {} venceu".format(self.j1.nome))
                elif self.j1.vitorias < self.j2.vitorias:
                    print("\nO jogo ababou. {} venceu".format(self.j2.nome))           
                else:
                    print("\nO jogo ababou.Foi um empate!")
                break
            

jogo = Jogo()
jogo.jogar()




