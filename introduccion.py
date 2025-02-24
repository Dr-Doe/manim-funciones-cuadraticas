from manim import *

class Presentacion_Parte2(Scene):
    def construct(self):
        title = Text("Introducción a la Función Cuadrática con Spiderman", font="Times new roman", font_size=40, t2c={"Función Cuadrática": YELLOW, "Spiderman": RED}).to_edge(UP)

        # Spiderman meme
        spiderman_meme = ImageMobject("resources/img/spiderman-raro.jpg").scale(0.3)

        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
        ).add_coordinates()
        axes.scale(0.7)
        axes.shift(DOWN)

        labels = axes.get_axis_labels(Tex('x (tiempo)').scale(0.60), Text("y (altura)").scale(0.45))

        plane = NumberPlane()

        parabola = axes.plot(lambda x: 2*x**2, color="#FFFF00")

        self.play(Write(title))
        self.wait(2)

        self.play(FadeIn(spiderman_meme))
        self.play(FadeOut(spiderman_meme) , run_time=2)
        self.wait(1)

        self.play(Create(axes))
        self.play(Write(labels))
        self.play(Create(plane))
        self.wait(1)
        self.play(Create(parabola))
        self.wait(1)

        self.play(FadeOut(parabola))
        self.play(FadeOut(axes))
        self.play(FadeOut(labels))
        self.play(FadeOut(plane))
        self.play(FadeOut(title))
        self.wait(1)

        caption = Text("La función cuadrática es de la forma:", font="Times New Roman", font_size=32).next_to(title, DOWN)

        equation = MathTex("f(x) = ax^2 + bx + c").next_to(caption, DOWN)

        equation.set_color_by_gradient("#33ccff", "#ff00ff")


        self.play(Write(caption))
        self.play(Write(equation))
        self.wait(1)

        axes2 = Axes(
            x_range=[-2, 2],
            y_range=[-1, 4],
            axis_config={"include_numbers": False, "include_tip": False},
        ).add_coordinates()

        axes2.scale(0.6).shift(DOWN)

        labels = axes2.get_axis_labels(Tex('x (tiempo)').scale(0.60), Text("y (altura)").scale(0.45))

        parabola2 = axes2.plot(lambda x: 2*x**2, x_range=[-2, 2])

        parabola2.set_color_by_gradient("#33ccff", "#ff00ff")

        self.play(Create(axes2), run_time=2)
        self.play(Write(labels), run_time=1)
        self.wait(1)
        self.play(Write(parabola2), run_time=2)
        self.wait(1)
        self.play(FadeOut(parabola2), FadeOut(axes2), FadeOut(labels), FadeOut(equation), FadeOut(caption), run_time=6)
