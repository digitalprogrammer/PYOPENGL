import sys

import pygame
from pygame import display

from core.input import Input


class Base(object):
    def __init__(self, screenSize=[512,512]):
        #initilize all pygame modules
        pygame.init()
        #indicate rendering details
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        #initlize buffers to perform antialiasing
        pygame.display.gl_set_attribute(
            pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(
            pygame.GL_MULTISAMPLESAMPLES, 4)
        #use a core opengl profile for cross-plataform compatibility
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK,
            pygame.GL_CONTEXT_PROFILE_CORE)
        #create and display the window
        self.screen = pygame.display.set_mode(
            screenSize, displayFlags)
        #set the text that appears in the title bar of window
        pygame.display.set_caption("Caipora Window")
        #determine if main loop is active
        self.running = True
        #manage time related data and operations
        self.clock = pygame.time.Clock()
        #manage user
        self.input = Input()
        #number of seconds application has been running
        self.time = 0

        #implemented by extending classes
    def initialize(self):
        pass

    #implement by extending class
    def update(self):
        pass
    
    def run(self):
        #startup
        self.initialize()

        #main loop
        while self.running:
            #process input 
            self.input.update()
            if self.input.quit:
                self.running = False
            #seconds since iteration of run loop
            self.deltaTime = self.clock.get_time() / 1000
            #increment time application has been running
            self.time += self.deltaTime

            #update
            self.update()

            #render - render image on screen
            pygame.display.flip()

            #pause if necessary to achieve 60 FPS
            self.clock.tick(60)
        #shutdown
        pygame.quit()
        sys.exit()
