import pygame, random

#iniciar pygame
pygame.init()

#configurações de tela
tela_largura = 720
tela_altura = 480
tela = pygame.display.set_mode((tela_largura,tela_altura), pygame.RESIZABLE)
pygame.display.set_caption('Jogo da Cobrinha')

#cores
branco = (255,255,255) 
preto = (0,0,0)
amarelo = (255, 255, 0)

#função para cobra
def cobra(cobra_tamanho, cobra_corpo):
    for x, y in cobra_corpo:
        pygame.draw.rect(tela, branco, [x, y, cobra_tamanho, cobra_tamanho])

#função para fruta
def fruta(fruta_pos_x, fruta_pos_y, cobra_tamanho):
    cores = ["white","red","green","yellow","blue","silver"]
    
    pygame.draw.rect(tela,  random.sample(cores,1)[0], [fruta_pos_x, fruta_pos_y, cobra_tamanho, cobra_tamanho])

#função para contar frutas comidas
def contadorFruta():
    pass

#função principal do jogo
def jogo(tela_largura, tela_altura):
    jogo_exe = True

    clock = pygame.time.Clock()

    #posição inicial da cobra
    cobra_pos_x = 300
    cobra_pos_y = 300

    #armazena mudança de posição da cobra
    cobra_mov_x = 0
    cobra_mov_y = 0

    #lista para armazenar o corpo da cobra, a posição de cada bloco do corpo
    cobra_corpo = []

    #lado do retângulo que forma a cobra
    cobra_tamanho = 15
    
    #armazena a quantidade de blocos que compõem o corpo da cobra
    cobra_blocos_qtd = 1
    
    #definindo posição da fruta
    tela_largura, tela_altura = tela.get_size()
    fruta_pos_x = round(random.randrange(0, tela_largura) / cobra_tamanho) * cobra_tamanho
    fruta_pos_y = round(random.randrange(0, tela_altura) / cobra_tamanho) * cobra_tamanho

    nivel = 0

    tempo_inicio = pygame.time.get_ticks()

    menu = True
    fim_jogo = False
    principal = False
            
    while jogo_exe:
        tempo_atual = pygame.time.get_ticks()
        if menu:
            tela.fill(preto)

            fonte = pygame.font.Font(None, 40)
            texto = fonte.render("ESCOLHA O NIVEL DO JOGO", True, (255, 255, 255))
            retangulo_texto = texto.get_rect()
            retangulo_texto.center = (tela_largura // 2, tela_altura // 2 - 80)
            tela.blit(texto, retangulo_texto)

            fonte = pygame.font.Font(None, 30)
            texto = fonte.render("[1] - Nivel 1", True, (255, 255, 255))
            retangulo_texto = texto.get_rect()
            retangulo_texto.center = (tela_largura // 2, tela_altura // 2 - 30)
            tela.blit(texto, retangulo_texto)

            fonte = pygame.font.Font(None, 30)
            texto = fonte.render("[2] - Nivel 2", True, (255, 255, 255))
            retangulo_texto = texto.get_rect()
            retangulo_texto.center = (tela_largura // 2, tela_altura // 2)
            tela.blit(texto, retangulo_texto)

            fonte = pygame.font.Font(None, 30)
            texto = fonte.render("[3] - Nivel 3", True, (255, 255, 255))
            retangulo_texto = texto.get_rect()
            retangulo_texto.center = (tela_largura // 2, tela_altura // 2 + 30)
            tela.blit(texto, retangulo_texto)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                        jogo_exe = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        nivel = 10
                        menu = False
                        principal = True
                    elif evento.key == pygame.K_2:
                        nivel = 20
                        menu = False
                        principal = True
                    elif evento.key == pygame.K_3:
                        nivel = 30
                        menu = False
                        principal = True
                    elif evento.key == pygame.K_4:
                        menu = False
                        fim_jogo = True

        elif principal:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    jogo_exe = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        cobra_mov_x = -cobra_tamanho
                        cobra_mov_y = 0
                    elif evento.key == pygame.K_RIGHT:
                        cobra_mov_x = cobra_tamanho
                        cobra_mov_y = 0
                    elif evento.key == pygame.K_UP:
                        cobra_mov_x = 0
                        cobra_mov_y = -cobra_tamanho
                    elif evento.key == pygame.K_DOWN:
                        cobra_mov_x = 0
                        cobra_mov_y = cobra_tamanho

            #Atualiza a posição da cobra
            cobra_pos_x += cobra_mov_x
            cobra_pos_y += cobra_mov_y

            #Preenche a tela com preto
            tela.fill(preto)

            #Desenha a fruta
            fruta(fruta_pos_x, fruta_pos_y, cobra_tamanho)
        
            #acrescenta um bloco ao corpo da cobra
            cobra_bloco = []
            cobra_bloco.append(cobra_pos_x)
            cobra_bloco.append(cobra_pos_y)
            cobra_corpo.append(cobra_bloco)
        
            #garante que a cobra não fique maior do que deve
            if len(cobra_corpo) > cobra_blocos_qtd:
                del cobra_corpo[0]

            cobra(cobra_tamanho, cobra_corpo)

            pygame.display.update()
        
            #verificando se cobra comeu a fruta e mudando de posição, conforme níveis 2 e 3
            if (cobra_pos_x == fruta_pos_x and cobra_pos_y == fruta_pos_y) or ((nivel == 20 or nivel == 30) and tempo_atual - tempo_inicio > 2000):
                fruta_pos_x = round(random.randrange(0, tela_largura) / cobra_tamanho) * cobra_tamanho
                fruta_pos_y = round(random.randrange(0, tela_altura) / cobra_tamanho) * cobra_tamanho

                tempo_inicio = tempo_atual
            
                cobra_blocos_qtd += 1

            if nivel == 30:
                if cobra_pos_x < 0 or cobra_pos_x > tela_largura or cobra_pos_y < 0 or cobra_pos_y > tela_altura:
                    principal = False
                    fim_jogo = True
                    
        elif fim_jogo:
            tela.fill(preto)

            cobra_blocos_qtd = 1

            fonte = pygame.font.Font(None, 50)
            texto = fonte.render("FIM DE JOGO!", True, amarelo)
            retangulo_texto = texto.get_rect()
            retangulo_texto.center = (tela_largura // 2, tela_altura // 2)

            tela.blit(texto, retangulo_texto)

            fonte = pygame.font.Font(None, 20)
            texto = fonte.render("Pressione qualquer tecla para continuar...", True, branco)
            retangulo_texto = texto.get_rect()
            retangulo_texto.center = (tela_largura // 2, tela_altura // 2 + 80)

            tela.blit(texto, retangulo_texto)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = False
                    jogo_exe = False
                    
                if evento.type == pygame.KEYDOWN:
                    menu = True
                    fim_jogo = False

        pygame.display.flip()
        clock.tick(nivel)

jogo(tela_largura, tela_altura)
    

