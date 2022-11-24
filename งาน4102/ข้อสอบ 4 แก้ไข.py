from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
l1,l2,l3,l4 = 10.,0.,10.,0.
t1,t2,t3 = 8., 1., 5.
d = 0
theta, sign = 0.0, 1.0
r, g, b, a = 1., 0., 0., 0.
w = 1
shine = 100
def setCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90.,1.,5.,90.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10,-10,25, 0, 0, 5, 0, 1, 50)

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
    glutInitWindowSize(500,500)
    glutCreateWindow("Lighting")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(on_keyboard)
    glutIdleFunc(MyIdle)
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glEnable(GL_LIGHTING)
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(theta, 0.2, 0.2, 0.8)
    glLightfv(GL_LIGHT0, GL_POSITION, [l1,l2,l3,l4] )
    glTranslatef(t1,t2,t3)
    glDisable(GL_LIGHTING)
    glutSolidSphere(1,50,100)
    glEnable(GL_LIGHTING)
    glPopMatrix()
    
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(25, 0, 0, 1)
    gluCylinder(gluNewQuadric(), 10, 10, 14, 50, 50)
    glPopMatrix()

    glutSwapBuffers()  
    return
def on_keyboard(key, x, y):
    global l1,l2,d,t1,t2,t3
    while True:
        if key == b'\x1b':
            sys.exit()
            break
        if key == b'f':
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)
            break
        if key == b'o':
            glEnable(GL_LIGHTING)
            glEnable(GL_LIGHT0)
            break
        if key == b't':
            l1,l2,d,t1,t2,t3 = 0.,10.,theta,1., 11., 5.
            break
        if key == b'b':
            l1,l2,d,t1,t2,t3 = 10.,0.,0,8., 1., 5.
            break
        if key == b'1':
            setCamera()
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(-16,16,-10,10,-9,30)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(10,-10,25, 0, 0, 5, 0, 1, 50)
          
            break
        if key == b'2':
            setCamera()
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(90.,1.,2.,90.)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(10,-10,25, 0, 0, 5, 0, 1, 50)
            
            break
        if key == b'3':
            setCamera()
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glFrustum(-3, 3, -3, 3,3,50)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(5,18,25, 1, 1, 1, 0, 5,50)
            break
    
    print(key)
    glutPostRedisplay()



def MyIdle():
    global theta, sign
    theta = theta + (0.1*sign)
    glutPostRedisplay()

if __name__ == '__main__': 
    main()