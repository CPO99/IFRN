import pygame
import random

#iniciar pygame
pygame.init()

#configurações de tela
tela = pygame.display.set_mode((0,0), pygame.RESIZABLE)

#cores
branco = (255,255,255) 
preto = (0,0,0)

#função para fruta
def fruta(fruta_pos_x, fruta_pos_y, cobra_tamanho):
    cores = ["white","red","green","yellow","silver"]
    
    pygame.draw.rect(tela,  random.sample(cores,1)[0], [fruta_pos_x, fruta_pos_y, cobra_tamanho, cobra_tamanho])

#função para cobra
def cobra(cobra_tamanho, cobra_corpo):
    for x, y in cobra_corpo:
        pygame.draw.rect(tela, branco, [x, y, cobra_tamanho, cobra_tamanho])

#função principal do jogo
def jogo():
    jogo_exe = True

    #posição inicial da cobra
    cobra_pos_x = 300
    cobra_pos_y = 300

    #armazena mudança de posição da cobra
    cobra_mov_x = 0
    cobra_mov_y = 0

    #lista para armazenar o corpo da cobra, a posição de cada bloco do corpo
    cobra_corpo = []
    
    #armazena a quantidade de blocos que compõem o corpo da cobra
    cobra_blocos_qtd = 1

    cobra_tamanho = 15
    
    #definindo posição da fruta
    tela_largura, tela_altura = tela.get_size()
    fruta_pos_x = round(random.randrange(0, tela_largura) / cobra_tamanho) * cobra_tamanho
    fruta_pos_y = round(random.randrange(0, tela_altura) / cobra_tamanho) * cobra_tamanho

    nivel = 10

    while jogo_exe:  
        pygame.display.flip()
        
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
        
        #verificando se cobra comeu a fruta
        if cobra_pos_x == fruta_pos_x and cobra_pos_y == fruta_pos_y:
            fruta_pos_x = round(random.randrange(0, tela_largura) / cobra_tamanho) * cobra_tamanho
            fruta_pos_y = round(random.randrange(0, tela_altura) / cobra_tamanho) * cobra_tamanho
            
            cobra_blocos_qtd += 1

        pygame.time.Clock().tick(nivel)

jogo()
    

