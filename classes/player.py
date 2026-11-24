import pygame
from constantes import LARGURA, ALTURA, ACELERACAO, ATRITO, VELOCIDADE_MAXIMA

class Player:
    def __init__(self, x, y):
        # Posicao do jogador
        self.posicao_x = x
        self.posicao_y = y
        
        # Velocidade do jogador
        self.velocidade_x = 0.0
        self.velocidade_y = 0.0

        # Largura do jogador
        self.largura = 20
        self.altura = 20

    # Função para a movimentação - A aceleração vai aumentando progressivamente aumentando a velocidade
    def movimentacao(self, teclas):
        if teclas[pygame.K_a]:
            self.velocidade_x -= ACELERACAO
        if teclas[pygame.K_d]:
            self.velocidade_x += ACELERACAO
        if teclas[pygame.K_w]:
            self.velocidade_y -= ACELERACAO
        if teclas[pygame.K_s]:
            self.velocidade_y += ACELERACAO

        # Simulando atrito com o chão
        self.velocidade_x *= ATRITO
        self.velocidade_y *= ATRITO

        # Limite da velocidade máxima, para que não ulrapasse caso a aceleração aumente mais que o limite
        self.velocidade_x = max(-VELOCIDADE_MAXIMA, min(self.velocidade_x, VELOCIDADE_MAXIMA))
        self.velocidade_y = max(-VELOCIDADE_MAXIMA, min(self.velocidade_y, VELOCIDADE_MAXIMA))

        # Atualiza a posição
        self.posicao_x += self.velocidade_x
        self.posicao_y += self.velocidade_y

        # Limites do mapa -> (A ideia final é que o mapa se mova)
        # PARA LARGURA
        if self.posicao_x < 0:
            self.posicao_x = 0
            self.velocidade_x = 0
          
        elif self.posicao_x > LARGURA - self.largura:
            self.posicao_x = LARGURA - self.largura
            self.velocidade_x = 0

        # PARA ALTURA
        if self.posicao_y < 0:
            self.posicao_y = 0
            self.velocidade_y = 0
        elif self.posicao_y > ALTURA - self.altura:
            self.posicao_y = ALTURA - self.altura
            self.velocidade_y = 0

    # Funçao que desenha o player
    def desenhar(self, tela):
        return pygame.draw.rect(tela, (255, 0, 0), (self.posicao_x, self.posicao_y, self.largura, self.altura))
