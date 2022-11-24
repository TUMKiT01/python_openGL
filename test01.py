from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import shaders
import numpy as np


# VERTEX_SHADER = """

# #version 330

#     in vec4 position;
#     in vec3 color;
#     out vec3 newColor;
    
#     void main()
#     {
#     gl_Position = position;
#     newColor = color;
#     }

# """

# FRAGMENT_SHADER = """
# #version 330
#     in vec3 newColor;
#     out vec4 outColor;
    
#     void main()
#     {

#         outColor = vec4(newColor,1.0f);

#     }

# """
# shaderProgram = None

def initliaze():
#     global VERTEXT_SHADER
#     global FRAGMEN_SHADER
#     global shaderProgram

#     vertexshader = shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
#     fragmentshader = shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
#     shaderProgram = shaders.compileProgram(vertexshader, fragmentshader)


    triangles = [0.5, -0.5, 0.0,   1.0,.0,0.0,
                 0.0, 0.0, 0.0,   1.0,0.0,0.0,
                 0.5, 0.5, 0.0,    1.0,0.0,0.0]

    triangles = np.array(triangles, dtype=np.float32)

    # VBO = glGenBuffers(1)
    # glBindBuffer(GL_ARRAY_BUFFER, VBO)
    # glBufferData(GL_ARRAY_BUFFER, triangles.nbytes, triangles, GL_DYNAMIC_DRAW)

    # position = glGetAttribLocation(shaderProgram, 'position')
    # glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    # glEnableVertexAttribArray(position)
   
    # color = glGetAttribLocation(shaderProgram, 'color')
    # glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    # glEnableVertexAttribArray(color)


def render():
    # global shaderProgram
    # global angle
    # glUseProgram(shaderProgram)

    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT )
    #render program
    glDrawArrays(GL_TRIANGLES, 0, 3)
    
    glUseProgram(0)
    glutSwapBuffers()
   
def main():
   
    glutInit([])
    glutInitWindowSize(640, 480)
    glutCreateWindow("pyopengl with glut 2")
    initliaze()
    glutDisplayFunc(render)
    glutMainLoop()


if __name__ == '__main__':
    main()