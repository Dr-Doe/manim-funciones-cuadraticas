from manim import *

class PlanteoSolucion2_Parte4(Scene):
    def construct(self):
        title = Text("Usando la fórmula del vértice", font="Times New Roman", font_size=40).to_edge(UP)

        caption = Text("a  b", font_size=30).next_to(title, DOWN)
        caption.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        caption2 = Text("El punto mas bajo o alto de una parabola es su vertice", font_size=30).next_to(caption, DOWN)
        caption3 = MathTex(r"h = \frac{-b}{2a}").next_to(caption2, DOWN)
        caption3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        caption4 = Text("Donde h es el valor de x en el vértice", font_size=30).next_to(caption3, DOWN)
        
        caption5 = Text("El punto mas bajo ocurre cuando x = 4", font_size=30).next_to(title, DOWN)
        caption6 = MathTex(r"4 = \frac{-b}{2a}").next_to(caption5, DOWN)
        caption6.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        caption7 = Text("Multiplicamos ambos terminos por 2a", font_size=30).next_to(caption6, DOWN)
        caption8 = MathTex(r"8a = -b").next_to(caption7, DOWN)
        caption8.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        caption9 = MathTex(r"b = -8a").next_to(caption8, DOWN)
        caption9.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        caption10 = Text("Esto nos ayudará a encontrar a y b", font_size=30).next_to(caption9, DOWN)

        self.play(Write(title), run_time=3)
        self.wait(1)
        self.play(Write(caption), run_time=3)
        self.wait(1)
        self.play(Write(caption2), run_time=3)
        self.wait(1)
        self.play(Write(caption3), run_time=3)
        self.wait(1)
        self.play(Write(caption4), run_time=3)
        self.wait(1)

        self.play(FadeOut(caption), FadeOut(caption2), FadeOut(caption4), run_time=3)
        self.play(Write(caption5), run_time=3)
        self.wait(1)

        self.play(Transform(caption3, caption6), run_time=3)
        self.wait(1)
        self.play(Write(caption7), run_time=3)
        self.wait(1)
        self.play(Transform(caption6, caption8), run_time=3)
        self.wait(1)
        self.play(Transform(caption8, caption9), run_time=3)
        self.wait(1)
        self.play(Write(caption10), run_time=3)
        self.wait(1)

        self.play(FadeOut(title), FadeOut(caption3), FadeOut(caption5), FadeOut(caption6), FadeOut(caption7), FadeOut(caption8), FadeOut(caption9), FadeOut(caption10), run_time=6)


