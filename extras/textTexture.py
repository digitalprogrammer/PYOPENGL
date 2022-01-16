import pygame
from core.texture import Texture


class TextTexture(Texture):
    def __init__(self, text="Enter text here!", systemFontName="Arial",
                fontFileName=None, fontSize=24, fontColor=[0,0,0],
                backgroundColor=[255,255,255], transparent=False, 
                imageWidth=None, imageHeight=None, alignHorizontal=0.0,
                alignVertical=0.0, imageBorderWidth=0, imageBorderColor=[0,0,0]):
                super().__init__()
                
                #default font
                font = pygame.font.SysFont(systemFontName, fontSize)
                #can override by loading font file
                if fontFileName is not None:
                    font = pygame.font.Font(fontFileName, fontSize)
                
                #render text to (antialiased) surface
                fontSurface = font.render(text, True, fontColor)

                #determine size of rendered text for aligment purpose
                (textWidth, textHeight) = font.size(text)

                #if image dimensions are not specified use font surface size default

                if imageWidth is None:
                    imageWidth = textWidth
                if imageHeight is None:
                    imageHeight = textHeight

                #create surface to store image of text (with transparent
                # channel by default) 
                self.surface = pygame.Surface((imageWidth, imageHeight), pygame.SRCALPHA)

                #background color used when not transparent i not transparent
                self.surface.fill(backgroundColor)

                #alignHorizontal, alignVertical are percentages, 
                #measured from top-left corner
                cornerPoint = (alignHorizontal * (imageWidth-textWidth),
                                alignVertical * (imageHeight-textHeight))
                
                destinationRectangle = fontSurface.get_rect(topleft=cornerPoint)

                #optional: add border
                if imageBorderWidth > 0:
                    pygame.draw.rect(self.surface, imageBorderColor,
                    [0,0, imageWidth, imageHeight], imageBorderWidth)

                #apply fontSurface to correct position on final surface
                self.surface.blit(fontSurface, destinationRectangle)
                self.uploadData()
