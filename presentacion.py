from manim import *
import manim

class Introduccion_Parte1(Scene):
    def construct(self):
        # Title 1 - first
        title1 = Text("Presentación de:", font_size=72, font="Times New Roman")
        self.play(
            Write(title1, run_time=3)
        )
        self.play(
            FadeOut(title1), run_time=3
        )
        self.wait(1)

        # Title 2 - second
        title2 = Text("¿Dónde vemos\nfunciones en\nnuestra vida?", 
                     font_size=72, font="Times New Roman", 
                     line_spacing=1.2, t2w={'nuestra vida': BOLD}, t2c={'funciones': RED})
        self.play(
            Write(title2[0]),
            Write(title2[1:7]),
            Write(title2[7:11]),
            Write(title2[11:16]),
            Write(title2[16:22]),
            Write(title2[22:29]),
            Write(title2[29:35]),
            run_time=5
        )
        self.play(
            FadeOut(title2), run_time=3
        )
        self.wait(1)

        # Names section - third
        title3 = Text("Hecho por:", font_size=48, font="Times New Roman")
        title3.to_edge(UP)
        self.play(
            Write(title3),  
            run_time=3
        )
        self.wait(1)

        title4 = Text("Andrés José López\nBenjamín Maximiliano Troncoso\nJoaquín Alexis Seguel\nMaría del Pilar Simón\nValentino Emanuel Delgado Gatica", line_spacing=1.2, font_size=48, font="Times New Roman", t2c={'[12:17]': '#FFFF00', '[38:47]': '#FFFF00', '[63:70]': '#FFFF00', '[85:91]': '#FFFF00', '[109:124]': '#FFFF00'})
        title4.next_to(title3, DOWN)
        self.play(
            Write(title4),
            
            run_time=8
        )
        self.play(FadeOut(title3), FadeOut(title4), run_time=3)
        self.wait(1)
