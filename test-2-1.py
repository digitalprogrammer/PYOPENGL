from core.base import Base


#Create a simple window with interactive close button
class Test(Base):
    def initialize(self):
        #return super().initialize()
        print("Initilialization...")
    
    def update(self):
        pass

Test().run()
