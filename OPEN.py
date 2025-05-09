from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Configuración de la ventana
width, height = 800, 600
polygons = [("Triángulo", 3), ("Cuadrado", 4), ("Pentágono", 5), ("Hexágono", 6), ("Heptágono", 7)]

def draw_text(x, y, text):
    glColor3f(1.0, 1.0, 1.0)  # Color blanco
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

def draw_polygon(n_sides, cx, cy, radius):
    glBegin(GL_LINE_LOOP)
    for i in range(n_sides):
        angle = 2 * math.pi * i / n_sides - math.pi / 2
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    start_x = -0.8
    spacing = 0.4
    radius = 0.15

    for i, (name, sides) in enumerate(polygons):
        cx = start_x + i * spacing
        cy = 0.2
        glColor3f(0.0, 1.0, 1.0)  # Color cian para los polígonos
        draw_polygon(sides, cx, cy, radius)

        # Dibujar texto debajo del polígono
        text_width = len(name) * 0.01  # Estimación del ancho del texto
        draw_text(cx - text_width, cy - radius - 0.1, name)

    glFlush()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Poligonos Regulares con PyOpenGL")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutMainLoop()

main()
