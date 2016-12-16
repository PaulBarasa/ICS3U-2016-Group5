# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the options scene.

from scene import *
import ui

from main_menu_scene import *

class OptionsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        center_of_screen = self.size/2

        # add background
        self.background = SpriteNode('./assets/sprites/background.JPG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 1)

        # add back button
        back_position = self.size
        back_position.x = 100
        back_position.y = back_position.y - 100
        self.left = SpriteNode('./assets/sprites/left.PNG',
                                       parent = self,
                                       position = back_position,
                                       scale = 0.1)

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

        # if back button is pressed, go to main scene
        if self.left.frame.contains_point(touch.location):
            self.dismiss_modal_scene()

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
