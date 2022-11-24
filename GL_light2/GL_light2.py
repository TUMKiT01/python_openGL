from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

#from sympy import true

theta, sign = 0.0, 1.0
r, g, b, a = 1., 1., 1., 1.
w = 0.1
flag = True
shine = 50
def setCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90.,1.,5.,90.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,13, 0, 0, 5, 0, 1, 0)

def setLight():
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [r, g, b, a])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [w*r, w*g, w*b, w*a])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [r, g, b, w*a])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [r, g, b, a])
    glMaterialfv(GL_FRONT, GL_SHININESS, shine)
    

def init():
    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    setCamera()
    setLight()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow("Lighting")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(on_keyboard)
    glutIdleFunc(MyIdle)
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    if (flag):
        glEnable(GL_LIGHTING)
    else:
        glDisable(GL_LIGHTING)

    glColor3f(r ,g, b)
    glPushMatrix()
    glRotatef(theta, 0, 1, 0)
    glLightfv(GL_LIGHT0, GL_POSITION, [10., 0., 0., 0.] )
    glTranslatef(10., 0., 0.)
    if (flag):
        glDisable(GL_LIGHTING)
        glutSolidSphere(0.5,80,80)
        glEnable(GL_LIGHTING)
    else:
        glutSolidSphere(0.5,80,80)

    glPopMatrix()
    glColor3f(r ,0.,0.)
    glMaterialfv(GL_FRONT,GL_DIFFUSE, [r, 0, 0, a])
    glMaterialfv(GL_FRONT,GL_AMBIENT, [w*r, 0, 0, w*a])
    glPushMatrix()
    glutSolidSphere(2,80,80)
    glPopMatrix()

    glColor3f(0.,g,0.)
    glMaterialfv(GL_FRONT,GL_DIFFUSE, [0, g, 0, a])
    glMaterialfv(GL_FRONT,GL_AMBIENT, [0, w*g, 0, w*a])
    glPushMatrix()
    glTranslatef(-6,0,0)
    glutSolidSphere(2,80,80)
    glPopMatrix()

    glColor3f(0.,0.,b)
    glMaterialfv(GL_FRONT,GL_DIFFUSE, [0, 0, b, a])
    glMaterialfv(GL_FRONT,GL_AMBIENT, [0, 0, w*b, w*a])
    glPushMatrix()
    glTranslatef(6,0,0)
    glutSolidSphere(2,80,80)
    glPopMatrix()
    glutSwapBuffers()
    return



def on_keyboard(key, x, y):
    global flag
    if key == b'\x1b':
        sys.exit()
    elif key == b'a':
        flag = not flag
    print(flag)
    glutPostRedisplay()

def MyIdle():
    global theta, sign
    theta = theta + (0.1*sign)
    glutPostRedisplay()

if __name__ == '__main__': 
    main()
