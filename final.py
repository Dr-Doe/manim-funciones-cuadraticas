from manim import *

class Final(Scene):
    def construct(self):
        title = Text("Función final y conclusión", font="Times New Roman", font_size=40).to_edge(UP)
        subtitle = Text("Teniendo los valores, podemos determinar la ecuacion que modela el problema", font_size=20).next_to(title, DOWN)

        formule = MathTex(r"f(x) = ax^2 + bx + c", font_size=36).next_to(subtitle, DOWN).to_edge(LEFT)
        caption = MathTex(r"f(x)", r" = \frac{5}{2}x^2 - 20x + c", font_size=36).next_to(formule, DOWN).to_edge(LEFT)
        formule.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        caption.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        table = Table(
            [["0", "2", "4", "6", "8"],
            ["50", "20", "10", "20", "50"]],
            row_labels=[Text("x"), Text("y")],
            include_outer_lines=True
        ).next_to(caption, DOWN).scale(0.3).to_edge(LEFT).shift(UP)

        self.add(title)
        self.play(Write(title), run_time=3)
        self.play(Write(subtitle), run_time=3)
        self.play(Write(formule), run_time=3)
        self.play(Write(caption), run_time=3)
        self.play(Create(table), run_time=3)

        axes = Axes(
            x_range=[-3, 11, 1],
            y_range=[0, 60, 10],
            axis_config={"include_numbers": True},
        ).shift(DOWN).scale(0.7).shift(RIGHT)

        labels = axes.get_axis_labels(Tex('x (tiempo)').scale(0.60), Text("y (altura)").scale(0.45))

        self.play(Create(axes), run_time=3)
        self.play(Write(labels), run_time=3)

        # Create the buildings
        building1 = Rectangle(width=1, height=axes.y_axis.unit_size * 35, fill_color=GREEN, fill_opacity=0.3, stroke_width=0).move_to(axes.c2p(-1, 25))  # Centered at y=25 for height up to 50
        building2 = Rectangle(width=1, height=axes.y_axis.unit_size * 35, fill_color=GREEN, fill_opacity=0.3, stroke_width=0).move_to(axes.c2p(9, 25))  # Centered at y=25 for height up to 50

        self.play(Create(building1), Create(building2)) # Create buildings before dots

        dot_axes = Dot(axes.c2p(0, 50), color="#FFFF00")
        lines = axes.get_lines_to_point(dot_axes.get_center(), color=WHITE)
        dot_axes1 = Dot(axes.c2p(2, 20), color="#FFFF00")
        lines1 = axes.get_lines_to_point(dot_axes1.get_center(), color=WHITE)
        dot_axes2 = Dot(axes.c2p(4, 10), color="#FFFF00")
        lines2 = axes.get_lines_to_point(dot_axes2.get_center(), color=WHITE)
        dot_axes3 = Dot(axes.c2p(6, 20), color="#FFFF00")
        lines3 = axes.get_lines_to_point(dot_axes3.get_center(), color=WHITE)
        dot_axes4 = Dot(axes.c2p(8, 50), color="#FFFF00")
        lines4 = axes.get_lines_to_point(dot_axes4.get_center(), color=WHITE)
        dot_support_axes = Dot(axes.c2p(4, 50), color=RED)

        self.play(Create(dot_axes), Create(lines), run_time=1)
        self.wait(0.5)
        self.play(Create(dot_axes1), Create(lines1), run_time=1)
        self.wait(0.5)
        self.play(Create(dot_axes2), Create(lines2), run_time=1)
        self.wait(0.5)
        self.play(Create(dot_axes3), Create(lines3), run_time=1)
        self.wait(0.5)
        self.play(Create(dot_axes4), Create(lines4), run_time=1)
        self.wait(0.5)
        self.play(Create(dot_support_axes), run_time=1)
        self.wait(0.5)

        parabola = axes.plot(lambda x: 2.5*x**2 - 20*x + 50, color=BLUE)

        self.play(Create(parabola), run_time=3)

        spiderman = ImageMobject("resources/img/spider-man-logo.png").scale(0.11)
        initial_position = axes.c2p(0, 50)
        spiderman.move_to(initial_position)
        
        

        rope = Line(dot_support_axes.get_center(), spiderman.get_center(), color=GRAY)

        # Add the rope before the animation of Spiderman
        self.play(Create(rope))

        self.play(FadeIn(spiderman), run_time=3)

        def update_rope(mob):  # mob refers to the rope object itself
            mob.become(Line(dot_support_axes.get_center(), spiderman.get_center(), color=GRAY)) # Update rope endpoints

        rope.add_updater(update_rope) # Update the line when spiderman moves.

        def update_spiderman(mob, alpha):
            x = alpha * 8
            y = 2.5 * x**2 - 20 * x + 50
            mob.move_to(axes.c2p(x, y))

        alpha_tracker = ValueTracker(0) 

        spiderman.add_updater(lambda mob: update_spiderman(mob, alpha_tracker.get_value()))

        self.play(alpha_tracker.animate.set_value(1), run_time=4, rate_func=linear)

        spiderman.remove_updater(lambda mob: update_spiderman(mob, alpha_tracker.get_value()))
        rope.remove_updater(update_rope)

        final_position = axes.c2p(8, 50)
        spiderman.move_to(final_position)
        self.wait(6)

        self.play(FadeOut(spiderman), FadeOut(rope), FadeOut(parabola), FadeOut(axes), FadeOut(labels), FadeOut(table), FadeOut(caption), FadeOut(formule), FadeOut(subtitle), FadeOut(title), FadeOut(dot_axes), FadeOut(dot_axes1), FadeOut(dot_axes2), FadeOut(dot_axes3), FadeOut(dot_axes4), FadeOut(dot_support_axes), FadeOut(lines), FadeOut(lines1), FadeOut(lines2), FadeOut(lines3), FadeOut(lines4), FadeOut(building1), FadeOut(building2), run_time=6)