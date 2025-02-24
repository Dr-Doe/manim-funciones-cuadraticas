from manim import *

class Planteo(Scene):
    def construct(self):

        title = Text("Elementos claves para plantear el problema", font="Times New Roman", font_size=40)
        title.to_edge(UP)

        subtitle  = Text("Spiderman se encuentra en la cima de un edificio de 50 metros de altura\ny se balancea desde un punto a otro tocandoun minimo de 10 metros\nsobre el nivel del piso en 4 segundos", font_size=20, color=YELLOW_B)
        subtitle.next_to(title, DOWN)
    

        building = ImageMobject("resources/img/edificio.png").next_to(subtitle, DOWN)
        building.scale(0.4)

        caption = Text("50 metros de altura", font_size=20).next_to(building, DOWN)
        caption2 = Text("10 metros sobre el nivel del suelo", font_size=20).next_to(caption, DOWN)
        caption3 = Text("4 segundos hasta el mínimo", font_size=20).next_to(caption2, DOWN)

        self.play(Write(title), run_time=5)
        self.wait(1)
        self.play(Write(subtitle), run_time=5)
        self.wait(1)
        self.play(FadeIn(building), run_time=3)
        self.wait(1)
        self.play(Write(caption), run_time=3)
        self.wait(1)
        self.play(Write(caption2), run_time=3)
        self.wait(1)
        self.play(Write(caption3), run_time=3)
        self.wait(7)
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(building), FadeOut(caption), FadeOut(caption2), FadeOut(caption3), run_time=6)