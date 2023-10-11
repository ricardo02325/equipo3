import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana principal
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

# Colores RGB
color_blanco = (255, 255, 255)
color_verde = (0, 255, 0)
color_negro = (0, 0, 0)

# Variable para poder poner el tiempo en reversa
auxiliar = 0

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Establecer el título de la ventana
pygame.display.set_caption("Nivel1")

# Crear una fuente para el texto
fuente = pygame.font.SysFont(None, 20)

# Cargar fondo y escalar a las dimensiones de la ventana
nivel1 = pygame.image.load("nivel1.png").convert()
nivel1 = pygame.transform.scale(nivel1, (ancho, alto))

# Recursos para jugador
jugador_derecha = pygame.image.load("personaje1.png")
jugador_derecha.set_colorkey(color_blanco)
jugador_derecha = pygame.transform.scale(jugador_derecha, (200, 140))

jugador_izquierda = pygame.image.load("personaje2.png")
jugador_izquierda.set_colorkey(color_blanco)
jugador_izquierda = pygame.transform.scale(jugador_izquierda, (200, 140))

jugador = jugador_derecha  # Inicialmente, el jugador mira hacia la derecha

# Recursos para objeto
objeto1 = pygame.image.load("pescao.png")
objeto1.set_colorkey(color_blanco)
objeto1 = pygame.transform.scale(objeto1, (90, 140))

# Posición inicial del objeto
objeto_x = random.uniform(0, ancho - 200)
objeto_y = 0

# Cosas para la fuente
fuente = pygame.font.SysFont("Arial", 30)

def juego(tiempo_inicial):
    corriendo = True
    global auxiliar, jugador_x, jugador  # Permitimos modificar la variable global auxiliar y jugador
    jugador_x = ancho // 2 - 100  # Posición inicial del jugador en x
    tiempo_max = 120  # Tiempo máximo en segundos

    while corriendo:
        tiempo_juego = (pygame.time.get_ticks() - tiempo_inicial) // 1000
        tiempo = tiempo_max - tiempo_juego

        if auxiliar != tiempo:
            auxiliar = tiempo

        ventana.blit(nivel1, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Obtener las teclas presionadas
        teclas = pygame.key.get_pressed()

        # Mover al jugador
        if teclas[pygame.K_LEFT] and jugador_x > 0:
            jugador_x -= 5
            jugador = jugador_izquierda  # Cambiar al personaje que camina hacia la izquierda
        elif teclas[pygame.K_RIGHT] and jugador_x < ancho - 200:
            jugador_x += 5
            jugador = jugador_derecha  # Cambiar al personaje que camina hacia la derecha

        # Pon el tiempo en pantalla
        contador = fuente.render("Tiempo: " + str(tiempo), 0, (0,0,0))
        ventana.blit(contador, (10, 10))

        # Dibujar jugador
        ventana.blit(jugador, (jugador_x, 570))

        # Dibujar objeto
        ventana.blit(objeto1, (objeto_x, objeto_y))

        # Actualizar la ventana
        pygame.display.update()
        relojPrincipal.tick(60)

# Inicializar el juego
tiempo_inicial = pygame.time.get_ticks()
juego(tiempo_inicial)