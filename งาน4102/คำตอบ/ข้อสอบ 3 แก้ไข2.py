from turtle import window_height
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
blend = True

index=0 
l=0
width =500
height =500
shine =50
theta, sign = 0,1
light = [GL_LIGHT0, GL_LIGHT1, GL_LIGHT2, GL_LIGHT3]
lightPosition0 = [50.0, 10.0, 0.0, 10.0]
lightPosition1 = [-50.0, -20.0, 50.0, 10.0]
lightPosition2 = [50.0, 50.0, -20.0, 10.0]
lightPosition3 = [-50.0, 50.0, -20.0, 10.0]
lightPosition=[lightPosition0,lightPosition1,lightPosition2,lightPosition3]




diffuse = [1.0,1.0,1.0,1.0]
specular = [1.0,1.0,1.0,1.0]
ambient = [1.0,1.0,1.0,1.0]
specularOFmaterial = [1.0,1.0,1.0,1.0]
diffuseOFmaterial = [1.0,1.0,1.0,1.0]
ambientOFmaterial = [0.0,1.0,0.5,1.0]



def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_BLEND)
    glBlendFunc(GL_ONE, GL_ZERO)
    glBlendFunc(GL_SRC_ALPHA, GL_DST_ALPHA)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    lightF()

def lightF():
    glMaterialfv(GL_FRONT , GL_DIFFUSE,diffuseOFmaterial)
    glMaterialfv(GL_FRONT , GL_AMBIENT,ambientOFmaterial)
    glMaterialfv(GL_FRONT , GL_SPECULAR,specularOFmaterial)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT3, GL_DIFFUSE, diffuse)
    
    
def display():
    global l,index
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(100.0,1.0,0.5,100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(12,1.2,1,0,1,0,0,1,0)
    glLightfv(light[index], GL_POSITION, lightPosition[index])
    glMaterialfv(GL_FRONT,GL_SHININESS, shine)
    

    
    glMaterialfv(GL_FRONT,GL_SHININESS, shine)
    rec = 10
    glPushMatrix()
    glRotatef(-50, 1, 0, 0)
    glRotatef(50, 0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-rec, rec)
    glVertex2f(-rec, -rec)
    glVertex2f(rec, -rec)
    glVertex2f(rec, rec)
    glEnd()
    
    glMaterialfv(GL_FRONT,GL_SHININESS, shine)
    rec = 10
    glRotatef(45, 0, 0, 0)
    glRotatef(45, 1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-rec, rec)
    glVertex2f(-rec, -rec)
    glVertex2f(rec, -rec)
    glVertex2f(rec, rec)
    glEnd()

    glPopMatrix()
    glutSwapBuffers()
    return 
    
    
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB| GLUT_DEPTH)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(width,height)
    glutInitWindowPosition(width,height)
    glutCreateWindow("work3")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(on_keyboard)
    glutMainLoop()
    return
    
    
def on_keyboard(key, x, y):
    global index
    global light 
    while True:
        if  key == b'1':
            index = 0
            glEnable(light[index])
            break
        if  key == b'2':
            index = 1
            glEnable(light[index])
            break
        if  key == b'3':
            index = 2
            glEnable(light[index])
            break
        if  key == b'4':
            index = 3
            glEnable(light[index])
            break
        if  key == b'5':
            glDisable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            glDisable(GL_LIGHT2)
            glDisable(GL_LIGHT3)
            break
      
        break
    print(index)
    glutPostRedisplay()

  
if __name__ == '__main__': main()
    
    
    
    
    
    
    

