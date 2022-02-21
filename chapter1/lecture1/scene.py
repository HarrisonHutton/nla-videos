from ctypes import alignment
from manim import *
config.background_color = "#191919"

"""
Video thumbnail
"""
class Thumbnail(Scene):
    def construct(self):
        book = Text("Numerical Linear Algebra", font_size = 80)
        title = Text("Matrix-Vector Multiplication", font_size = 54)
        tex = MathTex(r"b=Ax", font_size = 280, color=GOLD).shift(DOWN*0.7)

        book.set_color_by_gradient(TEAL, GREEN)
        book.shift(UP*2.5)

        title.set_color_by_gradient(RED, ORANGE)
        title.shift(UP*1.4)

        self.add(book, title, tex)

"""
Matrix-vector multiplication videos
"""
class Goal(Scene):
    def construct(self):
        goal = Text("Goal:", font_size=80)\
            .to_corner(LEFT + UP)\
            .set_color_by_gradient("#11DA28", "#4FE560")
        self.play(Write(goal))
        self.wait(1.5)
        
        tex_template = TexTemplate()
        tex_template.add_to_preamble(
            r"\usepackage{amsfonts}"
        )

        x_vec = MathTex(r"x", r"\in \mathbb{C}^n", font_size = 144)
        x_vec.animate.shift(UP*2 + LEFT*4.8).scale(0.6)

        self.play(Write(x_vec))
        self.wait()
        self.play(Indicate(x_vec[0], color=BLUE))
        self.play(MoveToTarget(x_vec))

        # Not currently aligned correctly
        # Possibly add both x and A to VGroup and align them inside this
        a_mat = MathTex(r"A", r"\in \mathbb{C}^{m \times n}", font_size = 144)
        a_mat.animate.scale(0.6).next_to(x_vec, DOWN, aligned_edge=LEFT, buff=0.4).shift(LEFT*0.15)

        self.play(Write(a_mat))
        self.wait()
        self.play(Indicate(a_mat[0], color=BLUE))
        self.play(MoveToTarget(a_mat))
        self.wait()

        self.play(
            x_vec[0].animate.set_color(BLUE),
            a_mat[0].animate.set_color(BLUE)
        )
        self.wait()
        