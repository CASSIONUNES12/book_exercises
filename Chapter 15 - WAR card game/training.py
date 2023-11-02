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
        v = self.valores[self.valor] + " de " + self.naipes[self.naipe]
        return v
        

from random import shuffle

class Baralho:
    lista_baralho = []

    def __init__(self):
        for i in range(2, 15):
            for j in range(4):
                self.lista_baralho.append(Card(i, j))

        shuffle(self.lista_baralho)

    def remove_card(self):
        if len(self.lista_baralho) == 0:
            return
        return self.lista_baralho.pop()
    

class Jogador():
    def __init__(self, name):
        self.wins = 0
        self.cartas = None
        self.name = name

class Jogo():
    def __init__(self):
        name1 = input("J1, coloque seu nome: ")
        name2 = input("J2, coloque seu nome: ")
        self.baralho = Baralho()
        self.jogador1 = Jogador(name1)
        self.jogador2 = Jogador(name2)


    def jogar(self):
        pc = self.baralho.lista_baralho
        text = None
        
               
        while len(pc) >= 2 and text != 'q':
            text = input("\nPressione Q para sair ou qualquer outra tecla para continuar: ")

            carta_j1 = self.baralho.remove_card()
            carta_j2 = self.baralho.remove_card()
            
            print("\n{} tirou {} e {} tirou {}".format(self.jogador1.name, carta_j1, self.jogador2.name, carta_j2))
            
            if carta_j1 > carta_j2:
                    self.jogador1.wins += 1
                    print("{} venceu essa rodada".format(self.jogador1.name))
                    print("O placar atual está: {} x {}".format(self.jogador1.wins, self.jogador2.wins))
            else:
                    self.jogador2.wins += 1
                    print("{} venceu essa rodada.".format(self.jogador2.name))
                    print("O placar atual está: {} x {}".format(self.jogador1.wins, self.jogador2.wins))
        
    
        if len(pc) < 2:
            if self.jogador1.wins > self.jogador2.wins:
                print("O jogo acabou. {} ganhou!".format(self.jogador1.name))
            elif self.jogador1.wins < self.jogador2.wins:
                print("O jogo acabou. {} ganhou!".format(self.jogador2.name))
            else:
                print("O jogo acabou empatado!")
        
                   

jogo = Jogo()
jogo.jogar()
