#!/usr/bin/env python

from manimlib.imports import *


# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()


class UpdatersExample1(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=1,
        )
        self.wait()


class demo1(Scene):
    CONFIG = {
        # Mobject
        'color': consts.WHITE,
        'height': 0.2,
        # Text
        'font': '',
        'gradient': None,
        'lsh': -1,
        'size': 1,
        'slant': NORMAL,
        'weight': NORMAL,
        't2c': {},
        't2f': {},
        't2g': {},
        't2s': {},
        't2w': {},
    }

    def construct(self):
        clear_codes = [
            "Node *p, *tmp;",
            "p = head-> next;",
            "while (p != NULL)",
            "{",
            "    tmp = p;",
            "    p = p->next;",
            "    delete tmp;",
            "}",
            "head->next = NULL;",
            "tail = head;",
            "curLength = 0;",
        ]
        l = []
        num = 30
        kill = num // 2
        m = 9
        n = 5
        #
        txt = '''约瑟夫双向生死游戏是在约瑟夫生者死者游戏的基础上，正向计数后反向计数，然后再正向计数。
具体描述如下：30个旅客同乘一条船，因为严重超载，加上风高浪大，危险万分；因此船长告诉
乘客，只有将全船一半的旅客投入海中，其余人才能幸免遇难。无奈，大家只得同意这种办法，
并议定30个人围成一圈，由第一个人开始，顺时针依次报数，数到第9人，便把他投入大海中，
然后从他的下一个人数起，逆时针数到第5人，将他投入大海，然后从他逆时针的下一个人数起，
顺时针数到第9人，再将他投入大海，如此循环，直到剩下15个乘客为止。问哪些位置是将被扔
下大海的位置。'''
        text = Text(f"{txt}", font='宋体', weight=NORMAL, size=1.5).scale(0.21)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        text1 = Text(f"总人数:{num}", font='宋体', weight=NORMAL, color=BLUE_A).scale(0.35).move_to(np.array([-6, 3, 0]))
        text2 = Text(f"杀掉的人数:{kill}", font='宋体', weight=NORMAL, color=BLUE_B).scale(0.35).move_to(
            np.array([-6, 2.5, 0]))
        text3 = Text(f"向前人数:{m}", font='宋体', weight=NORMAL, color=BLUE_C).scale(0.35).move_to(np.array([-6, 2, 0]))
        text4 = Text(f"向后人数:{n}", font='宋体', weight=NORMAL, color=BLUE_D).scale(0.35).move_to(np.array([-6, 1.5, 0]))
        R1 = VGroup()
        self.play(Write(text1), Write(text2), Write(text3), Write(text4), )

        for i in range(num):
            circle = Circle(radius=0.3)
            # circle1 = Circle(radius=0.1)
            text = Text(str(i + 1), font='宋体').scale(0.25)

            circle.move_to(-3 * LEFT * math.sin(2 * i * math.pi / num) - 3 * UP * math.cos(2 * i * math.pi / num))
            # circle1.next_to(circle,RIGHT)
            # text.shuffle(circle)
            text.next_to(circle, 0)
            g = VGroup(circle, text)
            l.append(g)

        for i in l:
            self.add(i)
            self.wait(0.1)
        end = l[0][0].get_center()

        end = np.array([i for i in end])
        line = Vector(end)
        self.add(line)
        index = 1
        num_txt = None
        nowindex = 1
        i = 0
        forceward = Text(f"向前数{m}步", font='宋体', weight=NORMAL, size=1.5, color=BLUE_E).scale(0.4).shift(UP)
        num_txt = Text(f"{i}", font='宋体', weight=NORMAL, size=1.5, color=RED).scale(0.5)
        self.play(Write(num_txt), run_time=0.2)
        while len(l) != num - kill:
            if i % 2 == 0:
                index = (m - 1) % len(l) + 1

            else:

                index = (-n) % len(l) + 1

            if nowindex != index:
                t = l.pop(0)
                l.append(t)
                nowindex += 1
            else:
                temp = l.pop(0)
                if i % 2 == 0:

                    # self.play(FadeOut(forceward), run_time=0.2)
                    self.play(Transform(forceward,
                                        Text(f"向前数{m}步", font='宋体', weight=NORMAL, size=1.2, color=GREEN_A).scale(
                                            0.3).shift(UP)))
                    # forceward = Text(f"向前数{m}步", font='宋体', weight=NORMAL, size=1.5).scale(0.4).shift(UP)
                    # self.play(Write(forceward), run_time=0.2)
                else:

                    self.play(Transform(forceward,
                                        Text(f"向后数{n}步", font='宋体', weight=NORMAL, size=1.2, color=MAROON_E).scale(
                                            0.3).shift(DOWN)))
                    # self.play(FadeOut(forceward), run_time=0.2)
                    # forceward = Text(f"向后数{n}步", font='宋体', weight=NORMAL, size=1.5).scale(0.4).shift(UP)
                    # self.play(Write(forceward), run_time=0.2)
                # self.play(ApplyMethod(line.set_leng   th,1))

                self.play(FadeOut(num_txt), run_time=0.2)
                num_txt = Text(f"{i}", font='宋体', weight=NORMAL, size=1.2, color=RED).scale(0.45)
                self.play(Write(num_txt), run_time=0.2)
                radians = -line.get_angle() + np.arctan2(temp[0].get_y(), temp[0].get_x())
                if radians < 0:
                    radians += 2 * np.pi
                if i % 2 == 0:
                    radians = radians
                else:
                    radians = radians - 2 * np.pi
                self.play(Rotating(line, about_point=ORIGIN,
                                   radians=radians),
                          run_time=0.2)
                self.wait(0.5)
                # temp.move_to([-6.5,3-i*0.5,0])

                self.play(ApplyMethod(temp.set_fill, GREY), ApplyMethod(temp.set_color, GREY), run_time=0.5)
                self.play(Transform(temp, Square().scale(0.3)), run_time=0.5)
                R1.add(temp)
                self.wait(0.3)
                nowindex = 1
                i += 1
        self.play(FadeOut(num_txt), run_time=0.2)
        num_txt = Text(f"{i}", font='宋体', weight=NORMAL, size=1.2).scale(0.45)
        self.play(Write(num_txt), run_time=0.2)

        self.play(Transform(line, Circle(radius=3.5)))
        self.play(Transform(forceward, Text(f"游戏结束", font='宋体', weight=NORMAL, size=1.5).scale(0.5)))

        self.play(Transform(forceward, Square().scale(0.3)))

        for temp in l:
            R1.add(temp)
            self.play(Transform(temp, Square().scale(0.3)), run_time=0.2)
            i += 1
            self.play(Transform(num_txt, Text(f"{i}", font='宋体', weight=NORMAL, size=1.2).scale(0.45)), run_time=0.2)
        self.play(Transform(line, Square().scale(0.3)), run_time=0.5)
        self.play(Transform(text1, Square().scale(0.3)), run_time=0.2)
        self.play(Transform(text2, Square().scale(0.3)), run_time=0.2)
        self.play(Transform(text3, Square().scale(0.3)), run_time=0.2)
        self.play(Transform(text4, Square().scale(0.3)), run_time=0.2)
        R1.add(forceward)
        R1.add(line)
        R1.add(num_txt)
        R1.add(text1)
        R1.add(text2)
        R1.add(text3)
        R1.add(text4)

        self.play(FadeOutAndShiftDown(R1))
        txt = "Author:HTR"
        text = Text(f"{txt}", font='宋体', weight=NORMAL, size=0.8, color=YELLOW_C).scale(2)
        self.play(GrowFromEdge(text, LEFT))
        txt = "Talk is cheap show me the code."
        text1 = Text(f"{txt}", font='宋体', weight=NORMAL, size=0.8, color=BLUE_C).scale(0.8)
        self.play(Transform(text, text1))
        self.wait(10)


from my_logo import *


# demo_01
class Logo_bounce_around(Scene):

    def construct(self):

        logo = Logo(size=0.5, plot_depth=-1).shift(UP)  # .set_opacity(0.12)
        self.logo_velocity = (RIGHT * 25 + 5 * UP) * 2e-2
        self.rotate_speed = 2 * DEGREES

        def update_logo(l, dt):
            l.shift(self.logo_velocity)
            l.rotate(self.rotate_speed)
            if abs(l.get_center()[1]) > (FRAME_HEIGHT - l.get_height()) / 2:
                self.logo_velocity *= DR  # or we can use self.logo_velocity[1] *= -1
                self.rotate_speed *= -1
            if abs(l.get_center()[0]) > (FRAME_WIDTH - l.get_width()) / 2:
                self.logo_velocity *= UL  # or we can use self.logo_velocity[0] *= -1
                self.rotate_speed *= -1

        logo.add_updater(update_logo)
        self.add(logo)

        # self.wait(1)
        # self.play(Write(TexMobject('xgnb!!!').scale(2.5)), run_time=2)

        self.wait(15)


class demo_graph(GraphScene):
    def construct(self):
        self.setup_axes(animate=True)
        g = self.get_graph(self.pow, color=RED)
        # lab=self.get_graph_label(g,label="y=x")
        # line=self.get_vertical_line_to_graph(3.7,g,color=YELLOW)
        self.play(ShowCreation(g))
        self.wait(2)

    def pow(self, x):
        return x
