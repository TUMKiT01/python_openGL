from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
name = b'ball_glut'
flag = True
w0 = 0.85
w1 = 0.64

def initialization():
    glClearColor(0., 0., 0., 0.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc(GL_ONE, GL_ZERO)
    glBlendFunc(GL_SRC_ALPHA, GL_DST_ALPHA)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(-4,4,-4,4,-4,4)
    glFrustum(-4, 4, -4, 4, 5, 10)
    #gluPerspective(90., 1., 5., 45.)    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 3, 0, 1, 0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)
    initialization()
    glutDisplayFunc(display)
    glutKeyboardFunc(on_keyboard)
    glutMainLoop()
    return


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if flag:
        draw_circle([0.0, 0.0, 1.0, w0],  -1.0)
        draw_circle([1.0, 0.0, 0.0, w1],  1.0)
    else:
        draw_circle([1.0, 0.0, 0.0, w0], 1.0)
        draw_circle([0.0, 0.0, 1.0, w1],  -1.0)
    glutSwapBuffers()
    return


def draw_circle(color, tx):
    glPushMatrix()
    glColor4fv(color)
    glTranslatef(tx, 0.0, 0.0)
    glutSolidSphere(2, 80, 80)
    glPopMatrix()


def on_keyboard(key, x, y):
    global flag
    while True:
        if key == b'\x1b':
            sys.exit()
        if key == b'f':
            if (flag):
                flag = False
            else:
                flag = True    
            print(flag)
        break
    glutPostRedisplay()
   

if __name__ == '__main__': main()