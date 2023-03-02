from manim import *
%%manim -v WARNING --disable_caching -qm -r400,400 Example1

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        mob = MathTex(r'\Psi(x)', color=WHITE)
        mob = Text('NO', color=YELLOW,weight=BOLD)
