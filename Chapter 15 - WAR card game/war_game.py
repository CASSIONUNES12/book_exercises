class Card:

    naipes = ("espadas", "copas", "ouros", "paus")

    valores = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei", "Ás")

    def __init__(self, valor, naipe):
        """naipe + valor são inteiros"""
        self.valor = valor
        self.naipe = naipe 

    
    def __lt__(self, carta2):
        if self.valor < carta2.valor:
            return True
        if self.valor == carta2.valor:
            if self.naipe < carta2.naipe:
                return True
            else:
                return False
        return False
    
    
    def __gt__(self, carta2):
        if self.valor > carta2.valor:
            return True
        if self.valor == carta2.valor:
            if self.naipe > carta2.naipe:
                return True
            else:
                return False
        return False
    
    
    def __repr__(self):
        v = self.valores[self.valor] + " de " + self.naipes[self.naipe]
        return v

from random import shuffle 

class Baralho:
    def __init__(self):
        self.cartas = []
        for i in range(2, 15):
            for j in range(4):
                self.cartas.append(Card(i, j))

        shuffle(self.cartas)

    def remover_carta(self):
        if len(self.cartas) == 0:
            return
        return self.cartas.pop()
        
class Jogador:
    def __init__(self, nome):
        self.vitorias = 0
        self.cartas = None
        self.nome = nome

class Jogo:
    def __init__(self):
        nome1 = input("Nome do Jogador1: ")
        nome2 = input("Nome do Jogador2: ")
        self.baralho = Baralho()
        self.j1 = Jogador(nome1)
        self.j2 = Jogador(nome2)

    def vitorias(self, vencedor):
        v = "{} obteve uma vitória nesta rodada!\n".format(vencedor)
        print(v)

    def empate(self, nome_jgd1, carta_jgd1, nome_jgd2, carta_jgd2):
        e = "\n{} tirou {}  e  {} tirou {}".format(nome_jgd1, carta_jgd1, nome_jgd2, carta_jgd2)
        print(e)

    def jogar(self):
        cartas = self.baralho.cartas
        print("\n Começando a Guerra!")
        while len(cartas) >= 2:
            resposta = input("Aperte Q para sair. Pressione qualquer outra tecla para jogar: ")
            if resposta == 'q':
                break
            carta_jgd1 = self.baralho.remover_carta()
            carta_jgd2 = self.baralho.remover_carta()
            nome_jgd1 = self.j1.nome
            nome_jgd2 = self.j2.nome
            self.empate(nome_jgd1, carta_jgd1, nome_jgd2, carta_jgd2)
            if carta_jgd1 > carta_jgd2:
                self.j1.vitorias += 1
                self.vitorias(self.j1.nome)
            else:
                self.j2.vitorias += 1
                self.vitorias(self.j2.nome)

        vitoria = self.vencedor(self.j1, self.j2)
        print("A guerra acabou." + " {} venceu!".format(vitoria))

    def vencedor(self, j1, j2):
        if j1.vitorias > j2.vitorias:
            return j1.nome
        if j1.vitorias < j2.vitorias:
            return j2.nome
        return "Foi um empate!"


jogo = Jogo()
jogo.jogar()

        

