# Created by: Rehan and Paul
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main game.

from scene import *
import ui

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.title_position = Vector2()

        # add rink background
        self.background = SpriteNode('./assets/sprites/rink.JPG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 1)
