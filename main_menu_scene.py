# Created by: Paul and Rehan
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from help_scene import *
from options_scene import *
from game_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.title_position = Vector2()

        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/background.JPG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 1)

        # title
        title_position = Vector2()
        title_position.x = 384
        title_position.y = 800
        self.title = SpriteNode('./assets/sprites/title.PNG',
                                      parent = self,
                                      position = title_position,
                                      scale = 0.3)

        # help button
        help_position = Vector2()
        help_position.x = 384
        help_position.y = 305.55
        self.help = SpriteNode('./assets/sprites/help.PNG',
                                      parent = self,
                                      position = help_position,
                                      scale = 0.5)

        # options button
        options_position = Vector2()
        options_position.x = 384
        options_position.y = 100
        self.options = SpriteNode('./assets/sprites/options.PNG',
                                      parent = self,
                                      position = options_position,
                                      scale = 0.5)

        # start button
        self.start = SpriteNode('./assets/sprites/start.PNG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.5)

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

        # if options button is pressed, go to options scene
        if self.options.frame.contains_point(touch.location):
            self.present_modal_scene(OptionsScene())

        # if help button is pressed, go to help scene
        if self.help.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())

        # if start button is pressed, go to game scene
        if self.start.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())

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
    
