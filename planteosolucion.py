from manim import *

class PlanteoSolucion_Parte3(Scene):
    def construct(self):

        title = Text("Planteando la función cuadrática", font="Times New Roman", font_size=40)
        title.to_edge(UP)

        planteo = MathTex(r"f(x) = ax^2 + bx + c")
        planteo.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        planteo.next_to(title, DOWN)

        caption = Text("x: Tiempo", font_size=30, t2c={"x": YELLOW}).next_to(planteo, DOWN)
        caption2 = Text("f(x): Altura", font_size=30, t2c={"x": YELLOW}).next_to(caption, DOWN)
        caption3 = Text("Para cada valor de tiempo en x refleja un valor de altura en y", font_size=30, t2c={"x": YELLOW}).next_to(caption2, DOWN)

        spiderman = ImageMobject("resources/img/spider-man-logo.png")
        spiderman.scale(0.3)
        spiderman.to_edge(DOWN)

        caption4 = Text("x = 0, entonces la altura es igual a 50 metros", font_size=30, t2c={"x": YELLOW}).next_to(planteo, DOWN)

        caption5 = Text("Nos da la ordenada al origen, c = 50", font_size=30, t2c={"c": BLUE}).next_to(caption4, DOWN)
        caption6 = Text("A los 4 segundos (x = 4), f(x) = 10", font_size=30, t2c={"x": YELLOW}).next_to(caption5, DOWN)

        self.play(Write(title), run_time=3)
        self.wait(1)
        self.play(Write(planteo), run_time=3)
        self.wait(1)
        self.play(Write(caption), run_time=3)
        self.wait(1)
        self.play(Write(caption2), run_time=3)
        self.wait(1)
        self.play(Write(caption3), run_time=3)
        self.wait(1)
        self.play(FadeIn(spiderman), run_time=3)
        self.wait(1)

        self.play(FadeOut(caption), FadeOut(caption2), FadeOut(caption3), run_time=3)

        self.play(Write(caption4), run_time=3)
        self.wait(1)
        self.play(Write(caption5), run_time=3)
        self.wait(1)
        self.play(Write(caption6), run_time=3)
        self.wait(1)
        self.play(FadeOut(spiderman), run_time=3)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(caption4), FadeOut(caption5), FadeOut(caption6), FadeOut(planteo), run_time=6)
