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

# Contador y objetivo
objetivo_contador = 5
cantidad_actual = 0

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Establecer el título de la ventana
pygame.display.set_caption("Nivel1")

# Crear una fuente para el texto
fuente = pygame.font.SysFont(None, 20)

# Cargar fondo y escalar a las dimensiones de la ventana
nivel1 = pygame.image.load("nivel1.png").convert()
nivel1 = pygame.transform.scale(nivel1, (ancho, alto))

# ... (código existente)

def juego(tiempo_inicial):
    global auxiliar, jugador_x, jugador, cantidad_actual  # Permitimos modificar la variable global auxiliar, jugador y cantidad_actual
    jugador_x = ancho // 2 - 100  # Posición inicial del jugador en x
    tiempo_max = 120  # Tiempo máximo en segundos

    while True:
        tiempo_juego = (pygame.time.get_ticks() - tiempo_inicial) // 1000
        tiempo = tiempo_max - tiempo_juego

        if auxiliar != tiempo:
            auxiliar = tiempo

        ventana.blit(nivel1, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] and jugador_x > 0:
            jugador_x -= 5
            jugador = jugador_izquierda
        elif teclas[pygame.K_RIGHT] and jugador_x < ancho - 200:
            jugador_x += 5
            jugador = jugador_derecha

        # Verificar colisión con el objeto
        if jugador_x < objeto_x + 90 and jugador_x + 200 > objeto_x and 570 < objeto_y + 140:
            cantidad_actual += 1
            objeto_x = random.uniform(0, ancho - 200)
            objeto_y = 0

        contador = fuente.render("Tiempo: " + str(tiempo), 0, color_negro)
        ventana.blit(contador, (10, 10))

        contador_objetivo = fuente.render("Contador: " + str(cantidad_actual) + "/" + str(objetivo_contador), 0, color_negro)
        ventana.blit(contador_objetivo, (10, 50))

        ventana.blit(jugador, (jugador_x, 570))
        ventana.blit(objeto1, (objeto_x, objeto_y))

        pygame.display.update()
        relojPrincipal.tick(60)

# Inicializar el juego
tiempo_inicial = pygame.time.get_ticks()
juego(tiempo_inicial)
