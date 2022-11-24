from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

#from sympy import true

theta, sign = 0.0, 1.0
r, g, b, a = 1., 1., 1., 1.
xx,yy,zz,ss = 0., 0., 0., 0.
w = 0.05
shine = 50
def setCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90.,1.,5.,90.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,8, 0, 0, 7, 0, 1, 0)

def setLight():
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [r, g, b, a])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [w*r, w*g, w*b, w*a])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [r, g, b, w*a])
    glMaterialfv(GL_FRONT, GL_SHININESS, shine)
    

def init():
    glClearColor(1.,1.,1.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    setCamera()
    setLight()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500,500)
    glutCreateWindow("Lighting")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(on_keyboard)
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_LIGHTING)
    glColor3f(r ,g, b)
    glPushMatrix()
    glLightfv(GL_LIGHT0, GL_POSITION, [xx,yy,zz,ss] )
    
    
    glTranslatef(10., 0., 0.)
    glDisable(GL_LIGHTING)
    glutSolidSphere(0.5,80,80)
    glEnable(GL_LIGHTING)
    
    glPopMatrix()
    glutSolidSphere (1, 100,100)#center sphere
    glPushMatrix()#right sphere
    glTranslatef(3,0,0)
    glutSolidSphere (1, 100,100)
    glPopMatrix()

    glPushMatrix() ## left sphere
    glTranslatef(-3,0,0)
    glutSolidSphere (1, 100,100)
    glPopMatrix()
    glutSwapBuffers()
    return

def on_keyboard(key, x, y):
    global xx,yy,zz,ss
    while True:
        if key == b'1':
            xx,yy,zz,ss = 0., 0., 0., 0.
        if key == b'2':
            xx,yy,zz,ss = 0.0, 0.0, 1., 0.
        if key == b'3':
            xx,yy,zz,ss = 0.0, 1., 0., 0.
        if key == b'4':
            xx,yy,zz,ss = 1, 0., 0., 0.
        if key == b'5':
            xx,yy,zz,ss = 1., 1., 0., 0.
        if key == b'6':
            xx,yy,zz,ss = 1., 1., 1., 0.
        break
    glutPostRedisplay()
if __name__ == '__main__': 
    main()
