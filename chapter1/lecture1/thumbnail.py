from manim import *

from background import set_background

"""
Video thumbnail
"""
class Thumbnail(Scene):
    def construct(self):
        set_background(self)
        book = Text("Numerical Linear Algebra", font_size = 80)
        title = Text("Matrix-Vector Multiplication", font_size = 54)
        tex = MathTex(r"b=Ax", font_size = 280, color=GOLD).shift(DOWN*0.7)

        book.set_color_by_gradient(TEAL, GREEN)
        book.shift(UP*2.5)

        title.set_color_by_gradient(RED, ORANGE)
        title.shift(UP*1.4)

        self.add(book, title, tex)