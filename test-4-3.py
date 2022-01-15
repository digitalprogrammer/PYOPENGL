from math import sin

from numpy import arange

from core.base import Base
from core.camera import Camera
from core.mesh import Mesh
from core.renderer import Renderer
from core.scene import Scene
from geometry.geometry import Geometry
from material.lineMaterial import LineMaterial
from material.pointMaterial import PointMaterial


### The graphic is not showing up######
#render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 4])
        
        geometry = Geometry()
        posData = []
        for x in arange(-3.2, 3.2, 0.3):
            posData.append([x, sin(x), 0])

        
        r = [1, 0, 0]
        y = [1, 1, 0]
        g = [0, 0.25, 0]
        colorData = [r,g,y, y,g,g, y,g,r]
        geometry.addAttribute("vec3", "vertexColor", colorData)
        
            
        geometry.addAttribute("vec3", "vertexPosition", posData)
        geometry.countVertices()
        pointMaterial = PointMaterial({"baseColor":[1, 1, 0], "pointSize":10})
        pointMesh = Mesh(geometry, pointMaterial)
        lineMaterial = LineMaterial({"baseColor":[1, 0, 1], "lineWidth":4})
        lineMesh = Mesh(geometry, lineMaterial)
        self.scene.add(pointMesh)
        self.scene.add(lineMesh)
      
    
    def update(self): 
        self.renderer.render(self.scene, self.camera)

    
#inistantiate this class and run the program
Test(screenSize=[800, 600]).run()
