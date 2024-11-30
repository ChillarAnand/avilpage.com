from manim import *


class Kmer(Scene):
    def construct(self):
        ref = Text("  ".join("ATGCGATAGTC"))
        self.play(FadeIn(ref))
        self.play(ref.animate.shift(UP))

        text = Text("ATCG          ")
        self.play(FadeIn(text))
        self.wait(0.5)
        self.play(FadeOut(text))
        text = Text("ATCG")
        self.play(FadeIn(text))

        self.wait(10)
