import pygame
import sys
from prueba2 import *

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana principal
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

# Cargar fondo y escalar a las dimensiones de la ventana
fondo = pygame.image.load("fin_del_juego.png").convert()
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Colores RGB
color_blanco = (255, 255, 255)

# Recursos para botones
boton1 = pygame.image.load("volver.png")
boton1.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
boton1 = pygame.transform.scale(boton1, (130, 50))

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Variable para controlar el clic del ratón
clic = False

# Función para el menú principal
def ganar():
    global clic  # Declarar 'clic' como global
    while True:
        ventana.blit(fondo, (0, 0))

        # Obtener la posición del ratón
        mx, my = pygame.mouse.get_pos()

        # Dibujar el botón
        ventana.blit(boton1, (560, 510))
        
        # Obtener el rectángulo del botón
        boton1_rect = boton1.get_rect(topleft=(560, 510))

        # Verificar si el ratón está sobre el botón
        if boton1_rect.collidepoint((mx, my)):
            # Verificar si se hizo clic
            if clic:
                iniciar_juego()
             
        # Reiniciar la variable de clic
        clic = False

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    clic = True

        # Actualizar la ventana
        pygame.display.update()
        relojPrincipal.tick(60)