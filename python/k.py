from manim import *


class Kmer(Scene):
    def construct(self):
        np = NumberPlane()
        np.add_coordinates = True
        # self.add(np)

        NumberPlane.add_coordinates = True
        font_size = 40
        sr = Text('   '.join("ATCGATTACATGA"), font_size=font_size)
        sq = Text('   '.join("GATTACA"), font_size=font_size)

        self.play(FadeIn(sr))
        self.play(sr.animate.shift(UP))
        self.play(FadeIn(sq))

        group = VGroup(sr, sq)
        group.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        # Animate the sequences towards each other
        self.play(
            sr.animate.shift(DOWN * 0.0),
            sq.animate.scale(1).shift(UP * 0.1),
            run_time=1,
            rate_func=linear
        )

        sub_str_len = len(sq)
        for i in range(0, 4):
            # shift by 1 character of text
            sub_ref = sr[i:sub_str_len + i]
            group = VGroup(sub_ref, sq)
            color = ORANGE
            if i == 3:
                color = GREEN
            rect = SurroundingRectangle(group, buff=0.2, color=color)
            if i == 3:
                self.play(FadeIn(rect))
                self.wait(0.1)
                self.play(FadeOut(rect))
                self.wait(0.1)
                self.play(FadeIn(rect))
                self.wait(0.1)
                self.play(FadeOut(rect))
                self.wait(0.1)
                self.play(FadeIn(rect))
                return
            else:
                self.play(Create(rect), run_time=0.3)

            self.wait(0.5)
            self.play(FadeOut(rect))

            self.play(
                sq.animate.shift(RIGHT * 0.8),
                run_time=1,
                rate_func=linear
            )

        self.interactive_embed()
        self.wait(1)
