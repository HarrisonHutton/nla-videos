from manim import *

def set_background(self):
    rect = FullScreenRectangle(fill_opacity = .4, stroke_width = 0).set_color([BLUE, PURPLE])
    self.add(rect)
    