from core.base import Base
from core.camera import Camera
from core.mesh import Mesh
from core.renderer import Renderer
from core.scene import Scene
from core.texture import Texture
from extras.movementRig import MovementRig
from geometry.boxGeometry import BoxGeometry
from geometry.rectangleGeometry import RectangleGeometry
from geometry.sphereGeometry import SphereGeometry
from material.surfaceMaterial import SurfaceMaterial
from material.textureMaterial import TextureMaterial


#render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 4])
        
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.setPosition([0,1,4])
        
        
        skyGeometry = SphereGeometry(radius=50)
        earthTexture = Texture("images/sky-earth.png")
        skyMaterial = TextureMaterial(earthTexture)
        sky = Mesh(skyGeometry, skyMaterial)
        self.scene.add(sky)
        
        
        grassGeometry = RectangleGeometry(width=100, height=100)
        grassTexture = Texture("images/grass.png")
        grassMaterial = TextureMaterial(grassTexture, {"repeatUV":[50,50]})
        grass = Mesh(grassGeometry, grassMaterial)
        grass.rotateX(-3.14*0.5)
        self.scene.add(grass)


    
    def update(self):
        self.rig.update(self.input, self.deltaTime)
        self.renderer.render(self.scene, self.camera)

    
#inistantiate this class and run the program
Test(screenSize=[800, 600]).run()
