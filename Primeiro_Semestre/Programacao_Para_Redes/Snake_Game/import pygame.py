import pygame

pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Caixa de Texto Pygame")

# Cores
cor_fundo = (255, 255, 255)
cor_texto = (0, 0, 0)
cor_caixa_texto = (200, 200, 200)

# Fonte
fonte = pygame.font.Font(None, 32)

# Caixa de texto
caixa_texto = pygame.Rect(100, 100, 600, 40)
texto = ""

executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                print(texto)  # Exibe o texto quando Enter é pressionado
                texto = "Teste"  # Limpa a caixa de texto
            elif evento.key == pygame.K_BACKSPACE:
                texto = texto[:-1]  # Remove o último caractere
            else:
                texto += evento.unicode  # Adiciona o caractere digitado

    # Desenha a tela
    tela.fill(cor_fundo)
    pygame.draw.rect(tela, cor_caixa_texto, caixa_texto)

    # Renderiza o texto
    superficie_texto = fonte.render(texto, True, cor_texto)
    tela.blit(superficie_texto, (caixa_texto.x + 5, caixa_texto.y + 5))

    pygame.display.flip()

pygame.quit()