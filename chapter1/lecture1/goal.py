from manim import *
# config.background_color = "#191919"

def set_background(self):
    rect = FullScreenRectangle(fill_opacity = .5, stroke_width = 0).set_color([BLUE, PURPLE])
    self.add(rect)

class Goal(Scene):
    def construct(self):
        set_background(self)
        goal = Text("Learning Goal:", font_size=80)\
            .to_corner(LEFT + UP)
            # .set_color_by_gradient("#11DA28", "#5AFF6D")
        self.play(Write(goal))
        self.wait(1.5)

        tex_template = TexTemplate()
        tex_template.add_to_preamble(
            r"\usepackage{amsfonts}"
        )

        product = MathTex(r"b=Ax", font_size = 140, color = RED).shift(UP*1.2)
        to = MathTex(r"\to", font_size = 120, color = YELLOW).shift(LEFT*5.4 + DOWN*0.5)

        implication_1 = Tex(r"$b$", r" is a linear combination of", font_size = 80)
        implication_1.next_to(to, RIGHT)
        implication_2 = Tex(r" the columns of ", r"$A$", r".", font_size = 80)
        implication_2.next_to(implication_1, DOWN, aligned_edge = LEFT)
        imp_group = VGroup(implication_1, implication_2)

        self.play(Write(product))
        self.play(Write(to))
        self.play(FadeIn(imp_group))
        self.wait()

        # Now make b and A from Tex formula float into their
        # positions in the implication.
        move_b = product[0][0].copy()
        og_b = implication_1[0].copy().set_color(RED)
        move_A = product[0][2].copy()
        og_A = implication_2[1].copy().set_color(RED)

        self.play(
            TransformFromCopy(move_b, og_b , path_arc = 80*DEGREES, run_time = 1.5),
            TransformFromCopy(move_A, og_A , path_arc = 80*DEGREES, run_time = 1.5)
        )
        self.wait(3)
