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
class MatrixVectorMult(Scene):
    def construct(self):
        tex_template = TexTemplate()
        tex_template.add_to_preamble(
            r"\usepackage{amsfonts}"
        )

        tex = MathTex(r"x \in \mathbb{C}^n", font_size = 144)
        tex.animate.shift(UP*3 + LEFT*4.8).scale(0.6)
        self.play(Write(tex))

        # Add comma after C^n to make way for the next vector

        self.wait()

        self.play(MoveToTarget(tex))