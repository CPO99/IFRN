import pygame
import random

# Inicializa o pygame
pygame.init()

# Define as dimensões da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")

# Cores
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Tamanho do bloco da cobra
tamanho_bloco = 20

# Velocidade da cobra
velocidade = 5

# Fonte para o texto
fonte = pygame.font.SysFont(None, 25)

def mensagem(msg, cor):
    """Exibe uma mensagem na tela."""
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])

def jogo_snake(tamanho_bloco, lista_cobra):
    """Desenha a cobra na tela."""
    for x, y in lista_cobra:
        pygame.draw.rect(tela, verde, [x, y, tamanho_bloco, tamanho_bloco])

def jogo():
    """Função principal do jogo."""
    fim_jogo = False
    fechar_jogo = False

    # Posição inicial da cobra
    x = largura / 2
    y = altura / 2

    # Mudança na posição
    x_mudanca = 0
    y_mudanca = 0

    # Lista para armazenar o corpo da cobra
    lista_cobra = []
    comprimento_cobra = 1

    # Posição da comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    # Loop principal do jogo
    while not fim_jogo:

        while fechar_jogo == True:
            tela.fill(branco)
            mensagem("Você perdeu! Pressione C para jogar novamente ou Q para sair", vermelho)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        fechar_jogo = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        # Verifica se a cobra bateu nas bordas
        if x >= largura or x < 0 or y >= altura or y < 0:
            fechar_jogo = True

        # Atualiza a posição da cobra
        x += x_mudanca
        y += y_mudanca

        # Preenche a tela com branco
        tela.fill(branco)

        # Desenha a comida
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        # Adiciona a cabeça da cobra à lista
        cabeca_cobra = []
        cabeca_cobra.append(x)
        cabeca_cobra.append(y)
        lista_cobra.append(cabeca_cobra)

        # Mantém o tamanho da cobra
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verifica se a cobra bateu em si mesma
        for parte in lista_cobra[:-1]:
            if parte == cabeca_cobra:
                fechar_jogo = True

        # Desenha a cobra
        jogo_snake(tamanho_bloco, lista_cobra)

        # Atualiza a tela
        pygame.display.update()

        # Verifica se a cobra comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        # Controla a velocidade do jogo
        pygame.time.Clock().tick(velocidade)

    # Encerra o pygame
    pygame.quit()
    quit()

# Inicia o jogo
jogo()
