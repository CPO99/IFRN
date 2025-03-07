import pygame

pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Texto Centralizado")

# Configurações da fonte
fonte = pygame.font.Font(None, 36)
texto = fonte.render("Olá, Pygame!", True, (255, 255, 255))
retangulo_texto = texto.get_rect()
retangulo_texto.center = (largura_tela // 2, altura_tela // 2)

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Limpar a tela
    tela.fill((0, 0, 0))

    # Desenhar o texto centralizado
    tela.blit(texto, retangulo_texto)

    # Atualizar a tela
    pygame.display.flip()

pygame.quit()