import pygame
import math

# Inicializar PyGame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Polígonos Regulares con PyGame")
font = pygame.font.SysFont("Arial", 20)

def draw_polygon(surface, n_sides, center, radius, color, label):
    angle = 2 * math.pi / n_sides
    points = [
        (
            center[0] + radius * math.cos(i * angle - math.pi / 2),
            center[1] + radius * math.sin(i * angle - math.pi / 2)
        )
        for i in range(n_sides)
    ]
    pygame.draw.polygon(surface, color, points, 2)
    text = font.render(label, True, (255, 255, 255))
    surface.blit(text, (center[0] - text.get_width() // 2, center[1] + radius + 10))

# Lista de polígonos
polygons = [("Triángulo", 3), ("Cuadrado", 4), ("Pentágono", 5), ("Hexágono", 6), ("Heptágono", 7)]

running = True
while running:
    screen.fill((0, 0, 0))
    for i, (name, sides) in enumerate(polygons):
        x = 150 + (i % 5) * 130
        y = 300
        draw_polygon(screen, sides, (x, y), 50, (0, 200, 255), name)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
