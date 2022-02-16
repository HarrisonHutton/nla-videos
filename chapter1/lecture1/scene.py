from manim import *
config.background_color = "#191919"

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