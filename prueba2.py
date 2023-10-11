import pygame
import sys
from logica1 import main  

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla principal
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Niveles")
main_font = pygame.font.SysFont("cambria", 35)
background = pygame.image.load("fondo.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Clase para representar un botón
class Button:
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update_image(self, image):
        self.image = pygame.transform.scale(image, self)

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        return self.rect.collidepoint(position)
def iniciar_juego():
    # Cargar imágenes y escalarlas para los botones
    boton = pygame.image.load("botonrojo.png")
    tamanoboton = pygame.transform.scale(boton, (150, 200))

    # Crear los botones
    button1 = Button(tamanoboton, 250, 200, "Nivel 1")
    button2 = Button(tamanoboton, 650, 200, "Nivel 2")
    button3 = Button(tamanoboton, 1030, 200, "Nivel 3")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.check_for_input(pygame.mouse.get_pos()):
                    main()

        # Actualizar la pantalla principal
        screen.blit(background, [0, 0])
        button1.update()
        button2.update()
        button3.update()
        pygame.display.update()
        
if __name__ == "__main__":
    # Inicializar Pygame
    pygame.init()

    # Llamar a la función para iniciar el juego
    iniciar_juego()