import pygame
import sys

pygame.init()

# Tamanho da tela
WIDTH, HEIGHT = 800, 600
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Raquetes
RAQUETE_LARGURA, RAQUETE_ALTURA = 10, 100
raquete1 = pygame.Rect(50, HEIGHT // 2 - 50, RAQUETE_LARGURA, RAQUETE_ALTURA)
raquete2 = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 50, RAQUETE_LARGURA, RAQUETE_ALTURA)

# Bola
bola = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
velocidade_bola_x = 5
velocidade_bola_y = 5

# Velocidade das raquetes
velocidade_raquete = 7

# Pontuação
pontos1 = 0
pontos2 = 0
fonte = pygame.font.Font(None, 36)

# Loop principal
clock = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles das raquetes
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete1.top > 0:
        raquete1.y -= velocidade_raquete
    if teclas[pygame.K_s] and raquete1.bottom < HEIGHT:
        raquete1.y += velocidade_raquete
    if teclas[pygame.K_UP] and raquete2.top > 0:
        raquete2.y -= velocidade_raquete
    if teclas[pygame.K_DOWN] and raquete2.bottom < HEIGHT:
        raquete2.y += velocidade_raquete

    # Movimento da bola
    bola.x += velocidade_bola_x
    bola.y += velocidade_bola_y

    # Colisão com o topo e base
    if bola.top <= 0 or bola.bottom >= HEIGHT:
        velocidade_bola_y *= -1

    # Colisão com as raquetes
    if bola.colliderect(raquete1) or bola.colliderect(raquete2):
        velocidade_bola_x *= -1

    # Pontuação
    if bola.left <= 0:
        pontos2 += 1
        bola.center = (WIDTH // 2, HEIGHT // 2)
        velocidade_bola_x *= -1

    if bola.right >= WIDTH:
        pontos1 += 1
        bola.center = (WIDTH // 2, HEIGHT // 2)
        velocidade_bola_x *= -1

    # Desenho
    TELA.fill(PRETO)
    pygame.draw.rect(TELA, BRANCO, raquete1)
    pygame.draw.rect(TELA, BRANCO, raquete2)
    pygame.draw.ellipse(TELA, BRANCO, bola)
    pygame.draw.aaline(TELA, BRANCO, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    texto = fonte.render(f"{pontos1}  -  {pontos2}", True, BRANCO)
    TELA.blit(texto, (WIDTH // 2 - 50, 20))

    pygame.display.flip()
    clock.tick(60)
