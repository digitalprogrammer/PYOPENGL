from math import fsum

from core.base import Base
from core.camera import Camera
from core.mesh import Mesh
from core.renderer import Renderer
from core.scene import Scene
from geometry.boxGeometry import BoxGeometry
from geometry.sphereGeometry import SphereGeometry
from material.material import Material
from material.surfaceMaterial import SurfaceMaterial


#render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 7])

        geometry = SphereGeometry(radius=3)
        vsCode ="""
        in vec3 vertexPosition;
        out vec3 position;
        uniform mat4 modelMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;

        void main()
        {
            vec4 pos = vec4(vertexPosition, 1.0);
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * pos;
            position = vertexPosition;
        }"""

        fsCode = """
        in vec3 position;
        out vec4 fragColor;

        void main()
        {
            vec3 color = mod(position, 1.0);
            fragColor = vec4(color, 1.0);
        }"""

        material = Material(vsCode, fsCode)
        material.locateUniforms()
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)
        
        
    
    def update(self):
        self.mesh.rotateY(0.00514)
        self.mesh.rotateX(0.00337)
        self.renderer.render(self.scene, self.camera)

    
#inistantiate this class and run the program
Test(screenSize=[800, 600]).run()
