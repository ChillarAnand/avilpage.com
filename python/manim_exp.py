from manim import *


class Minimizer(Scene):
    def construct(self):
        ref_set = Text("ATGATGACTAGAAATAGATGATATG")
        query_set = Text("AATAGATATG")

        self.play(Write(ref_set))
        self.play(ref_set.animate.shift(UP))

        self.play(Write(query_set))
        self.play(query_set.animate.shift(LEFT))

        self.wait(4)
