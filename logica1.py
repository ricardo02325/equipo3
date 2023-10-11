import pygame
import sys
import random
from ganar import ganar

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Equipo 3")
background = pygame.image.load("nivel1.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Cargar imágenes para el jugador y los objetos que caen
player_image = pygame.image.load("personaje1.png")
player_image = pygame.transform.scale(player_image, (150, 140))

red_object_image = pygame.image.load("manzana.png")
red_object_image = pygame.transform.scale(red_object_image, (40, 40))

blue_object_image = pygame.image.load("pescao.png")
blue_object_image = pygame.transform.scale(blue_object_image, (40, 40))

green_object_image = pygame.image.load("hueso.png")
green_object_image = pygame.transform.scale(green_object_image, (40, 40))

yellow_object_image = pygame.image.load("lata_refresco.png")
yellow_object_image = pygame.transform.scale(yellow_object_image, (40, 40))

purple_object_image = pygame.image.load("hoja_de_periodico.png")
purple_object_image = pygame.transform.scale(purple_object_image, (40, 40))

orange_object_image = pygame.image.load("botella_de_plastico.png")
orange_object_image = pygame.transform.scale(orange_object_image, (40, 40))

pink_object_image = pygame.image.load("cd.png")
pink_object_image = pygame.transform.scale(pink_object_image, (40, 40))

cyan_object_image = pygame.image.load("foco.png")
cyan_object_image = pygame.transform.scale(cyan_object_image, (40, 40))

brown_object_image = pygame.image.load("telefono.png")
brown_object_image = pygame.transform.scale(brown_object_image, (40, 40))

gray_object_image = pygame.image.load("colilla_de _cigarro.png")
gray_object_image = pygame.transform.scale(gray_object_image, (40, 40))

# Variable para poder poner el tiempo en reversa
auxiliar = 0

# Puntos
puntos = 0

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Crear una fuente para el texto
fuente = pygame.font.SysFont(None, 35)

# Definir el objeto móvil
player_rect = player_image.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 20
player_speed = 5

# Listas para almacenar objetos que caen
falling_objects_red = []
falling_objects_blue = []
falling_objects_green = []
falling_objects_yellow = []
falling_objects_purple = []
falling_objects_orange = []
falling_objects_pink = []
falling_objects_cyan = []
falling_objects_brown = []
falling_objects_gray = []

def draw_falling_objects(objects, image):
    for obj in objects:
        screen.blit(image, obj)

def main():
    global player_rect, auxiliar, puntos  # Declarar player_rect, auxiliar y puntos como globales

    running = True

    tiempo_inicial = pygame.time.get_ticks()  # Obtener el tiempo inicial

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calcular el tiempo restante
        tiempo_max = 120  # Tiempo máximo en segundos
        tiempo_juego = (pygame.time.get_ticks() - tiempo_inicial) // 1000
        tiempo = tiempo_max - tiempo_juego

        if auxiliar != tiempo:
            auxiliar = tiempo

        if puntos < 0:
            puntos = 0

        # Mover el objeto móvil
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += player_speed

        # Generar objetos que caen aleatoriamente
        if random.randint(1, 100) < 3:
            obj_width = 20
            obj_height = 20
            obj_x = random.randint(0, WIDTH - obj_width)
            obj_y = 0
            rand_num = random.randint(1, 10)
            if rand_num == 1:
                falling_objects_red.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 2:
                falling_objects_blue.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 3:
                falling_objects_green.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 4:
                falling_objects_yellow.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 5:
                falling_objects_purple.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 6:
                falling_objects_orange.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 7:
                falling_objects_pink.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 8:
                falling_objects_cyan.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 9:
                falling_objects_brown.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))
            elif rand_num == 10:
                falling_objects_gray.append(pygame.Rect(obj_x, obj_y, obj_width, obj_height))

        # Mover y eliminar objetos que caen
        for obj in falling_objects_red:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_red.remove(obj)

        for obj in falling_objects_blue:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_blue.remove(obj)

        for obj in falling_objects_green:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_green.remove(obj)

        for obj in falling_objects_yellow:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_yellow.remove(obj)

        for obj in falling_objects_purple:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_purple.remove(obj)

        for obj in falling_objects_orange:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_orange.remove(obj)

        for obj in falling_objects_pink:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_pink.remove(obj)

        for obj in falling_objects_cyan:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_cyan.remove(obj)

        for obj in falling_objects_brown:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_brown.remove(obj)

        for obj in falling_objects_gray:
            obj.y += 5
            if obj.y > HEIGHT:
                falling_objects_gray.remove(obj)

        # Detectar colisiones con objetos rojos
        for obj in falling_objects_red:
            if player_rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos += 1
                falling_objects_red.remove(obj)

        # Detectar colisiones con objetos azules
        for obj in falling_objects_blue:
            if player_rect.colliderect(obj):
                print("¡Colisión con objeto azul!")
                puntos += 1
                falling_objects_blue.remove(obj)

        # Detectar colisiones con objetos verdes
        for obj in falling_objects_green:
            if player_rect.colliderect(obj):
                print("¡Colisión con objeto verde!")
                puntos += 1
                falling_objects_green.remove(obj)

        for obj in falling_objects_yellow:
            if player_rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                falling_objects_yellow.remove(obj)

        for obj in falling_objects_purple:
            if player_rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                falling_objects_purple.remove(obj)

        for obj in falling_objects_orange:
            if player_rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                falling_objects_orange.remove(obj)

        for obj in falling_objects_pink:
            if player_rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                falling_objects_pink.remove(obj)

        for obj in falling_objects_cyan:
            if player_rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                falling_objects_cyan.remove(obj)

        for obj in falling_objects_brown:
            if player_rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                falling_objects_brown.remove(obj)

        for obj in falling_objects_gray:
            if player_rect.colliderect(obj):
                print("¡Colisión con objeto rojo!")
                puntos -= 1
                falling_objects_gray.remove(obj)
        
        # Limpiar la pantalla
        screen.fill((0, 0, 0))

        # Dibujar el objeto móvil y los objetos que caen
        screen.blit(player_image, player_rect)
        draw_falling_objects(falling_objects_red, red_object_image)
        draw_falling_objects(falling_objects_blue, blue_object_image)
        draw_falling_objects(falling_objects_green, green_object_image)
        draw_falling_objects(falling_objects_yellow, yellow_object_image)
        draw_falling_objects(falling_objects_purple, purple_object_image)
        draw_falling_objects(falling_objects_orange, orange_object_image)
        draw_falling_objects(falling_objects_pink, pink_object_image)
        draw_falling_objects(falling_objects_cyan, cyan_object_image)
        draw_falling_objects(falling_objects_brown, brown_object_image)
        draw_falling_objects(falling_objects_gray, gray_object_image)

        # Pon el tiempo en pantalla
        contador = fuente.render("Tiempo: " + str(tiempo), 0, (255, 255, 255))
        screen.blit(contador, (10, 10))

        # Mostrar puntos en pantalla
        puntos_text = fuente.render("Puntos: " + str(puntos) + " /5", 0, (255, 255, 255))
        screen.blit(puntos_text, (WIDTH - 150, 10))

        # Verificar si se han alcanzado 5 puntos
        if puntos >= 5:
            ganar() 

        # Actualizar la pantalla
        pygame.display.update()

        # Controlar la velocidad del juego
        relojPrincipal.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()