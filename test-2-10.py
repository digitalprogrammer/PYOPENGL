from core.base import Base


#check input
class Test(Base):
    def initialize(self):
        #return super().initialize()
        print("Initialization...")
    
    def update(self):
        #return super().update()
        #Typical usage
        if self.input.isKeyDown("space"):
            print("The 'space' key was just pressed down.")
        
        if self.input.isKeyPressed("right"):
            print("The 'right' key is currently being pressed.")

Test().run()
