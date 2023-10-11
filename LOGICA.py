import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de Colisiones")

# Cargar imagen del jugador
jugador_imagen = pygame.image.load("personaje1.png")
jugador_imagen = pygame.transform.scale(jugador_imagen, (150, 150))

# Colores
blanco = (255, 255, 255)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)

# Definir el objeto móvil
ancho_jugador = 100
alto_jugador = 100 
posicion_jugador_x = ancho // 2 - ancho_jugador // 2
posicion_jugador_y = alto - alto_jugador - 20
velocidad_jugador = 5

# Listas para almacenar objetos que caen
objetos_cayendo_rojos = []
objetos_cayendo_azules = []
objetos_cayendo_verdes = []

def dibujar_jugador(x, y):
    pantalla.blit(jugador_imagen, (x, y))

def dibujar_objetos_cayendo(objetos, color):
    for obj in objetos:
        pygame.draw.rect(pantalla, color, obj)

def main():
    global posicion_jugador_x  # Declarar posicion_jugador_x como global

    corriendo = True

    reloj = pygame.time.Clock()

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Mover el objeto móvil
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and posicion_jugador_x > 0:
            posicion_jugador_x -= velocidad_jugador
        if teclas[pygame.K_RIGHT] and posicion_jugador_x < ancho - ancho_jugador:
            posicion_jugador_x += velocidad_jugador

        # Generar objetos que caen aleatoriamente
        if random.randint(1, 100) < 3:
            ancho_objeto = 20
            alto_objeto = 20
            posicion_objeto_x = random.randint(0, ancho - ancho_objeto)
            posicion_objeto_y = 0
            rand_num = random.randint(1, 3)
            if rand_num == 1:
                objetos_cayendo_rojos.append(pygame.Rect(posicion_objeto_x, posicion_objeto_y, ancho_objeto, alto_objeto))
            elif rand_num == 2:
                objetos_cayendo_azules.append(pygame.Rect(posicion_objeto_x, posicion_objeto_y, ancho_objeto, alto_objeto))
            else:
                objetos_cayendo_verdes.append(pygame.Rect(posicion_objeto_x, posicion_objeto_y, ancho_objeto, alto_objeto))

        # Mover y eliminar objetos que caen
        for obj in objetos_cayendo_rojos:
            obj.y += 5
            if obj.y > alto:
                objetos_cayendo_rojos.remove(obj)

        for obj in objetos_cayendo_azules:
            obj.y += 5
            if obj.y > alto:
                objetos_cayendo_azules.remove(obj)

        for obj in objetos_cayendo_verdes:
            obj.y += 5
            if obj.y > alto:
                objetos_cayendo_verdes.remove(obj)

        # Detectar colisiones con objetos rojos
        for obj in objetos_cayendo_rojos:
            if pygame.Rect(posicion_jugador_x, posicion_jugador_y, ancho_jugador, alto_jugador).colliderect(obj):
                print("¡Colisión con objeto rojo!")
                objetos_cayendo_rojos.remove(obj)

        # Detectar colisiones con objetos azules
        for obj in objetos_cayendo_azules:
            if pygame.Rect(posicion_jugador_x, posicion_jugador_y, ancho_jugador, alto_jugador).colliderect(obj):
                print("¡Colisión con objeto azul!")
                objetos_cayendo_azules.remove(obj)

        # Detectar colisiones con objetos verdes
        for obj in objetos_cayendo_verdes:
            if pygame.Rect(posicion_jugador_x, posicion_jugador_y, ancho_jugador, alto_jugador).colliderect(obj):
                print("¡Colisión con objeto verde!")
                objetos_cayendo_verdes.remove(obj)

        # Limpiar la pantalla
        pantalla.fill((0, 0, 0))

        # Dibujar el objeto móvil y los objetos que caen
        dibujar_jugador(posicion_jugador_x, posicion_jugador_y)
        dibujar_objetos_cayendo(objetos_cayendo_rojos, rojo)
        dibujar_objetos_cayendo(objetos_cayendo_azules, azul)
        dibujar_objetos_cayendo(objetos_cayendo_verdes, verde)

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar la velocidad del juego
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
