from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
name = b'Transformation_chapter'
# parameters of GL display
import numpy as np

xmin, ymin = 0.5, 0.5
xmax, ymax = 1.5, 1.5
left, right, bottom, top = -5., 5., -5., 5.
tx, ty = 0., 0.
sc = 1.
theta = 0
obj = np.array([[xmin, ymin, 1], [xmin, ymax, 1], [xmax, ymax, 1], [xmax, ymin, 1]], dtype=float)
step = 0.1
def InitGL():
    glClearColor(1.,1.,1.,0.)
    glColor3f(0.0, 0.0, 0.0)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glTranslatef(tx, ty, 0)
    glScalef(sc,sc,0)
    glBegin(GL_QUADS)
    for p in obj:
        glVertex2f(p[0], p[1])
    glEnd()
    glPopMatrix()

    glFlush()
    return

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)
    InitGL()
    glutDisplayFunc(display)
    glutKeyboardFunc(On_keyboard)

    glutMainLoop()
    return

def On_keyboard(key, x, y):
    global tx, ty, sc, theta
    while True:
        if key == b'\x1b':
            sys.exit()
        if key == b'l':
            tx = tx - 0.1       
            break
        if key == b'r':
            tx = tx + 0.1       
            break
        if key == b'b':
            ty = ty - 0.1         
            break
        if key == b't':
            ty = ty + 0.1            
            break
        if key == b'i':
            sc = sc + 0.1            
            break
        if key == b'd':
            sc = sc - 0.1            
            break
        break
    glutPostRedisplay()



if __name__ == '__main__': main()
