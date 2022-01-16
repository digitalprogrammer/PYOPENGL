from core.base import Base
from core.camera import Camera
from core.mesh import Mesh
from core.renderer import Renderer
from core.scene import Scene
from core.texture import Texture
from effects.colorReduceEffect import ColorReducerEffect
from effects.invertEffect import InvertEffect
from effects.pixelateEffect import PixelateEffect
from effects.tintEffect import TintEffect
from effects.vignetteEffect import VignetteEffect
from extras.movementRig import MovementRig
from extras.postprocessor import Postprocessor
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

        sphereGeometry = SphereGeometry()
        sphereTexture = Texture("images/grid.png")
        sphereMaterial = TextureMaterial(sphereTexture)
        self.sphere = Mesh(sphereGeometry, sphereMaterial)
        self.sphere.setPosition([0,1,0])
        self.scene.add(self.sphere)

        self.postprocessor = Postprocessor(self.renderer, self.scene, self.camera)
        
        #Tint effect
        #self.postprocessor.addEffect(TintEffect(tintColor=[1,0,0]))
        
        #Invert effect
        #self.postprocessor.addEffect(InvertEffect())
        
        #Pixalate Effect
        #self.postprocessor.addEffect(PixelateEffect())

        #vignette Effect
        #self.postprocessor.addEffect(VignetteEffect())

        #reduce color effect
        self.postprocessor.addEffect(ColorReducerEffect())



    
    def update(self):
        self.rig.update(self.input, self.deltaTime)
        self.postprocessor.render()

    
#inistantiate this class and run the program
Test(screenSize=[800, 600]).run()
