import pygame

largura = 640
altura = 480
velocidade = 4
pontos_por_coletavel = 25

arena = pygame.Rect(0, 50, largura, altura - 50)

obstaculos = [
    pygame.Rect(144, 148, 88, 30),
    pygame.Rect(425, 245, 36, 88),
    pygame.Rect(185, 365, 102, 30),
]

tipos_coletaveis = {
    "Azul": ((90, 172, 255), (105, 165)),
    "Vermelho": ((255, 80, 96), (486, 276)),
    "Branco": ((245, 245, 245), (232, 330)),
}


def mover(jogador, dx, dy):
    x_anterior = jogador.x
    jogador.x += dx
    jogador.clamp_ip(arena)
    if jogador.collidelist(obstaculos) != -1:
        jogador.x = x_anterior

    y_anterior = jogador.y
    jogador.y += dy
    jogador.clamp_ip(arena)
    if jogador.collidelist(obstaculos) != -1:
        jogador.y = y_anterior


def comecar_partida():
    jogador = pygame.Rect(0, 0, 20, 20)
    jogador.center = arena.center
    coletaveis = {}
    for nome, (_, (x, y)) in tipos_coletaveis.items():
        coletaveis[nome] = pygame.Rect(x - 7, y - 7, 14, 14)
    quantidades = dict.fromkeys(tipos_coletaveis, 0)
    return jogador, coletaveis, quantidades, 0


def jogar():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Verbum Caninum")
    clock = pygame.time.Clock()
    fonte = pygame.font.Font(None, 24)

    jogador, coletaveis, quantidades, placar = comecar_partida()
    rodando = True

    while rodando:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif evento.key == pygame.K_r:
                    jogador, coletaveis, quantidades, placar = comecar_partida()

        teclas = pygame.key.get_pressed()
        dx = teclas[pygame.K_d] - teclas[pygame.K_a]
        dy = teclas[pygame.K_s] - teclas[pygame.K_w]

        passo = velocidade
        if dx != 0 and dy != 0:
            passo = round(velocidade / 1.414)
        mover(jogador, dx * passo, dy * passo)

        for nome, coletavel in coletaveis.copy().items():
            if jogador.colliderect(coletavel):
                del coletaveis[nome]
                quantidades[nome] += 1
                placar += pontos_por_coletavel

        tela.fill((16, 19, 31))
        for obstaculo in obstaculos:
            pygame.draw.rect(tela, (78, 91, 117), obstaculo)
        for nome, coletavel in coletaveis.items():
            cor, _ = tipos_coletaveis[nome]
            pygame.draw.circle(tela, cor, coletavel.center, 7)
        pygame.draw.rect(tela, (251, 83, 100), jogador)

        pygame.draw.rect(tela, (26, 32, 48), (0, 0, largura, arena.top))
        texto = fonte.render(f"Placar: {placar}", True, (234, 239, 251))
        tela.blit(texto, (14, 16))
        x = 108
        for nome, quantidade in quantidades.items():
            cor, _ = tipos_coletaveis[nome]
            texto = fonte.render(f"{nome}: {quantidade}/1", True, cor)
            tela.blit(texto, (x, 16))
            x += texto.get_width() + 12
        controles = fonte.render("WASD: mover   |   R: reiniciar", True, (190, 202, 221))
        tela.blit(controles, (largura - controles.get_width() - 14, 16))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    jogar()
