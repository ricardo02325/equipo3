import pygame
import sys
from nivel1 import juego

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana principal
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))

# Cargar recursos de sonido
# sonido = pygame.mixer.Sound("corrido.mp3")

# Colores RGB
color_blanco = (255, 255, 255)

# Establecer el reloj principal
relojPrincipal = pygame.time.Clock()

# Cargar fondo y escalar a las dimensiones de la ventana
fondo = pygame.image.load("fondo.png").convert()
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Variable para controlar el clic del ratón
clic = False

# Recursos para botones
boton1 = pygame.image.load("botonrojo.png")
boton1.set_colorkey(color_blanco)  # Establecer el color blanco como el color clave para hacerlo transparente
boton1 = pygame.transform.scale(boton1, (200, 180))

# Variable para controlar si estamos en el juego o en el menú principal
in_game = False

# Función para dibujar texto en la pantalla
def dibujar_texto(texto, fuente, color, superficie, x, y):
    texto_obj = fuente.render(texto, 1, color)
    rectangulo_texto = texto_obj.get_rect()
    rectangulo_texto.topleft = (x, y)
    superficie.blit(texto_obj, rectangulo_texto)

# Función para abrir la ventana del juego
def abrir_ventana_juego():
    tiempo_inicial = pygame.time.get_ticks()  # Obtener el tiempo inicial
    juego(tiempo_inicial)

# Función para el menú principal
def menu_principal():
    global clic, in_game  # Declarar variables como globales
    while True:
        ventana.blit(fondo, (0, 0))

        mx, my = pygame.mouse.get_pos()

        if not in_game:
            # Dibujar el botón
            ventana.blit(boton1, (550, 540))
            
            # Obtener el rectángulo del botón
            boton1_rect = pygame.Rect(550, 540, 200, 180)
    
            # Verificar si el ratón está sobre el botón
            if boton1_rect.collidepoint((mx, my)):
                if clic:
                    in_game = True
                    clic = False

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

        pygame.display.update()
        relojPrincipal.tick(60)

if __name__ == "__main__":
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if in_game:
            abrir_ventana_juego()
            in_game = False
        else:
            ventana.fill((0, 0, 0))
            menu_principal()
