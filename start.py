# https://docs.manim.org.cn/getting_started/quickstart.html
from manimlib import *

class SquareToCircle(Scene): # 创建一个 Scene 的子类 SquareToCircle——将要编写、渲染的场景
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        self.add(circle)