import random
import pygame as pg
from pygame import Color
import pygame_menu as pgm

pg.init()
pg.display.set_caption("Snake em Python")
#                               ⁡⁢⁣⁡⁢⁢⁢        𝘃𝗮𝗿𝗶𝗮𝘃𝗲𝗶𝘀 𝗱𝗲 𝗰𝗼𝗻𝗳𝗶𝗴𝘂𝗿𝗮çã𝗼⁡⁡
altura = 600
comprimento = 800

tela = pg.display.set_mode((comprimento, altura))
relogio = pg.time.Clock()

tamanho_pixel = 20

cor_fundo = 'black'
#                                       ⁡⁢⁢⁢𝘃𝗮𝗿𝗶𝗮𝘃𝗲𝗶𝘀 𝗱𝗲 𝗱𝗶𝗳𝗶𝗰𝘂𝗹𝗱𝗮𝗱𝗲⁡⁡⁡
velocidade_cobra = 10
quantidade_de_bonus = 600
valor_da_comida = 2
valor_da_comida_bonus = 5
#                               ⁡⁢⁢⁢        𝘃𝗮𝗿𝗶𝗮𝘃𝗲𝗶𝘀 𝗱𝗲 𝗲𝘀𝘁𝗶𝗹𝗼⁡
cor_cabeça_cobra = 'cornsilk1'
cor_borda_corpo_cobra = 'white'
cor_pinta_cobra = 'chartreuse4'
cor_interior_cobra = 'cornsilk4'

cor_interior_comida = 'chartreuse3'
cor_borda_comida = 'red'

cor_interior_comida_bonus = 'darkorchid1'
cor_borda_comida_bonus = 'deeppink'

def mudar_dificuldades(dificiuldade, valor):

    global velocidade_cobra
    global quantidade_de_bonus
    global valor_da_comida
    global valor_da_comida_bonus

    if valor ==  1:
        velocidade_cobra = 10
        quantidade_de_bonus = 600
        valor_da_comida = 2
        valor_da_comida_bonus = 5
        return velocidade_cobra, quantidade_de_bonus, valor_da_comida, valor_da_comida_bonus

    elif valor == 3:
        velocidade_cobra = 15
        quantidade_de_bonus = 400
        valor_da_comida = 2
        valor_da_comida_bonus = 4
        return velocidade_cobra, quantidade_de_bonus, valor_da_comida, valor_da_comida_bonus

    elif valor == 5:
        velocidade_cobra = 20
        quantidade_de_bonus = 300
        valor_da_comida = 1
        valor_da_comida_bonus = 3
        return velocidade_cobra, quantidade_de_bonus, valor_da_comida, valor_da_comida_bonus

    elif valor == 7:
        velocidade_cobra = 25
        quantidade_de_bonus = 300
        valor_da_comida = 1
        valor_da_comida_bonus = 2
        return velocidade_cobra, quantidade_de_bonus, valor_da_comida, valor_da_comida_bonus

    elif valor == 9:
        velocidade_cobra = 30
        quantidade_de_bonus = 200
        valor_da_comida = 1
        valor_da_comida_bonus = 2
        return velocidade_cobra, quantidade_de_bonus, valor_da_comida, valor_da_comida_bonus

    elif valor == 11:
        velocidade_cobra = 45
        quantidade_de_bonus = 100
        valor_da_comida = 1
        valor_da_comida_bonus = 2
        return velocidade_cobra, quantidade_de_bonus, valor_da_comida, valor_da_comida_bonus
    else:
        return 15, 300, 1, 3

def criar_comida():
    posicao_x_comida = round(random.randrange(0, comprimento - tamanho_pixel) / float(tamanho_pixel)) * float(tamanho_pixel)
    posicao_y_comida = round(random.randrange(0, altura - tamanho_pixel) / float(tamanho_pixel)) * float(tamanho_pixel)
    return posicao_x_comida, posicao_y_comida

def criar_comida_bonus():
    posicao_x_comidab = round(random.randrange(0, comprimento - tamanho_pixel) / float(tamanho_pixel)) * float(tamanho_pixel)
    posicao_y_comidab = round(random.randrange(0, altura - tamanho_pixel) / float(tamanho_pixel)) * float(tamanho_pixel)
    return posicao_x_comidab, posicao_y_comidab

def desenhar_comida(tamanho_pixel, posicao_x_comida, posicao_y_comida):
    pg.draw.rect(tela, Color('chartreuse3'), [posicao_x_comida, posicao_y_comida, tamanho_pixel, tamanho_pixel], width=10, border_radius=10)# meio da comida
    pg.draw.rect(tela, Color('red'), [posicao_x_comida, posicao_y_comida, tamanho_pixel, tamanho_pixel], width=1, border_radius=5)#           borda da comida
    
def desenhar_comida_bonus(tamanho_pixel, posicao_x_comidab, posicao_y_comidab):
    pg.draw.rect(tela, Color('darkorchid1'), [posicao_x_comidab, posicao_y_comidab, tamanho_pixel, tamanho_pixel], width=10, border_radius=10)# meio da comida
    pg.draw.rect(tela, Color('deeppink'), [posicao_x_comidab, posicao_y_comidab, tamanho_pixel, tamanho_pixel], width=1, border_radius=5)#      borda da comida

def desenhar_cobra(tamanho_pixel, pixels_da_cobra):
    for pixel in pixels_da_cobra:
        pg.draw.rect(tela, Color('chartreuse4'), [pixel[0], pixel[1], tamanho_pixel, tamanho_pixel], width=10 ,border_radius=8)#        pinta do meio da cobra
        pg.draw.rect(tela, Color('white'), [pixel[0], pixel[1], tamanho_pixel, tamanho_pixel], width=7 ,border_radius=7)#               borda da cobra
        pg.draw.rect(tela, Color('cornsilk4'), [pixel[0], pixel[1], tamanho_pixel, tamanho_pixel], width=7 ,border_radius=10)#          meio da cobra
        if pixel == pixels_da_cobra[-1]:
            pg.draw.rect(tela, Color('cornsilk1'), [pixel[0], pixel[1], tamanho_pixel, tamanho_pixel], width=2 ,border_radius=7)#       Boda da cabeça da cobra( sobre pondo a borda do corpo)
            
def fechar_pagina(eventos):
    for acao in eventos:
        if acao.type == pg.QUIT:
            return True        

def desenhar_fundo(cor_fundo):
    return tela.fill(Color(cor_fundo))

def desenhar_pontos(pontos):
    fonte = pg.font.SysFont("Helvetica", 20)
    letras = fonte.render("pontos: " + str(pontos), True, Color('cyan2'))
    tela.blit(letras, [1, 1])

def cria_lista_bonus(valor):
    bonus =[]
    x=0
    while x < valor:
        bonus.append(random.randint(5,1190))
        x += 1
    bonus.sort()
    return bonus

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def movimentos_cobra(tecla, movimento_anterior):
    if tecla == pg.K_UP or tecla == pg.K_w:
        if movimento_anterior[1] == tamanho_pixel:                                                  # nao deixa vc voltar para tras para nao colidir com vc msm voltando para tras
            pass
        else:
            velocidade_y = -tamanho_pixel
            velocidade_x = 0
            return velocidade_x, velocidade_y

    elif tecla == pg.K_DOWN or tecla == pg.K_s:
        if movimento_anterior[1] == -tamanho_pixel:                                                  # nao deixa vc voltar para tras para nao colidir com vc msm voltando para tras
            pass
        else:
            velocidade_y = tamanho_pixel
            velocidade_x = 0
            return velocidade_x, velocidade_y

    elif tecla == pg.K_RIGHT or tecla == pg.K_d:
        if movimento_anterior[0] == -tamanho_pixel:                                                  # nao deixa vc voltar para tras para nao colidir com vc msm voltando para tras
            pass
        else:
            velocidade_y = 0
            velocidade_x = tamanho_pixel
            return velocidade_x, velocidade_y

    elif tecla == pg.K_LEFT or tecla == pg.K_a:
        if movimento_anterior[0] == tamanho_pixel:                                                  # nao deixa vc voltar para tras para nao colidir com vc msm voltando para tras
            pass
        else:
            velocidade_y = 0
            velocidade_x = -tamanho_pixel
            return velocidade_x, velocidade_y
 
def iniciar_jogo ():

    fim_de_jogo = False
    posicao_x = comprimento / 2
    posicao_y = altura / 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_da_cobra = 1
    posicao_x_comida, posicao_y_comida = criar_comida()
    posicao_x_comidab, posicao_y_comidab = criar_comida_bonus()
    pixels_da_cobra = []
    bonus_sortiada = remove_repetidos(cria_lista_bonus(quantidade_de_bonus))

    while not fim_de_jogo:                                                                          # LOOP do jogo
        eventos = pg.event.get()                                                                    # captura todos os eventos do teclado

        fim_de_jogo = fechar_pagina(eventos)                                                        # fecha o programa quando vc clica no X da pagina

        desenhar_fundo(cor_fundo)                                                                   # desenha o Background, devolve a cor e o display

        desenhar_comida(tamanho_pixel, posicao_x_comida, posicao_y_comida)                          # desenha a comida na tela

        if tamanho_da_cobra in bonus_sortiada:
            desenhar_comida_bonus(tamanho_pixel, posicao_x_comidab, posicao_y_comidab)

        movimento_anterior = velocidade_x, velocidade_y                                             # manda a velocidade para a função de teclas para n deixar vc andar para tras

        for acao in eventos:                                                                        # intera sobre todos os eventos recebidos e envia os KEYDOWN para a função de movimento
            if acao.type == pg.KEYDOWN:
                if movimentos_cobra(acao.key, movimento_anterior) == None:                          # se apertar qualquer botao que n estiver configurado em movimentos_cobra() ele n faz nada
                    pass
                else:
                    velocidade_x, velocidade_y = movimentos_cobra(acao.key, movimento_anterior)     # gera o movimento da cobra
        

        posicao_y += velocidade_y                                                                   # trasforma esse movimento em posiçoes para ser desenhado na tela
        posicao_x += velocidade_x
        
        pixels_da_cobra.append([posicao_x, posicao_y])                                              # gera o movimento ILUSORIO da cobra
        if len(pixels_da_cobra) > tamanho_da_cobra:
            del pixels_da_cobra[0]     

        if posicao_x < 0 or posicao_x >= comprimento or posicao_y < 0 or posicao_y >= altura:       # Responsavel pelas coliçoes nas paredes
            fim_de_jogo = True

        for pixel in pixels_da_cobra[:-1]:                                                          # Responsavel pela colisao com sigo mesmo, tirando a cebeça
            if pixel == [posicao_x, posicao_y]:
                fim_de_jogo = True
            
        if posicao_x == posicao_x_comida and posicao_y == posicao_y_comida:                         # Responsavel por fazer a cobra crescer
            tamanho_da_cobra += valor_da_comida
            posicao_x_comida, posicao_y_comida = criar_comida()

        if posicao_x == posicao_x_comidab and posicao_y == posicao_y_comidab:                       # Responsavel por fazer a cobra crescer
            tamanho_da_cobra += valor_da_comida_bonus
            posicao_x_comidab, posicao_y_comidab = criar_comida_bonus()


        desenhar_cobra(tamanho_pixel, pixels_da_cobra)                                              # Representa a cobra na tela
        desenhar_pontos(tamanho_da_cobra - 1)                                                       # passa valores para os pontos de acordo com o tamanho da cobra

        pg.display.update()                                                                         # atualiza a tela, para desenhar os itens em movimento

        relogio.tick(velocidade_cobra)                                                              # Responsavel pela velocidade do jogo, pra n ficar rodando o loop mais rapido que a exibição

menu = pgm.Menu('Bem vindo ao Snake VML', comprimento, altura, theme=pgm.themes.THEME_SOLARIZED)
menu.add.text_input('Escreva seu Nome : ', default='')
menu.add.selector('Escolha a Dificuldade :', [('Muito Facil', 1), ('Facil', 3), ('Medio', 5), ('Dificil', 7), ('Muito Dificil', 9), ('Insano', 11)], onchange=mudar_dificuldades)
menu.add.button('Jogar', iniciar_jogo)
menu.add.button('Sair', pgm.events.EXIT)

menu.mainloop(tela)
