import arcade
from views.FightView import FightView
import pyglet

COLORS = [arcade.color.BLACK, arcade.color.RED_BROWN]

class IntroView(arcade.View):
    def __init__(self, window: pyglet.window.Window):
        super().__init__()
        self.window = window
        self.idx = 0

    def on_draw(self):
        self.idx +=1
        arcade.start_render()
        arcade.set_background_color(arcade.color.SLATE_GRAY)
        color =  COLORS[(self.idx // 80) % 2]
        arcade.draw_text("Brotal Combat", self.window.width/2, self.window.height/2,
                     color, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width/2, self.window.height/2-75,
                     arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = FightView(self.window)
        self.window.show_view(instructions_view)



