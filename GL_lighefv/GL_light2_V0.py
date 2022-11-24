from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
r, g, b = 1.0, 1.0, 1.0
w = 0.8
name = b'Lighting'
dif_color = [r, g, b, 1.]
amb_color = [w*r, w*g, w*b, 1]
spec_color = [1.0, 0., 0., 1.]
lightZeroPosition = [0., -10., 0., 0.]
lightZeroColor = [0.8, 1.0, 0.8, 1.0]  # green tinged
shininess = [50.0]
def setCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,10, 0,0,0, 0,1,0)

def setLight():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [10, 0, 0, 0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [r, g, b, 1.0])
    glMaterialfv(GL_FRONT,GL_DIFFUSE,[0, g, 0, 1.0])
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, [r*0.7, g*0.7, b*0.7, 1.0])    
    glMaterialfv(GL_FRONT,GL_AMBIENT,[0, g*0.25, 0, 0.0])
    

    #glLightfv(GL_LIGHT0, GL_AMBIENT, [r*0.7, g*0.7, b*0.7, 1.0])    
    
    
    
    #glLightfv(GL_LIGHT0, GL_SPECULAR, lightZeroColor)
    #glMaterialfv(GL_FRONT, GL_SPECULAR, spec_color)
    #glMaterialfv(GL_FRONT,GL_DIFFUSE,dif_color)
    

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
    glutCreateWindow(name)
    init()
    glutDisplayFunc(display)
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.,1., 0.)
    glPushMatrix()
    glutSolidSphere(2,80,80)
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()
