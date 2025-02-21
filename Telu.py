import pygame
import random
#faser chinela, fazer versão dos bonecos de frente para servir como "estado inicial" e ajeitar a cozinha

pygame.init() #___________inicialização do programa

tipográfico, mouse_x, mouse_y, screen, clock = pygame.font.Font(None, 24), 0, 0, pygame.display.set_mode((800, 400)), pygame.time.Clock()
t_utorial, tu_torial, tut_orial, tuto_rial, tutor_ial, tutori_al, tutoria_l, tutorial_ = tipográfico.render(f"mostra",True, (28,28,28)), tipográfico.render(f"ou",True, (28,28,28)) , tipográfico.render(f"Faz correr",True, (28,28,28)), tipográfico.render(f"Clique básico do mouse",True, (28,28,28)), tipográfico.render(f"Movimenta o personagem",True, (28,28,28)), tipográfico.render(f"Abre a geladeira e o fogão",True, (28,28,28)), tipográfico.render(f"Fecha a geladeira e o fogão",True, (28,28,28)), tipográfico.render(f"Pegar o objeto perdido",True, (28,28,28))
p_rogram,pr_ogram, pro_gram, prog_ram, progr_am, perso_mainha = tipográfico.render(f"Iniciar",True, (28,28,28)), tipográfico.render(f"Customizar", True, (28,28,28)), tipográfico.render(f"Tutorial", True, (28,28,28)), tipográfico.render("Confirmar", True, (28,28,28)), tipográfico.render("Sair", True, (28,28,28)), tipográfico.render(f"Mainha:", True, (28,28,28))
f_rase, fr_ase, fra_se = tipográfico.render(f"Eu achei, mainha!", True, (28,28,28)), tipográfico.render(f"Ainda bem que não demorou, Filho, obrigada", True, (28,28,28)), tipográfico.render(f"Ainda bem que não demorou, Filha, obrigada", True, (28,28,28))
s_ala, sa_la, sal_a, sala_ = tipográfico.render(f"Já esqueci o que eu deveria procurar", True, (28,28,28)), tipográfico.render(f"Gatinho fofo", True, (28,28,28)), tipográfico.render(f"Aquela planta é mais guerreira que cacto", True, (28,28,28)), tipográfico.render(f"Devo me apressar", True, (28,28,28)),
c_ozinha, co_zinha, coz_inha, cozi_nha = tipográfico.render(f"Aqui é ventilado", True, (28,28,28)), tipográfico.render(f"Será que está na geladeira?", True, (28,28,28)), tipográfico.render(f"Será que está no fogão?", True, (28,28,28)), tipográfico.render(f"Mainha está me esperando", True, (28,28,28))
p_uxada1, p_uxada2, pu_xada, pux_ada, perso_filho, puxa_da = tipográfico.render(f"Ariel, o que será de você quando eu não estiver", True, (28,28,28)), tipográfico.render(f"Mais na Terra para achar os seus pertences?", True, (28,28,28)), tipográfico.render(f"Vá novamente procurar essa geringonça, e olhe lá....", True, (28,28,28)), tipográfico.render(f"Se eu for lá e achar, já sabe. Vou te dar alguns segundos.", True, (28,28,28)), tipográfico.render(f"Ariel:", True, (28,28,28)), tipográfico.render(f"Relaxa, coroa, eu vou achar sim.", True, (28,28,28))
chao, fora, quintal= pygame.Surface([800, 200]), pygame.Surface([230, 100]), pygame.Surface([120, 193])
fala_sala, fala_cozinha = [s_ala, sa_la, sal_a, sala_], [c_ozinha, co_zinha, coz_inha, cozi_nha]
#_____________________________________Imagens e conversões
cora1, cora2, cora3, cora4, cora5, image0, image1, image2, image3 = pygame.image.load('imagens/cora1.png').convert_alpha(), pygame.image.load('imagens/cora2.png').convert_alpha(), pygame.image.load('imagens/cora3.png').convert_alpha(), pygame.image.load('imagens/cora4.png').convert_alpha(), pygame.image.load('imagens/cora5.png').convert_alpha(), pygame.image.load('imagens/image1.png').convert(), pygame.image.load('imagens/image2.png').convert(), pygame.image.load('imagens/image3.png').convert(), pygame.image.load('imagens/image4.png').convert() 
cora1, cora2, cora3, cora4, cora5, image0, image1, image2, image3 = pygame.transform.scale(cora1, (300,300)), pygame.transform.scale(cora2, (300,300)), pygame.transform.scale(cora3, (300,300)), pygame.transform.scale(cora4, (300,300)), pygame.transform.scale(cora5, (300,300)), pygame.transform.scale(image0, (300,150)), pygame.transform.scale(image1, (300,200)), pygame.transform.scale(image2, (300,150)), pygame.transform.scale(image3, (300,200))
moldura, titulo, controle, osso, mamao = pygame.image.load('imagens/moldura.png').convert_alpha(), pygame.image.load('imagens/Titulo init.png').convert_alpha(), pygame.image.load('imagens/controle.png').convert_alpha(), pygame.image.load('imagens/osso.png').convert_alpha(), pygame.image.load('imagens/mamaoComAcucar.png').convert_alpha()
moldura, titulo, controle, osso, mamao = pygame.transform.scale(moldura, (300,300)), pygame.transform.scale(titulo, (350,250)), pygame.transform.scale(controle, (100,100)), pygame.transform.scale(osso, (200,200)), pygame.transform.scale(mamao, (200,200))
parada_img, parado_img, inaAndando_img, inoAndando_img, menina_img, menino_img, botao, ponteiro, ponteir, ponteirozin, ponteirinho = pygame.image.load('imagens/meninaParada.png').convert_alpha(), pygame.image.load('imagens/meninoParado.png').convert_alpha(), pygame.image.load('imagens/meninaAndando.png').convert_alpha(), pygame.image.load('imagens/meninoAndando.png').convert_alpha(), pygame.image.load('imagens/menina dorço.png').convert_alpha(), pygame.image.load('imagens/menino dorço.png').convert_alpha(), pygame.image.load('imagens/caixa.png').convert_alpha(), pygame.image.load('imagens/setinha.png').convert_alpha(), pygame.image.load('imagens/lindona.png').convert_alpha(), pygame.image.load('imagens/setinha.png').convert_alpha(), pygame.image.load('imagens/lindona.png').convert_alpha()
parada_img, parado_img, inaAndando_img, inoAndando_img, menina_img, menino_img, botao, ponteiro, ponteir, ponteirozin, ponteirinho = pygame.transform.scale(parada_img, (150,200)), pygame.transform.scale(parado_img, (120,190)), pygame.transform.scale(inaAndando_img, (200,200)), pygame.transform.scale(inoAndando_img, (160, 160)), pygame.transform.scale(menina_img,(200,200)), pygame.transform.scale(menino_img, (200,200)), pygame.transform.scale(botao, (350,200)), pygame.transform.scale(ponteiro,(100,100)), pygame.transform.scale(ponteir,(100,100)), pygame.transform.scale(ponteirozin, (90,90)), pygame.transform.scale(ponteirinho,(90,90))
sofa_img, planta_img, gatoMimindo_img, portaFechada_img, candelabro_img, gatoAtento_img, portAberta_img, mainha_img = pygame.image.load('imagens/sofá.png').convert_alpha(),pygame.image.load('imagens/planta.png').convert_alpha(),pygame.image.load('imagens/gatoDormindo.png').convert_alpha(), pygame.image.load('imagens/portaFechada.png').convert_alpha(), pygame.image.load('imagens/candelabro.png').convert_alpha(), pygame.image.load('imagens/gatoAtento.png').convert_alpha(), pygame.image.load('imagens/portaAberta.png').convert_alpha(), pygame.image.load('imagens/mainha.png').convert_alpha()
sofa_img, planta_img, gatoMimindo_img, portaFechada_img, candelabro_img, gatoAtento_img, portAberta_img, mainha_img, miniEu = pygame.transform.scale(sofa_img, (400, 200)), pygame.transform.scale(planta_img, (150, 200)), pygame.transform.scale(gatoMimindo_img, (90, 50)), pygame.transform.scale(portaFechada_img, (300, 300)), pygame.transform.scale(candelabro_img, (180, 150)), pygame.transform.scale(gatoAtento_img, (87, 47)), pygame.transform.scale(portAberta_img, (300,330)), pygame.transform.scale(mainha_img, (120,140)), pygame.transform.scale(parada_img, (75, 100))
pia_img, geladeiraFechada_img, geladeiraAberta_img, fogaoFechado_img, fogaoAberto_img, janela_img, cortinaAberta_img, cortinaFechada_img = pygame.image.load('imagens/pia.png').convert_alpha(), pygame.image.load('imagens/geladeiraFechada.png').convert_alpha(), pygame.image.load('imagens/geladeiraAberta.png').convert_alpha(), pygame.image.load('imagens/fogãoFechado.png').convert_alpha(), pygame.image.load('imagens/fogãoAberto.png').convert_alpha(), pygame.image.load('imagens/janela.png').convert_alpha(), pygame.image.load('imagens/cortinaAberta.png').convert_alpha(), pygame.image.load('imagens/cortinaFechada.png').convert_alpha()
pia_img, geladeiraFechada_img, geladeiraAberta_img, fogaoFechado_img, fogaoAberto_img, janela_img, cortinaAberta_img, cortinaFechada_img = pygame.transform.scale(pia_img, (280,250)), pygame.transform.scale(geladeiraFechada_img, (280,310)), pygame.transform.scale(geladeiraAberta_img, (300,280)), pygame.transform.scale(fogaoFechado_img, (240,200)), pygame.transform.scale(fogaoAberto_img, (250,200)), pygame.transform.scale(janela_img, (350,180)), pygame.transform.scale(cortinaAberta_img, (380,180)), pygame.transform.scale(cortinaFechada_img, (350,180))
chave_img, roupaAberta_img, roupaFechada_img, celular_img, ovos_img, guardaChuva_img = pygame.image.load('imagens/chave.png').convert_alpha(), pygame.image.load('imagens/camisaAberta.png').convert_alpha(), pygame.image.load('imagens/camisaDobrada.png').convert_alpha(), pygame.image.load('imagens/celular.png').convert_alpha(),pygame.image.load('imagens/ovos.png').convert_alpha(), pygame.image.load('imagens/guardaChuva.png').convert_alpha()
chave_img, roupaAberta_img, roupaFechada_img, celular_img, ovos_img, guardaChuva_img = pygame.transform.scale(chave_img,(25,25)), pygame.transform.scale(roupaAberta_img, (125,180)), pygame.transform.scale(roupaFechada_img,(160,180)), pygame.transform.scale(celular_img, (100,90)), pygame.transform.scale(ovos_img, (90,80)), pygame.transform.scale(guardaChuva_img, (60,150))
exclamacao_img, interrogacao_img, chinelo_img = pygame.image.load('imagens/exclamação.png.png').convert_alpha(), pygame.image.load('imagens/interrogação.png').convert_alpha(), pygame.image.load('imagens/chinela.png.png').convert_alpha()
exclamacao_img, interrogacao_img, chinelo_img = pygame.transform.scale(exclamacao_img, (100,100)), pygame.transform.scale(interrogacao_img, (100,100)), pygame.transform.scale(chinelo_img, (200,200))
#________________________________________Estados iniciais
cima = ponteir
baixo = pygame.transform.flip(ponteir, False, True)
direita = ponteiro
esquerda = pygame.transform.flip(ponteiro, True, False)

mainha_img = pygame.transform.flip(mainha_img, True, False)
gato_img = gatoMimindo_img
geladeira_img = geladeiraFechada_img
fogao_img = fogaoFechado_img
roupa_img = roupaFechada_img
personagem_andando, personagem_parado = inoAndando_img, parado_img
seletor_cozinha, seletor_sala = fala_cozinha[random.randint(0,3)], fala_sala[random.randint(0,3)]
#_______________________________________Pintura
chao.fill((240,230,140)) 
quintal.fill((255,255,255))
def cozinha(estado,mentos, select, geladeira_img, fogao_img):
    # print(local)
    biloca = pygame.key.get_pressed()
    if velocidade >= 490 and velocidade <= 680: #_cozinha - abrir/fechar geladeira
        if geladeira_img == geladeiraFechada_img:
            if biloca[pygame.K_LEFT] and biloca[pygame.K_RIGHT]:
                geladeira_img = geladeiraAberta_img
        else:
            if biloca[pygame.K_DOWN] and not biloca[pygame.K_UP] and not biloca[pygame.K_LEFT] and not biloca[pygame.K_RIGHT]:
                geladeira_img = geladeiraFechada_img
    elif velocidade >= -40 and velocidade <= 180: #_cozinha - abrir/fechar fogão
        if fogao_img == fogaoFechado_img:
            if biloca[pygame.K_LEFT] and biloca[pygame.K_RIGHT]:
                fogao_img = fogaoAberto_img
        else:
            if biloca[pygame.K_DOWN] and not biloca[pygame.K_UP] and not biloca[pygame.K_LEFT] and not biloca[pygame.K_RIGHT]:
                fogao_img = fogaoFechado_img
    if geladeira_img == geladeiraAberta_img: #___________Se a geladeira estiver aberta, posicionar...
        screen.blit(geladeira_img, (520,65))
    else:
        screen.blit(geladeira_img, (500,35))
    if fogao_img == fogaoAberto_img:#____________________Se o fogão estiver aberto, posicionar...
        screen.blit(fogao_img,(30,115))
    else:
        screen.blit(fogao_img,(40,110))
    screen.blit(pia_img,(270,150))
    screen.blit(fora,(300,80))
    screen.blit(janela_img,(250,60))
    if fase == 1:#_____________Mudança de cortina, fundo vermelho/ou n devido a fase
        screen.blit(cortinaAberta_img,(243,30))
        fora.fill((255,255,255))
    else:
        screen.blit(cortinaFechada_img,(230,45))
        fora.fill((255,50,50))
    if local == 2:#_cozinha - Dentro da pia     ________________local easy
        if perdido == chave_img:
            screen.blit(perdido, (300,350))
        elif perdido == celular_img:
            screen.blit(perdido, (340,200))
        else:
            screen.blit(perdido, (270,150))
        if velocidade >= 190 and velocidade <= 460:
            if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                screen.blit(exclamacao_img, (velocidade+10, 60))
            elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]: 
                estado = 3
        elif velocidade >= 490 and velocidade <= 680:#___terceira área
                if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                    screen.blit(interrogacao_img, (velocidade+10, 60))
                elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]:
                        mentos = 1
        elif velocidade >= -40 and velocidade <= 180:#___primeira área
                if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                    screen.blit(interrogacao_img, (velocidade+10, 60))
                elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]:
                        mentos = 1
    elif local == 5 or local == 6 :#___________local hard
        if local == 5:#_cozinha - dentro da geladeira
            if geladeira_img == geladeiraAberta_img:
                if perdido == celular_img:
                    screen.blit(perdido, (580,180))
                elif perdido == chave_img:
                    screen.blit(perdido, (620,190))
                elif perdido == roupaFechada_img:
                    screen.blit(perdido, (560,130))
                else:
                    screen.blit(perdido, (580,130))
                if velocidade >= 490 and velocidade <= 680:
                    if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                        screen.blit(exclamacao_img, (velocidade+10, 60))
                    elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]: 
                        estado = 3
                elif velocidade >= 190 and velocidade <= 460:#___segunda área
                    if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                        screen.blit(interrogacao_img, (velocidade+10, 60))
                    elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]:
                        mentos = 1
                elif velocidade >= -40 and velocidade <= 180:#___primeira área
                    if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                        screen.blit(interrogacao_img, (velocidade+10, 60))
                    elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]:
                        mentos = 1
        elif local == 6:#_cozinha - dentro do fogão
            if fogao_img == fogaoAberto_img:
                if perdido == celular_img:
                    screen.blit(perdido, (100,200))
                elif perdido == chave_img:
                    screen.blit(perdido, (130,220))
                else:
                    screen.blit(perdido, (60,180))
                if velocidade >= -40 and velocidade <= 180:
                    if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                        screen.blit(exclamacao_img, (velocidade+10, 60))
                    elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]: 
                        estado = 3
                elif velocidade >= 190 and velocidade <= 460:#___segunda área
                    if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                        screen.blit(interrogacao_img, (velocidade+10, 60))
                    elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]:
                        mentos = 1
                elif velocidade >= 490 and velocidade <= 680:#___terceira área
                    if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                        screen.blit(interrogacao_img, (velocidade+10, 60))
                    elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]:
                        mentos = 1
    else:#___________________quando o objeto estiver em outro ambiente
        if velocidade >= -40 and velocidade <= 180:#___primeira área
            if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                screen.blit(interrogacao_img, (velocidade+10, 60))
            elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]:
                mentos = 1
        elif velocidade >= 190 and velocidade <= 460:#___segunda área
            if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                screen.blit(interrogacao_img, (velocidade+10, 60))
            elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]:
                mentos = 1
        elif velocidade >= 490 and velocidade <= 680:#___terceira área
            if biloca[pygame.K_UP] and not biloca[pygame.K_DOWN]:
                screen.blit(interrogacao_img, (velocidade+10, 60))
            elif biloca[pygame.K_UP] and biloca[pygame.K_DOWN]:
                    mentos = 1
    if geladeira_img == geladeiraAberta_img:
        screen.blit(ovos_img, (677,165))
    if biloca[pygame.K_RIGHT] or biloca[pygame.K_LEFT]:
        if not biloca[pygame.K_UP] or not biloca[pygame.K_DOWN]:
            mentos = 0
            select = fala_cozinha[random.randint(0,3)]
    if mentos == 1:
        screen.blit(perso_filho, (50, 320))
        screen.blit(select, (150,320))
    return estado, mentos, select, geladeira_img, fogao_img
def sala(estado, elementos, seletiva, perdido, gato_img):#___________________________________________Ambientes
    b, joca = 0, pygame.key.get_pressed()
    # print(local)
    if joca[pygame.K_DOWN] and joca[pygame.K_LEFT]:#_____Movimento do gato
        if velocidade >= 100 and velocidade <= 500:
            gato_img = gatoAtento_img
    elif joca[pygame.K_DOWN] and joca[pygame.K_RIGHT]:
        if velocidade >= 100 and velocidade <= 500:
            gato_img = gatoAtento_img
    else:
        if velocidade >= 100 and velocidade <= 500:
            gato_img = gatoMimindo_img
    if fase != 1 and local == 4:
        if perdido == guardaChuva_img:#____________troca de objetos
            perdido = chave_img
        if perdido == celular_img: 
            perdido == roupaFechada_img
    if local == 1 and estado == 2:#___sala - atrás da planta _______reposição de itens específicos
        if perdido == chave_img:
            screen.blit(perdido, (670,120))
        elif perdido == celular_img:
            screen.blit(perdido, (600,150))
        elif perdido == roupa_img:
            screen.blit(perdido, (590,140))
        else:
            screen.blit(perdido, (590,120))
    elif local == 3 and estado == 2:#_sala - encostado no sofá
        if perdido == roupaFechada_img:
            screen.blit(perdido, (253, 100))
        elif perdido == chave_img:
            screen.blit(perdido, (250, 235))
        elif perdido == celular_img:
            screen.blit(perdido, (280, 140))
        else:
            screen.blit(perdido, (260, 140))
    screen.blit(quintal,(97, 60))
    screen.blit(sofa_img,(270,130))
    screen.blit(planta_img,(600, 100))
    screen.blit(candelabro_img,(320, -35))
    if fase == 3:#__________________Mudança de porta devido a fase
        screen.blit(portaFechada_img,(25, 15))
    else:
        screen.blit(portAberta_img,(95, 15))
    if estado != 1 and estado != 3:
        if local == 1 or local ==3 : #_________________________local easy
            if local == 1:#___sala - atrás da planta
                if velocidade >= 510 and velocidade <= 720:
                    if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                        screen.blit(exclamacao_img, (velocidade+10, 60))
                    elif joca[pygame.K_UP] and joca[pygame.K_DOWN]: 
                        estado = 3
                elif velocidade >= 270 and velocidade <= 420:#___segunda área
                    if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                        screen.blit(interrogacao_img, (velocidade+10, 60))
                    elif joca[pygame.K_UP] and joca[pygame.K_DOWN]:
                        elementos = 1
                elif velocidade >= 160 and velocidade <= 260:#___primeira área
                    if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                        screen.blit(interrogacao_img, (velocidade+10, 60))
                    elif joca[pygame.K_UP] and joca[pygame.K_DOWN]:
                        elementos = 1
            elif local == 3:#_sala - encostado no sofá
                if velocidade >= 160 and velocidade <= 260:
                    if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                        screen.blit(exclamacao_img, (velocidade+10, 60))
                    elif joca[pygame.K_UP] and joca[pygame.K_DOWN]: 
                        estado = 3
                elif velocidade >= 270 and velocidade <= 420:#___segunda área
                    if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                        screen.blit(interrogacao_img, (velocidade+10, 60))
                    elif joca[pygame.K_UP] and joca[pygame.K_DOWN]:
                        elementos = 1
                elif velocidade >= 510 and velocidade <= 720:#___terceira área
                    if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                        screen.blit(interrogacao_img, (velocidade+10, 60))
                    elif joca[pygame.K_UP] and joca[pygame.K_DOWN]:
                        elementos = 1
        #_________________________local hard
        elif local == 4:#___sala - embaixo do gato
            if perdido == chave_img:
                screen.blit(perdido, (360,180))
            elif perdido == roupaFechada_img:
                screen.blit(perdido, (330,130))
                b = 24
            else:
                screen.blit(perdido, (360,200))
                b = 14
            if velocidade >= 270 and velocidade <= 420:
                if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                    screen.blit(exclamacao_img, (velocidade+10, 60))
                elif joca[pygame.K_UP] and joca[pygame.K_DOWN]: 
                    estado = 3
            elif velocidade >= 160 and velocidade <= 260:#___primeira área
                if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                    screen.blit(interrogacao_img, (velocidade+10, 60))
                elif joca[pygame.K_UP] and joca[pygame.K_DOWN]:
                        elementos = 1
            elif velocidade >= 510 and velocidade <= 720:#___terceira área
                if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                    screen.blit(interrogacao_img, (velocidade+10, 60))
                elif joca[pygame.K_UP] and joca[pygame.K_DOWN]:
                        elementos = 1
        else:#___________________quando o objeto estiver em outro ambiente
            if velocidade >= 160 and velocidade <= 260:#___primeira área
                if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                    screen.blit(interrogacao_img, (velocidade+10, 60))
                elif joca[pygame.K_UP] and joca[pygame.K_DOWN]:
                        elementos = 1
            elif velocidade >= 270 and velocidade <= 420:#___segunda área
                if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                    screen.blit(interrogacao_img, (velocidade+10, 60))
                elif joca[pygame.K_UP] and joca[pygame.K_DOWN]:
                        elementos = 1
            elif velocidade >= 510 and velocidade <= 720:#___terceira área
                if joca[pygame.K_UP] and not joca[pygame.K_DOWN]:
                    screen.blit(interrogacao_img, (velocidade+10, 60))
                elif joca[pygame.K_UP] and joca[pygame.K_DOWN]:
                        elementos = 1
        if joca[pygame.K_RIGHT] or joca[pygame.K_LEFT]:
            if not joca[pygame.K_UP] or not joca[pygame.K_DOWN]:
                elementos = 0
                seletiva = fala_sala[random.randint(0,3)]
        if elementos == 1:
            screen.blit(perso_filho, (50, 320))
            screen.blit(seletiva, (150,320))
    screen.blit(gato_img,(360, 198 - b))
    return estado, elementos, seletiva, perdido, gato_img
def movimentoDeMainha(b):
    b += 1
    if b % 9 == 0:#_____________Movimento de mainha
        screen.blit(mainha_img, (200, 160))
    else:
        screen.blit(mainha_img, (200, 180))
    return b
def movimentoDePersonagem(a):
    a += 1
    if a % 9 == 0:#_____________Movimento de mainha
        screen.blit(personagem_parado, (350,131))
    else:
        screen.blit(personagem_parado, (350,151))
    return a
def andarilho(veloci, ambiene, a, genero):
    if a == 1:
        veloci = 350
    sentido, potencia = 13, 0
    loukura= pygame.key.get_pressed()
    if loukura[pygame.K_LEFT] and not loukura[pygame.K_DOWN]:#se andar normal para esquerda
        veloci = veloci - 5
        sentido = 13
        potencia = 0
    elif loukura[pygame.K_RIGHT] and not loukura[pygame.K_DOWN]:#se andar normal para direita
        veloci = veloci + 5
        sentido = 22
        potencia = 0
    if loukura[pygame.K_LEFT] and loukura[pygame.K_DOWN]:#se correr para esquerda
        veloci = veloci - 10
        sentido = 13
        potencia = 2
    elif loukura[pygame.K_RIGHT] and loukura[pygame.K_DOWN]: #se correr para esquerda
        veloci = veloci + 10
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
                screen.blit(personagem_andando, (veloci, 177))
            else:
                screen.blit(personagem_andando, (veloci, 151))
        elif sentido == 22:
            if genero == 0:
                screen.blit(pygame.transform.flip(personagem_andando, True, False), (veloci, 177))
            else:
                screen.blit(pygame.transform.flip(personagem_andando, True, False), (veloci, 151))
    a += 1
    return veloci, ambiene, a
def planoDeFundo1(chinela):
    if chinela >= 100 and chinela <= 500:
        gato_img = gatoAtento_img
    else:
        gato_img = gatoMimindo_img
    screen.blit(chao,(0,250))
    screen.blit(sofa_img,(270,130))
    screen.blit(planta_img,(600, 100))
    screen.blit(gato_img,(360, 198))
    screen.blit(portaFechada_img,(25, 15))
    screen.blit(pygame.transform.flip(inaAndando_img, True, False), (chinela + 150, 151))
    screen.blit(chinelo_img, (chinela, 131))
    if chinela >= 850:
        chinela = -350
    else:
        chinela += 5
    return chinela
def planoDeFundo2():
    screen.blit(chao,(0,250))
    screen.blit(planta_img,(600, 100))
    screen.blit(portaFechada_img,(25, 15))
def paixao(z):
    z+= 1
    if z <= 7:
        screen.blit(cora1, (120,-10))
    elif z >= 8 and z <= 17:
        screen.blit(cora2, (120,-10))
    elif z >= 18 and z <= 27:
        screen.blit(cora3, (120,-10))
    elif z >= 28 and z <= 37:
        screen.blit(cora4, (120,-10))
    elif z >= 38 and z <= 47:
        screen.blit(cora5, (120,-10))
    else:
        z = 0
    return z

'''Momento= passagem do tempo em uma cena | velocidade= movimento do personagem na tela  | tempo= contagem regressiva para o estresse total de Mainha
estado: big-bang = 0, prelúdio = 1, procura = 2, fim bom = 3, fim triste = 4 #___________Variáveis
fase: fácil = 1, difícil = 3      |     sentido: direita = 22, esquerda = 13
ambiente: sala= 0, cozinha = 1    |     genero: menino = 0, menina = 1'''
estado, fase, ambiente, genero, momento, b, a, velocidade, mome, tempo, x, z, veloc, k, l, sentid = 0, 0, 0, 0, 0, 0, 0, 350, 0, 350, -200, 0, 0, 0, 0, 13
#local: 1= atrás da planta, 2= Dentro da pia, 3= Emcima da planta | 4= embaixo do gato, 5= dentro da geladeira, 6= dentro do fogão
lugar = [1,2,3,4,5,6]
#objetos: 0= guarda-chuva, 1= roupa do if, 2= celular, 3= chave
objetos = [guardaChuva_img, roupa_img, celular_img, chave_img]

while True:
    t_emporizador =  tipográfico.render(f"Paciência: {tempo}", True, (28,28,28)) 
    for event in pygame.event.get():#_____________________Leitura de eventos
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if estado == 1 or estado == 3:
               momento += 1
            if estado == 0 and momento == 3:
                if mouse_x < 400: #looping da tela e mudança de informações
                    sentid = 13
                if mouse_x > 400:
                    sentid = 22
                if sentid == 22:
                    mome += 1
                    if mome > 3:
                        mome = 0
                elif sentid == 13:
                    mome -= 1
                    if mome < 0:
                        mome = 3
    screen.fill((216,191,216)) #__________Repintando a tela 
    if estado == 0: #____________________________________________Tela inicial
        gologo, senti, escolha = pygame.key.get_pressed() , -1, pygame.key.get_pressed()
        ambiente = 0
        if fase != 3:
            tempo = 450
        else:
            tempo = 325
        if momento < 1:
            x = planoDeFundo1(x)
        elif momento == 2:
            planoDeFundo2()
        else:
            screen.blit(chao,(0,350))
        if momento == 0: #tela inicial inicial
            screen.blit(titulo, (245, 0))
            screen.blit(botao, (245, 94))
            screen.blit(esquerda, (100,133))
            screen.blit(p_rogram, (385, 175))#texto
            screen.blit(botao, (245, 164))
            screen.blit(cima, (105,200))
            screen.blit(pr_ogram, (368, 245))#texto
            screen.blit(botao, (245, 230))
            screen.blit(direita, (100, 270))
            screen.blit(pro_gram, (380, 310))#texto
            if gologo[pygame.K_UP] and not gologo[pygame.K_RIGHT] and not gologo[pygame.K_LEFT]:#_____Cima
                senti = 1
            if gologo[pygame.K_LEFT] and not gologo[pygame.K_RIGHT] and not gologo[pygame.K_UP]:#___Esquerda
                senti = 0
            if gologo[pygame.K_RIGHT] and not gologo[pygame.K_LEFT] and not gologo[pygame.K_UP]:#___Direita
                senti = 2
            if senti == 0:#__________Jogar
                momento = 1
            elif senti == 1:#________Customizar
                momento = 2
            elif senti == 2:#________Tutorial
                momento = 3
        if momento == 1: #Jogar e nível - Jogar  _________Escolha da dificuldade
            if (escolha[pygame.K_LEFT] and not escolha[pygame.K_RIGHT]) or fase == 1:#___________fácil
                fase, local, perdido = 1, lugar[random.randint(0,2)], guardaChuva_img
                screen.blit(moldura, (122,30))
            if (escolha[pygame.K_RIGHT] and not escolha[pygame.K_LEFT]) or fase == 3:#_____________Difícil
                fase, local, perdido = 3, lugar[random.randint(0,5)], objetos[random.randint(0,3)]
                screen.blit(moldura, (382,30))
            if escolha[pygame.K_DOWN] and not escolha[pygame.K_UP]:
                momento, estado = 0, 1
            screen.blit(esquerda, (238, 40))
            screen.blit(direita, (498, 40))
            screen.blit(baixo, (700,270))
            screen.blit(prog_ram, (706, 350))
            screen.blit(osso, (447,110))
            screen.blit(mamao, (187,105))
        elif momento == 2: #___________________________personagem - customizar
            screen.blit(menina_img, (190,100))
            screen.blit(menino_img, (450,103))
            screen.blit(baixo, (700,-10))
            screen.blit(prog_ram, (706, 70))
            #screen.blit(botao2, (196, 240))
            escolha = pygame.key.get_pressed()
            if (escolha[pygame.K_LEFT] and not escolha[pygame.K_RIGHT]) or genero == 1:
                genero = 1#______Menina
                screen.blit(moldura, (122,30))
                personagem_parado, personagem_andando = parada_img, inaAndando_img
            else:
                genero == 0  
            if (escolha[pygame.K_RIGHT] and not escolha[pygame.K_LEFT]) or genero == 0:
                genero = 0#_____Menino
                personagem_parado, personagem_andando = parado_img, inoAndando_img
                screen.blit(moldura, (382,30))
            screen.blit( esquerda, (238, 40))
            screen.blit( direita, (496,  40))
            if not escolha[pygame.K_UP] and escolha[pygame.K_DOWN]:
                momento = 0
        elif momento == 3: #Tutorial dos botões e jogabilidade - tutorial
            calçaRasgada = pygame.key.get_pressed()
            screen.blit(baixo, (700,-10))
            screen.blit(progr_am, (731, 70))
            screen.blit(controle, (403, 300))
            screen.blit(controle, (280, 300))
            if calçaRasgada[pygame.K_DOWN] and not calçaRasgada[pygame.K_UP]:#sair
                momento, mome = 0, 0
            if sentid == 22:
                screen.blit(pygame.transform.flip(miniEu, True, False), (355,300))
            else:
                screen.blit(miniEu, (355,300))
            if mome == 0: #________primeira tela
                screen.blit(image0, (50,130))
                screen.blit(cima,(570,100))
                screen.blit(baixo,(520, 105))
                screen.blit(tutorial_, (480,98))#pegar objeto perdido
                screen.blit(controle,(540, 215))
                screen.blit(tuto_rial, (480,207))#toque do mouse
            elif mome == 1: #______segunda
                screen.blit(image1, (50,80))
                screen.blit(baixo,(500,100))
                screen.blit(esquerda,(450, 105))
                screen.blit(tu_torial, (574,150))#ou
                screen.blit(direita,(620,102))
                screen.blit(baixo,(580,100))
                screen.blit(tut_orial, (548,98))#faz correr
                screen.blit(esquerda,(450, 215))
                screen.blit(tu_torial, (574,260))#ou
                screen.blit(direita,(620,212))
                screen.blit(tutor_ial, (480,207))#movimenta o personagem
            elif mome == 2:#________terceira
                screen.blit(image2, (50, 130))
                screen.blit(esquerda,(450, 105))
                screen.blit(direita,(620,102))
                screen.blit(tutori_al, (480,98))#abre a geladeira e o fogão
                screen.blit(baixo,(540, 215))
                screen.blit(tutoria_l, (480,207))#fecha a geladeira e o fogão
            else:#______________quarta
                screen.blit(image3, (50,80))
                screen.blit(cima, (450, 105))
                screen.blit(t_utorial, (540,150))#mostra
                screen.blit(exclamacao_img, (665, 100))
                screen.blit(tu_torial, (660,150))#ou
                screen.blit(interrogacao_img, (580, 110))
            
    if estado == 1:#__________________Puxada de orelha  ___________________________________________________________Jogo
            screen.blit(chao,(0,250))
            screen.blit(controle, (670,285))
            estado, mome, seletor_sala, perdido, gato_img = sala(estado, mome, seletor_sala, perdido, gato_img)
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
                momento, a, b, x = 0, 0 , 0, -100
    if fase == 1 and estado == 2:#______Separação de fase
            tempo -= 1
            screen.blit(chao,(0,250))
            if ambiente == 0:
                estado,mome, seletor_sala, perdido, gato_img = sala(estado, mome, seletor_sala, perdido, gato_img)
            if ambiente == 1:
                estado,momento, seletor_cozinha, geladeira_img, fogao_img = cozinha(estado, momento, seletor_cozinha, geladeira_img, fogao_img)
            velocidade, ambiente, a = andarilho(velocidade, ambiente, a, genero)#função do movimento controlado
            screen.blit(t_emporizador,(600,10))
            if tempo == 0:#____________________________perder por conta do tempo
                estado = 4
                momento = 0
    if fase == 3 and estado ==2:#_____Difícil
            tempo -= 1
            screen.blit(chao,(0,250))
            if ambiente == 0:
                estado,mome, seletor_sala, perdido, gato_img = sala(estado, mome, seletor_sala, perdido, gato_img)
            if ambiente == 1:
                estado,momento, seletor_cozinha, geladeira_img, fogao_img = cozinha(estado,momento, seletor_cozinha, geladeira_img, fogao_img)
            velocidade, ambiente, a = andarilho(velocidade, ambiente, a, genero)#função do movimento controlado
            screen.blit(t_emporizador,(600,10))
            if tempo == 0:#____________________________perder por conta do tempo
                estado = 4
                momento = 0
    elif estado == 3:#_________________Final feliz
            screen.blit(chao,(0,250))
            estado, mome, seletor_sala, perdido, gato_img = sala(estado, mome, seletor_sala, perdido, gato_img)
            screen.blit(controle, (680,280))
            gologodo = pygame.key.get_pressed()
            if momento == 0:#__segurando item
                screen.blit(mainha_img, (200,180))
                screen.blit(perso_filho, (50, 320))
                a = movimentoDePersonagem(a)
                screen.blit(f_rase,(150,320))
            elif  momento == 1:#__entregar 
                veloc += 3
                if perdido == chave_img:
                    k, l = 0, 90
                if perdido == celular_img:
                    k, l = -20, 60
                if perdido == roupaFechada_img:
                    k,l, perdido = -30, 15, roupaAberta_img
                if perdido == guardaChuva_img:
                    k,l = 0,0
                if (370 - veloc) > 270:
                    laraya = (370-veloc) + k
                    screen.blit(perdido, (laraya, 151+l))
                else:
                    screen.blit(perdido, (laraya, 151+(l-15)))
                screen.blit(mainha_img,(200, 180))
                screen.blit(personagem_parado, (350, 151))
            elif  momento == 2:#__corações
                z = paixao(z)
                screen.blit(personagem_parado, (350, 151))
                b = movimentoDeMainha(b)
                screen.blit(perso_mainha, (50, 320))
                if genero == 0:
                    screen.blit(fr_ase,(150,320))
                else:
                    screen.blit(fra_se,(150,320))
            else:
                momento, estado, veloc = 0, 0, 0
                geladeira_img, fogao_img = geladeiraFechada_img, fogaoFechado_img
    elif estado == 4:#_____________Final triste
            screen.blit(chao,(0,250))
            x += 10
            if ambiente == 0:
                estado,mome, seletor_sala, perdido, gato_img = sala(estado, mome, seletor_sala, perdido, gato_img)
            if ambiente == 1:
                estado, momento, seletor_cozinha, geladeira_img, fogao_img = cozinha(estado, momento, seletor_cozinha, geladeira_img, fogao_img)

            if x >= (velocidade-70):
                screen.blit(chinelo_img,(velocidade-70,131))
                screen.blit(personagem_andando,(velocidade,151))
                momento, estado, veloc = 0, 0, 0
                geladeira_img, fogao_img = geladeiraFechada_img, fogaoFechado_img
            else:
                screen.blit(personagem_parado,(velocidade,151))
                screen.blit(chinelo_img,(x,131))
    
    pygame.display.flip()
    clock.tick(30)  # taxa de quadros por segundo (FPS)
pygame.quit()