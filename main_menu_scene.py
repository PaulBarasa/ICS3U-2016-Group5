# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *

import ui

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.title_position = Vector2()

        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/blue.JPG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.30)

        # title
        title_position = Vector2()
        title_position.x = 384
        title_position.y = 850
        self.title = LabelNode(text = 'Hockey Shootout',
                                      font=('Futura', 120),
                                      color = '#ffffff',
                                      parent = self,
                                      scale = 0.75,
                                      position = title_position)

        # start button
        self.start = SpriteNode('./assets/sprites/start.PNG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.75)
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
