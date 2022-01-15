from core.base import Base
from core.camera import Camera
from core.mesh import Mesh
from core.renderer import Renderer
from core.scene import Scene
from geometry.boxGeometry import BoxGeometry
from geometry.geometry import Geometry
from material.surfaceMaterial import SurfaceMaterial


#render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 1])
        
        geometry = Geometry()
        p0 = [-0.1, 0.1, 0.0]
        p1 = [0.0, 0.0, 0.0]
        p2 = [0.1, 0.1, 0.0]
        p3 = [-0.2, -0.2, 0.0]
        p4 = [0.2, -0.2, 0.0]
        posData = [p0,p3,p1, p1,p3,p4, p1,p4,p2]
        geometry.addAttribute("vec3", "vertexPosition", posData)
        r = [1, 0, 0]
        y = [1, 1, 0]
        g = [0, 0.25, 0]
        colData = [r,g,y, y,g,g, y,g,r]
        geometry.addAttribute("vec3", "vertexColor", colData)
        geometry.countVertices()
        material = SurfaceMaterial({"useVertexColors":True})
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)
    
    def update(self):
        #self.mesh.rotateY(0.0514)
        #self.mesh.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)

    
#inistantiate this class and run the program
Test(screenSize=[800, 600]).run()
