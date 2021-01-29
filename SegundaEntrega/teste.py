from random import randrange
class lutador:
    vitorias = 0
    derrotas = 0
    def __init__ (self):
        nome = input('escolha o nome do jogador')
        idade = input('escolha a idade do jogador')
        peso = input('escolha o peso do jogador')
        forca= input('escolha a forca do jogador')
        faixa = input('escolha uma faixa')
        arte_marcial = input('escolha uma arte marcial')


lutador_1 = lutador()
lutador_2 = lutador()

lutadores = []
def cadastro(): 
    jogador = lutador()
    lutadores.append(jogador)

def ver_lutadores():
    for i in range (len(lutadores)):
        print(lutadores[i].nome)

#Regras
def ganhar_luta(lutador_1, lutador_2):
    P1 = lutador_1.peso
    P2 = lutador_2.peso
    if P1 > P2:
        print(lutador_2.nome + 'perdeu!')
    else:
        print(lutador_1.nome +'perdeu!')

def confronto(lutador_1, lutador_2):
    A1 = lutador_1.arte_marcial
    A2 = lutador_2.arte_marcial
    if A1 != A2:
        print('não foi possível iniciar partida')
    else:
        print('iniciar partida')

class aleatorio(self):
    nomes = [] 
    faixas = []
    artes_marciais = []
    def __init__(self):
        self.nome = nomes[randrange(0, len(nomes)-1)]+str(randrange(0,1000))
        #o nome sera na forma Fernanda120 para não haver repetição
        self.idade = randrange(18, 50)
        self.peso = randrange(50, 100)
        self.forca = randrange(0, 300)
        self.faixa = faixas[randrange(0, len(faixas)-1)]
        self.arte_marcial = artes_marciais[randrange(0, len(artes_marciais)-1)]


class torneio:
    def __init__ (self):
        nome_torneio = input('escolha o nome do torneio')
        modalidade_arte = input('escolha uma modalidade de arte marcial para competir')
        faixas = input('escolha as faixas dos competidores')
        pesos = input('escolha os pesos dos competidores')
        inscritos = []

#criando torneio
torneios =[]
def criar_torneio():
    c = torneio()
    torneios.append(c)

def inscreve_lutador(lutador):
    
    torneios.append(f)
    

def torneio_existente():
    for i in range(len(torneios)):
        print(torneios[i].nome_torneio)


if 




