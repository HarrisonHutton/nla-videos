from manim import *
config.background_color = "#191919"

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

        product = MathTex(r"b=Ax", font_size = 140, color = BLUE).shift(UP*1.8)
        to = MathTex(r"\to", font_size = 120, color = ORANGE).shift(LEFT*5.4)

        implication_1 = Tex(r"$b$", r" is a linear combination of", font_size = 80)
        implication_1.next_to(to, RIGHT)
        implication_2 = Tex(r" the columns of ", r"$A$.", font_size = 80)
        implication_2.next_to(to, DOWN, aligned_edge = LEFT)
        imp_group = VGroup(implication_1, implication_2)


        self.play(Write(product))
        self.play(Write(to))
        self.play(FadeIn(imp_group))
        self.wait()
