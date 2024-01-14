import pygame
from random import *
pygame.init() #inicializar pygame
clock = pygame.time  # velocidade dos eventos

# CRIAR UMA JANELA -----------------------------------------------------------------------------------------------------
window= pygame.display.set_mode((1000,650)) #criar a janela com  pixels de altura e comprimento iguais a imagem de fundo
pygame.display.set_caption("Snake")  #dar um nome a janela

#SUONI -----------------------------------------------------------------------------------------------------------------
sottofondo = pygame.mixer.music.load("sottofondo.wav")
pygame.mixer.music.play(-1)
suonomorte = pygame.mixer.Sound("morte.wav")
prendimoneta = pygame.mixer.Sound("coin.wav")
gameover = pygame.mixer.Sound("videogame death.wav")

# GRAFICI --------------------------------------------------------------------------------------------------------------
perso = pygame.image.load("io vivo.jpg")
persomorto = pygame.image.load("io morto.jpg")
cattivo = pygame.image.load("enemy.jpg")
hp = pygame.image.load("hp.jpg")
#soldi = [,pygame.image.load("pepita.jpg"),pygame.image.load("diamante.jpg")]
moneta = pygame.image.load("moneta.jpg")

#PROTAGONISTA ----------------------------------------------------------------------------------------------------------
class protagonista (object):
    def __init__ (self):
        self.x = 465
        self.y = 300
        self.vel = 12
        self.punti = 0
        self.vita = 5
        self.hitbox = (self.x, self.y, 64, 64)  # criar uma caixa que envolve o personagem

    def movimento (self,asse,direzione) :
        if asse:
            if direzione == 1 :
                self.x += self.vel
            else:
                self.x -= self.vel
        else :
            if direzione == 1:
                self.y -= self.vel
            else:
                self.y += self.vel
    def hit (self):
        suonomorte.play()
        window.blit(persomorto, (self.x, self.y))
        self.x = 465
        self.y = 300
        self.vita -= 1
        fonte = pygame.font.SysFont("killer", 60)
        text = fonte.render("You Died!!!", 1, (255, 0, 0))
        window.blit(text, (450, 300))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            if i == 50 and self.vita == 0:
                gameover.play()
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        if self.vita == 0 :
            window.fill((0, 0, 0))
            text2 = fonte.render("Game Over!!!", 1, (255, 0, 0))
            window.blit(text2, (390, 300))
            pygame.display.update()
            while i < 200:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()
            quit()


    def vincere (self):
        self.punti += 5

    def vitaplus (self):
        self.vita = self.vita + 1

    def draw (self):
        window.blit(perso, (self.x, self.y))
        tipolet = pygame.font.SysFont("comicsans", 30, True)
        text = tipolet.render("Vite :", 1, (0, 255, 255))
        window.blit(text, (300, 0))
        for i in range(self.vita):
           pygame.draw.rect(window, (0,255,255),(380+25*i, 5,20, 6))
        self.hitbox = (self.x, self.y, 64, 64)  # atualizar a posicao da caixa
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)  # desenhar a caixa

#ANTAGONISTA -----------------------------------------------------------------------------------------------------------
class antagonista (object):
    def __init__ (self,x,y,direzione):
        self.x = x
        self.y = y
        self.x0 = x
        self.y0 = y
        self.direzione= direzione
        self.vel = 10
        self.cambio = 0
        self.max_x = 0
        self.max_y = 0
        self.hitbox = (self.x, self.y, 64, 64)

    def movimento (self) :
        deci= randint(1,50)
        if self.cambio == 55 :
            self.cambio = 0
            deci = 1
        elif deci == 1:
            self.cambio = 0
        else:
            self.cambio += 1
        if deci == 1:
            self.direzione= randint(1,4)

        if self.direzione == 1:
            if self.x + self.vel <= 950:
                self.x += self.vel
            else :
                self.direzione = randint(2,4)
        elif self.direzione == 2:
            if self.x - self.vel >= 0:
                self.x -= self.vel
            else :
                self.direzione = randint (1,4)
        elif self.direzione == 3:
            if self.y + self.vel <= 586 :
                self.y += self.vel
            else:
                self.direzione = randint(1,4)
        elif self.direzione == 4:
            if self.y - self.vel >= 0:
                self.y -= self.vel
            else:
                self.direzione = randint(1,3)

    def hit (self):
        self.x = self.x0
        self.y = self.y0

    def draw (self):
        window.blit(cattivo, (self.x, self.y))
        self.hitbox = (self.x, self.y, 64, 64)
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

#PREZIOSI --------------------------------------------------------------------------------------------------------------
class preziosi (object):
    def __init__ (self,valore,lista):
        self.x = randint(0,957)
        self.y = randint (0,607)
        self.valore = valore
        self.disegnare = False
        self.lista = lista
        #self.probabilita = probabilita
        self.tempov = 0
        self.tempom = 0
        self.visivel = True
        self.hitbox = (self.x, self.y, 32, 32)  # atualizar a posicao da caixa

    def movimento (self) :
        if self.tempov == 100 :
            if self.tempom == 100 :
                self.x = randint(0, 957)
                self.y = randint(0, 607)
                self.tempov = 0
            else :
                self.tempom +=4
        else :
            self.tempov += 2

    def hit (self):
        prendimoneta.play()
        self.x = randint(0,975)-100
        self.x = randint(0, 607)-100
        self.visivel = False

    def draw (self) :
        window.blit(moneta, (self.x, self.y))
        self.hitbox = (self.x, self.y, 32, 32)  # atualizar a posicao da caixa
        #pygame.draw.circle(window, (255, 0, 0), (self.x+17, self.y+15), 16,2)

#HP UP -----------------------------------------------------------------------------------------------------------------
class HP_UP (object):
    def __init__(self,probabilita,lifetime):
        self.x= 2000
        self.y = 2000
        self.tempo = 5
        self.lifetime = lifetime
        self.hitbox = (self.x, self.y, 32, 32)  # atualizar a posicao da caixa
        self.visivel = False
        self.probabilita = probabilita

    def movimento (self):
        if self.visivel:
            self.x = randint(0, 975)
            self.y = randint(0, 607)
            self.visivel= False

    def hit (self):
        self.x = 2000
        self.y= 2000
        self.visivel = False

    def draw (self):
        window.blit(hp, (self.x, self.y))
        self.hitbox = (self.x, self.y, 32, 38)  # atualizar a posicao da caixa
        pygame.draw.circle(window, (255, 0, 0), (self.x+17, self.y+15), 16,2)

#ATTUALIZAZIONE DEL GIOCO ----------------------------------------------------------------------------------------------
def refresh ():
    window.fill((0, 0, 0))  # retirar o retangulo da posicao anterior preenchendo esta parte pelo fundo
    io.draw()
    if hp2.lifetime >= 0: #a vida so aparece durante um certo periudo de vida
        hp2.draw()
        hp2.lifetime -= 1
    else:
        hp2.hit()
        hp2.lifetime = 130
    for nemico in nemici:
       nemico.draw()
    if soldo.visivel:
       soldo.draw()
    else:
       soldo.visivel = True
    tipoleteras = pygame.font.SysFont("comicsans", 30, True)
    texto0 = tipoleteras.render("Pontos : %d" %io.punti, 1, (0, 255, 255))
    window.blit(texto0, (0, 0))
    pygame.display.update()

#PERSONAGGI E ITEM -----------------------------------------------------------------------------------------------------
io = protagonista()
nem1= antagonista(0,0,1)
nem2= antagonista(930,580,2)
nem3= antagonista(0,580,3)
nem4= antagonista(930,0,4)
nem5= antagonista(465,584,randint(1,4))
nemici =[nem1,nem2,nem3,nem4, nem5]
soldo = preziosi(5,0)
hp2= HP_UP(100,130)
#pepita = preziosi(10,1,50)
#diamante = preziosi(25,2,70)
#ricc= [soldo, pepita, diamante]

#EVENTI DEL GIOCO ------------------------------------------------------------------------------------------------------
run = True
while run :
    clock.delay(30)

# MORTE DEL PERSONAGGIO
    for nem in nemici :
        if io.hitbox[1] < nem.hitbox[1] + nem.hitbox[3] and io.hitbox[1] + io.hitbox[3] > nem.hitbox[1]:  # verificar que a personagem esta dentro da hitbox no eixo y
            if io.hitbox[0] + io.hitbox[2] > nem.hitbox[0] and io.hitbox[0] < nem.hitbox[0] + nem.hitbox[2]:  # verificar que a personagem esta dentro da hitbox no eixo x
                io.hit()  # executa as consequencias do perssonagem ser atingido
                nem.hit()
# VINCERE PUNTI --------------------------------------------------------------------------------------------------------
    if io.hitbox[1] < soldo.hitbox[1] + soldo.hitbox[3] and io.hitbox[1] + io.hitbox[3] > soldo.hitbox[1]:  # verificar que a personagem esta dentro da hitbox no eixo y
        if io.hitbox[0] + io.hitbox[2] > soldo.hitbox[0] and io.hitbox[0] < soldo.hitbox[0] + soldo.hitbox[2]:  # verificar que a personagem esta dentro da hitbox no eixo x
            soldo.hit()
            io.vincere()  # executa as consequencias do perssonagem atingir o dinheiro
            refresh() #para apanhar apenas uma moeda

#INTERROMPERE IL GIOCO -------------------------------------------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # parar o jogo se for pressionado o bortao sair
            run = False

#APPARIZIONE VITE EXTRA ------------------------------------------------------------------------------------------------
    if io.vita <= 2 and hp2.probabilita == randint(0,hp2.probabilita) :
        if hp2.tempo == 0 :
            hp2.visivel = True
            hp2.movimento()
            hp2.tempo = 5
        else :
            hp2.tempo -= 1
#PRENDERE VITE EXTRA ---------------------------------------------------------------------------------------------------
    if io.hitbox[1] < hp2.hitbox[1] + hp2.hitbox[3] and io.hitbox[1] + io.hitbox[3] > hp2.hitbox[1]:  # verificar que a personagem esta dentro da hitbox no eixo y
        if io.hitbox[0] + io.hitbox[2] > hp2.hitbox[0] and io.hitbox[0] < hp2.hitbox[0] + hp2.hitbox[2]:  # verificar que a personagem esta dentro da hitbox no eixo x
            hp2.hit()
            io.vitaplus()  # executa as consequencias do perssonagem atingir o dinheiro
            refresh() # atualizar para apanhar apenas uma vida

#MOVIMENTO PERSONAGGIO -------------------------------------------------------------------------------------------------
    keys = pygame.key.get_pressed()  # criar uma lista onde serao colocados os comandos
    if keys[pygame.K_LEFT] and io.x > io.vel:  # o pesrsonagem move-se naquela direcao MAS SO SE NAO SAIRA DA TELA AO FAZER ISSO
        io.movimento(True,-1)
    if keys[pygame.K_RIGHT] and io.x < 930:  # o pesrsonagem move-se naquela direcao MAS SO SE NAO SAIRA DA TELA AO FAZER ISSO
        io.movimento(True, 1)
    if keys[pygame.K_DOWN] and io.y+io.vel < 590:  # o pesrsonagem move-se naquela direcao MAS SO SE NAO SAIRA DA TELA AO FAZER ISSO
        io.movimento(False,-1)
    if keys[pygame.K_UP] and io.y > io.vel:  # o pesrsonagem move-se naquela direcao MAS SO SE NAO SAIRA DA TELA AO FAZER ISSO
        io.movimento(False, 1)

#MOVIMENTO NEMICI ------------------------------------------------------------------------------------------------------
    for nemico in nemici :
        nemico.movimento()

#APPARIZIONE PREZIOSI ---------------------------------------------------------------------------------------------------
    soldo.movimento()

    refresh()
pygame.quit() #terminar o pygame


