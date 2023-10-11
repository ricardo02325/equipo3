import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Levels")
main_font = pygame.font.SysFont("cambria", 50)
background = pygame.image.load("fondo.png").convert()

class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		

	def update_image(self,image):
		self.image = pygame.transform.scale(image, self)	

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button pressed")
	
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")

boton = pygame.image.load("botonrojo.png")
botonPress = pygame.image.load("BotonRojoPress.jpg")
tamanoboton = pygame.transform.scale(boton, (200, 100))

button1 = Button(tamanoboton, 200, 200, "Nivel 1")
button2 = Button(tamanoboton, 540, 200, "Nivel 2")
button3 = Button(tamanoboton, 880, 200, "Nivel 3")
botonDifFacil = Button(tamanoboton, 400, 500, "Facil")
botonDifDificil = Button(tamanoboton, 600, 500, "Dificil")


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button1.checkForInput(pygame.mouse.get_pos())
			button2.checkForInput(pygame.mouse.get_pos())
			button3.checkForInput(pygame.mouse.get_pos())
			botonDifFacil.checkForInput(pygame.mouse.get_pos())
			botonDifDificil.checkForInput(pygame.mouse.get_pos())
	screen.blit(background, [0,0])

	button1.update()
	button1.changeColor(pygame.mouse.get_pos())
	button2.update()
	button2.changeColor(pygame.mouse.get_pos())
	button3.update()
	button3.changeColor(pygame.mouse.get_pos())
	botonDifFacil.update()
	botonDifFacil.changeColor(pygame.mouse.get_pos())
	

	pygame.display.update()