from manim import *

class Resolviendo(Scene):
    def construct(self):
        title = Text("Resolviendo para a y b", font="Times New Roman", font_size=40).to_edge(UP)
        caption = Text("Sustituimos valores", font_size=30).next_to(title, DOWN)
        caption2 = MathTex(r"x = 4").next_to(caption, DOWN)
        caption21 = MathTex(r"f(x) = 10").next_to(caption2, DOWN)
        caption2.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        caption21.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        caption3 = MathTex(r"10 = a(4)^2 + b(4) + 50").next_to(title, DOWN)
        caption3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        caption4 = MathTex(r"10 = 16a + 4b + 50").next_to(caption3, DOWN)
        caption4.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        caption5 = Text("Restamos 50 en ambos lados", font_size=30).next_to(caption4, DOWN)
        caption6 = MathTex(r"-40 = 16a + 4b").next_to(caption5, DOWN)
        caption6.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        caption7 = Text("Sustituimos", font_size=30).next_to(title, DOWN)
        caption8 = MathTex(r"-40 = 16a + 4(-8a)").next_to(caption7, DOWN)
        caption8.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        caption9 = MathTex(r"-40 = 16a - 32a").next_to(caption8, DOWN)
        caption9.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        caption10 = MathTex(r"-40 = -16a").next_to(caption9, DOWN)
        caption10.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        caption11 = MathTex(r"a = \frac{5}{2}").next_to(caption10, DOWN)
        caption11.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        caption12 = Text("Calculamos b", font_size=30).next_to(title, DOWN)
        caption13 = MathTex(r"b = -8(\frac{5}{2})").next_to(caption12, DOWN)
        caption13.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        caption14 = MathTex(r"b = -20").next_to(caption13, DOWN)
        caption14.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.play(Write(title), run_time=3)
        self.wait(1)
        self.play(Write(caption), run_time=3)
        self.wait(1)
        self.play(Write(caption2), run_time=3)
        self.wait(1)
        self.play(Write(caption21), run_time=3)
        self.wait(1)
        self.play(FadeOut(caption), FadeOut(caption2), FadeOut(caption21), run_time=1)

        self.play(Write(caption3), run_time=3)
        self.wait(1)
        self.play(Transform(caption3, caption4), run_time=3)
        self.wait(1)
        self.play(Write(caption5), run_time=3)
        self.wait(1)
        self.play(Transform(caption4, caption6), run_time=3)
        self.wait(1)
        self.play(FadeOut(caption3), FadeOut(caption4), FadeOut(caption5), FadeOut(caption6), run_time=1)

        self.play(Write(caption7), run_time=3)
        self.wait(1)
        self.play(Transform(caption8, caption9), run_time=3)
        self.wait(1)
        self.play(Transform(caption9, caption10), run_time=3)
        self.wait(1)
        self.play(Transform(caption10, caption11), run_time=3)
        self.wait(1)
        self.play(FadeOut(caption7), FadeOut(caption8), FadeOut(caption9), FadeOut(caption10), FadeOut(caption11), run_time=1)

        self.play(Write(caption12), run_time=3)
        self.wait(1)
        self.play(Write(caption13), run_time=3)
        self.wait(1)
        self.play(Transform(caption13, caption14), run_time=3)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(caption12), FadeOut(caption13), FadeOut(caption14), run_time=3)

