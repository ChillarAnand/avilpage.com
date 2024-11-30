from collections import deque

from manim import *

class Kmer(Scene):
    def construct(self):
        x_vals = list("ATGA")
        y_vals = deque("AT  ")
        data = [x_vals, list(y_vals)]
        print(data)
        t1 = Table(
            data,
            # col_labels=[Text("Ref"), Text("Query")],
            # include_background_rectangle=False,
            line_config={"stroke_width": 0, "color": YELLOW}
        )
        # table animation
        self.play(FadeIn(t1))
        # rotate second row in table
        self.wait(0.5)
        y_vals.rotate(1)
        data = [x_vals, list(y_vals)]
        print(data)
        t1.update(data)
        t2 = Table(
            data,
            # col_labels=[Text("Ref"), Text("Query")],
            # include_background_rectangle=False,
            line_config={"stroke_width": 0, "color": YELLOW}
        )
        self.play(FadeOut(t1))
        self.play(FadeIn(t2))
        # self.play(t1.animate.shift(UP * 0.5))
        self.interactive_embed()
