from math import cos, sin

from numpy.core.fromnumeric import var
from OpenGL.GL import *

from core.attribute import Attribute
from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform


#animate triangle moving across screen
class Test(Base):
    def initialize(self):
        #return super().initialize()
        print("Initializing...")

        #initialize program
        vsCode = """
        in vec3 position;
        uniform vec3 translation;
        void main()
        {
            vec3 pos = position + translation;
            gl_Position = vec4(pos, 1.0);
        }"""

        fsCode = """
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(baseColor, 1.0);
        }"""

        self.programRef = OpenGLUtils.initializeProgram(
            vsCode, fsCode)

        #render settings (optional)
        #specify color used when clearly
        glClearColor(0.0, 0.0, 0.0, 1.0)

        #set up vertex array object
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        #set up vertex attribute
        positionData = [
            [0.0, 0.2, 0.0],
            [0.2, -0.2, 0.0],
            [-0.2, -0.2, 0.0]
        ]

        self.vertexCount = len(positionData)
        positionAttribute = Attribute(
            "vec3", positionData)
        positionAttribute.associateVariable(
            self.programRef, "position")
        
        #set up uniforms
        self.translation = Uniform(
            "vec3", [-0.5, 0.0, 0.0])
        self.translation.locateVariable(
            self.programRef, "translation")
        self.baseColor = Uniform(
            "vec3", [1.0, 0.0, 0.0])
        self.baseColor.locateVariable(
            self.programRef, "baseColor")
    def update(self):
        #return super().update()
        #update data

        self.baseColor.data[0] = (sin(3 * (self.time)) + 1) * 0.5

        #render scene
        #reset color buffer with specified color
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.programRef)
        self.translation.uploadData()
        self.baseColor.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)


Test().run()
