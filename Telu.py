import pygame
import random
#faser chinela, fazer versão dos bonecos de frente para servir como "estado inicial" e ajeitar a cozinha

pygame.init() #___________inicialização do programa

tipográfico, mouse_x, mouse_y, screen, clock, tempo= pygame.font.Font(None, 24), 0, 0, pygame.display.set_mode((800, 400)), pygame.time.Clock() , 400
t_exto, te_xto, tex_to, perso_mainha= tipográfico.render(f"Deseja iniciar com qual personagem? (< ou >)", True, (0,0,0)), tipográfico.render(f"Com qual nível de dificuldade deseja jogar? (v ou ^)", True, (0,0,0)), tipográfico.render(f"Fácil                   Difícil", True, (0,0,0)), tipográfico.render(f"Mainha:", True, (0,0,0))
p_uxada1, p_uxada2, pu_xada, pux_ada, perso_filho, puxa_da = tipográfico.render(f"Ariel, o que será de você quando eu não estiver", True, (0,0,0)), tipográfico.render(f"mais na Terra para achar os seus pertences?", True, (0,0,0)), tipográfico.render(f"Vá novamente procurar essa geringonça, e olhe lá....", True, (0,0,0)), tipográfico.render(f"se eu for lá e achar, já sabe. Você tem o tempo de {tempo}", True, (0,0,0)), tipográfico.render(f"Ariel:", True, (0,0,0)), tipográfico.render(f"Relaxa, coroa, eu vou achar sim.", True, (0,0,0))
chao , fora, quintal, relogio= pygame.Surface([800, 200]), pygame.Surface([100, 200]), pygame.Surface([200, 100]), pygame.Surface([300, 100])

#_____________________________________Imagens, -rects- e conversões
parada_img, parado_img, inaAndando_img, inoAndando_img = pygame.image.load('imagens/meninaParada.png').convert_alpha(), pygame.image.load('imagens/meninoParado.png').convert_alpha(), pygame.image.load('imagens/meninaAndando.png').convert_alpha(), pygame.image.load('imagens/meninoAndando.png').convert_alpha()
parada_img, parado_img, inaAndando_img, inoAndando_img = pygame.transform.scale(parada_img, (150,200)), pygame.transform.scale(parado_img, (120,190)), pygame.transform.scale(inaAndando_img, (200,200)), pygame.transform.scale(inoAndando_img, (160, 160))
sofa_img, planta_img, gatoMimindo_img, portaFechada_img, candelabro_img, gatoAtento_img, portAberta_img, mainha_img = pygame.image.load('imagens/sofá.png').convert_alpha(),pygame.image.load('imagens/planta.png').convert_alpha(),pygame.image.load('imagens/gatoDormindo.png').convert_alpha(), pygame.image.load('imagens/portaFechada.png').convert_alpha(), pygame.image.load('imagens/candelabro.png').convert_alpha(), pygame.image.load('imagens/gatoAtento.png').convert_alpha(), pygame.image.load('imagens/portaAberta.png').convert_alpha(), pygame.image.load('imagens/mainha.png').convert_alpha()
sofa_img, planta_img, gatoMimindo_img, portaFechada_img, candelabro_img, gatoAtento_img, portAberta_img, mainha_img = pygame.transform.scale(sofa_img, (400, 200)), pygame.transform.scale(planta_img, (150, 200)), pygame.transform.scale(gatoMimindo_img, (90, 50)), pygame.transform.scale(portaFechada_img, (300, 300)), pygame.transform.scale(candelabro_img, (180, 150)), pygame.transform.scale(gatoAtento_img, (180, 150)), pygame.transform.scale(portAberta_img, (180,150)), pygame.transform.scale(mainha_img, (120,140))
pia_img, geladeiraFechada_img, geladeiraAberta_img, fogaoFechado_img, fogaoAberto_img, janela_img, cortinaAberta_img, cortinaFechada_img = pygame.image.load('imagens/pia.png').convert_alpha(), pygame.image.load('imagens/geladeiraFechada.png').convert_alpha(), pygame.image.load('imagens/geladeiraAberta.png').convert_alpha(), pygame.image.load('imagens/fogãoFechado.png').convert_alpha(), pygame.image.load('imagens/fogãoAberto.png').convert_alpha(), pygame.image.load('imagens/janela.png').convert_alpha(), pygame.image.load('imagens/cortinaAberta.png').convert_alpha(), pygame.image.load('imagens/cortinaFechada.png').convert_alpha()
pia_img, geladeiraFechada_img, geladeiraAberta_img, fogaoFechado_img, fogaoAberto_img, janela_img, cortinaAberta_img, cortinaFechada_img = pygame.transform.scale(pia_img, (280,250)), pygame.transform.scale(geladeiraFechada_img, (180,350)), pygame.transform.scale(geladeiraAberta_img, (180,350)), pygame.transform.scale(fogaoFechado_img, (280,250)), pygame.transform.scale(fogaoAberto_img, (280,250)), pygame.transform.scale(janela_img, (180,350)), pygame.transform.scale(cortinaAberta_img, (180,350)), pygame.transform.scale(cortinaFechada_img, (180,150))
chave_img, roupaAberta_img, roupaFechada_img, celular_img, ovos_img, guardaChuva_img = pygame.image.load('imagens/chave.png').convert_alpha(), pygame.image.load('imagens/camisaAberta.png').convert_alpha(), pygame.image.load('imagens/camisaDobrada.png').convert_alpha(), pygame.image.load('imagens/celular.png').convert_alpha(),pygame.image.load('imagens/ovos.png').convert_alpha(), pygame.image.load('imagens/guardaChuva.png').convert_alpha()
chave_img, roupaAberta_img, roupaFechada_img, celular_img, ovos_img, guardaChuva_img = pygame.transform.scale(chave_img,(50,25)), pygame.transform.scale(roupaAberta_img, (125,180)), pygame.transform.scale(roupaFechada_img,(125,180)), pygame.transform.scale(celular_img, (70,100)), pygame.transform.scale(ovos_img, (150,80)), pygame.transform.scale(guardaChuva_img, (60,150))
#________________________________________Estados iniciais
mainha_img = pygame.transform.flip(mainha_img, True, False)
gato_img = gatoMimindo_img
porta_img = portaFechada_img
geladeira_img = geladeiraFechada_img
cortina_img = cortinaAberta_img
fogao_img = fogaoFechado_img
roupa_img = roupaFechada_img
#_______________________________________Pintura
chao.fill((240,230,140)) 
fora.fill((255,255,255))
quintal.fill((255,255,255))
def sala():#___________________________________________Ambientes
    print(f"imagem: {perdido}, local:{local}, fase:{fase},")
    b = 0
    if estado > 1:
        rolado = pygame.transform.flip(perdido, False, True)
        if local <= 3 : #_________________________local easy
            if local == 1:#___sala - atrás da planta
                screen.blit(perdido, (590,120))
            elif local == 3:#_sala - encostado no sofá
                screen.blit(perdido, (260, 140))
        elif local >= 4 :#_________________________local hard
            if local == 4:#___sala - embaixo do gato
                screen.blit(rolado, (360,200))
                b = 24
    screen.blit(sofa_img,(270,130))
    screen.blit(planta_img,(600, 100))
    screen.blit(gato_img,(360, 198 - b))
    screen.blit(porta_img,(25, 15))
    screen.blit(candelabro_img,(320, -35))
def movimentoDeMainha(b):
    b += 1
    if b % 3 == 0:#_____________Movimento de mainha
        screen.blit(mainha_img, (200, 160))
    else:
        screen.blit(mainha_img, (200, 180))
    return b
def movimentoDePersonagem(a):
    a += 1
    if a % 3 == 0:#_____________Movimento de mainha
        screen.blit(personagem_parado, (350,131))
    else:
        screen.blit(personagem_parado, (350,151))
    return a
def andarilho(veloci, ambiene, a):
    if a == 1:
        veloci = 350
    sentido, potencia = 13, 0
    loukura= pygame.key.get_pressed()
    if loukura[pygame.K_LEFT] and not loukura[pygame.K_DOWN]:#se andar normal para esquerda
        veloci = veloci - 10
        sentido = 13
        potencia = 0
    elif loukura[pygame.K_RIGHT] and not loukura[pygame.K_DOWN]:#se andar normal para direita
        veloci = veloci + 10
        sentido = 22
        potencia = 0
    if loukura[pygame.K_LEFT] and loukura[pygame.K_DOWN]:#se correr para esquerda
        veloci = veloci - 20
        sentido = 13
        potencia = 2
    elif loukura[pygame.K_RIGHT] and loukura[pygame.K_DOWN]: #se correr para esquerda
        veloci = veloci + 20
        sentido = 22
        potencia = 2
    if ambiene == 0 and veloci <= -45: #não passa da sala
        veloci= -40
    elif ambiene == 1 and veloci >= 680:#não passa da cozinha
        veloci = 680
    if ambiene == 0 and veloci >= 750:#passa para cozinha
        ambiene = 1
        veloci = -50
    elif ambiene == 1 and veloci <= -90:#passa para a sala
        ambiene = 0
        veloci = 720
    #_______________________________Prints personagem na screen
    if potencia == 0:#andando
        if sentido == 13:
            screen.blit(personagem_parado, (veloci, 151))
        elif sentido == 22:
            screen.blit(pygame.transform.flip(personagem_parado, True, False), (veloci, 151))
    elif potencia == 2:#correndo
        if sentido == 13:
            if genero == 0:
                screen.blit(personagem_andando, (veloci, 171))
            else:
                screen.blit(personagem_andando, (veloci, 151))
        elif sentido == 22:
            if genero == 0:
                screen.blit(pygame.transform.flip(personagem_andando, True, False), (veloci, 171))
            else:
                screen.blit(pygame.transform.flip(personagem_andando, True, False), (veloci, 151))
    a += 1
    return veloci, ambiene, a

def cozinha():
    '''if local <= 3 : #___________local easy
        if local == 2:#_cozinha - Dentro da pia
            screen.blit(perdido, ())
    elif local >= 4 :#___________local hard
        if local == 5:#_cozinha - dentro da geladeira
            screen.blit(perdido, ())
        elif local == 6:#_cozinha - dentro do fogão
            screen.blit(perdido, ())'''
    screen.blit(geladeira_img,(150,200))
    screen.blit(pia_img,(150,200)) 
    screen.blit(janela_img,(150,200))
    screen.blit(cortina_img,(150,200))
    screen.blit(fogao_img,(150,200))

'''Momento= passagem do tempo em uma cena | velocidade= movimento do personagem na tela  | tempo= contagem regressiva para o estresse total de Mainha
estado: big-bang = 0, prelúdio = 1, procura = 2, fim bom = 3, fim triste = -3 #___________Variáveis
fase: fácil = 1, difícil = 3      |     sentido: direita = 22, esquerda = 13
ambiente: sala= 0, cozinha = 1    |     genero: menino = 0, menina = 1'''
estado, fase, ambiente, genero, momento, b, a, velocidade = 0, 0, 0, 5, 0, 0, 0, 350
#local: 1= atrás da planta, 2= Dentro da pia, 3= Emcima da planta | 4= embaixo do gato, 5= dentro da geladeira, 6= dentro do fogão
lugar = [1,2,3,4,5,6]
#objetos: 0= guarda-chuva, 1= roupa do if, 2= celular, 3= chave
objetos = [guardaChuva_img, roupa_img, celular_img, chave_img]

while True:
    for event in pygame.event.get():#_____________________Leitura de eventos
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            momento += 1
    screen.fill((216,191,216)) #__________Repintando a tela 


    if estado == 0: #____________________________________________Tela inicial
        screen.blit(t_exto, (208,120))
        screen.blit(parada_img, (190,150))
        screen.blit(parado_img, (450,153))
        escolha = pygame.key.get_pressed()
        if escolha[pygame.K_LEFT]:
            genero,estado = 1, -1
        elif escolha[pygame.K_RIGHT]:#__________Escolha do personagem
            genero, estado = 0, -1
        if genero == 0: #menino
            personagem_parado, personagem_andando = parado_img, inoAndando_img
        elif genero == 1: #menina
            personagem_parado, personagem_andando = parada_img, inaAndando_img
    elif estado == -1:
        screen.blit(te_xto, (200,120))#_________Escolha da dificuldade
        screen.blit(tex_to, (320,190))
        escolha = pygame.key.get_pressed()
        if escolha[pygame.K_UP]:#_____________Difícil
            fase, estado, local, perdido = 3, 1, lugar[random.randint(0,5)], objetos[random.randint(0,3)]
        elif escolha[pygame.K_DOWN]:#___________fácil
            fase, estado, local, perdido = 1, 1, lugar[random.randint(0,2)], guardaChuva_img
    #____________________________________________________________Jogo
    else:
        screen.blit(chao, (0,250))
        if estado == 1:#__________________Puxada de orelha
            sala()
            if momento == 1:#_______________________Trocas de falas
                b = movimentoDeMainha(b)
                screen.blit(personagem_parado, (350,151))
                screen.blit(perso_mainha, (50, 320))
                screen.blit(pu_xada,(150,320))
            elif momento == 2:
                b = movimentoDeMainha(b)
                screen.blit(personagem_parado, (350,151))
                screen.blit(perso_mainha, (50, 320))
                screen.blit(pux_ada, (150,320))
            elif momento == 0:
                b = movimentoDeMainha(b)
                screen.blit(personagem_parado, (350,151))
                screen.blit(perso_mainha, (50, 320))
                screen.blit(p_uxada1,(150,320))
                screen.blit(p_uxada2, (160,340))
            elif momento == 3: #_______________Resposta
                screen.blit(mainha_img, (200,180))
                screen.blit(perso_filho, (50, 320))
                a = movimentoDePersonagem(a)
                screen.blit(puxa_da,(150,320))
            else:#__________________Troca de estado
                estado = 2
                momento, a, b = 0, 0 , 0
        if fase == 1 and estado > 1:#______Separação de fase
            if estado == 2:
                if ambiente == 0:
                    sala()
                if ambiente == 1:
                    cozinha()
                velocidade, ambiente, a = andarilho(velocidade, ambiente, a)#função do movimento controlado
                #_____________________________Toque dos objetos

            elif estado == 3:
                print("Parabens")
            elif estado == -3:
                print("Castigo")

        if fase == 3 and estado > 1:#______Separação de fase
            if estado == 2:
                print("investigar")
            elif estado == 3:
                print("Parabens")
            elif estado == -3:
                print("Castigo")
    
    pygame.display.flip()
    clock.tick(15)  # taxa de quadros por segundo (FPS)

#             if fase == 1:
pygame.quit()