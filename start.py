# https://docs.manim.org.cn/getting_started/quickstart.html
# from manimlib import *

# class SquareToCircle(Scene): # 创建一个 Scene 的子类 SquareToCircle——将要编写、渲染的场景
#     def construct(self): # 决定如何创建画面的物体，以及可执行的操作
#         circle = Circle() # Circle 类的实例
#         circle.set_fill(BLUE, opacity=0.5) # 填充，设置样式 https://docs.manim.org.cn/documentation/constants.html
#         circle.set_stroke(BLUE_E, width=4) # 线条，深蓝色
#
#         self.add(circle) # Scene 的方法 add 添加到画面

# 【执行语句】
# manimgl start.py SquareToCircle 【输出画面】
# manimgl start.py SquareToCircle -os 【输出图片】
# manimgl start.py SquareToCircle -ow 【输出动画】
# manimgl 【可直接进入交互模式】

from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square() # Square 类的实例

        # 【为什么这次不用 add 添加到画面？因为 play 已经有展示功能？】
        self.play(ShowCreation(square)) # Scene 的方法 play 播放动画，ShowCreation 是一个动画（效果）【理解为平滑效果】
        self.wait() # Scene 的方法，默认1s
        self.play(ReplacementTransform(square, circle)) # square => circle 的动画【顺序影响变化效果】
        self.wait()

        # self.embed() # 【交互模式，不可碰窗口，在 cmd 进行交互】

        # 在水平方向上拉伸到四倍
        self.play(circle.stretch, 4, {"dim": 0})
        # 旋转90°
        self.play(Rotate(circle, TAU / 4))
        # 在向右移动2单位同时缩小为原来的1/4
        self.play(circle.shift, 2 * RIGHT, circle.scale, 0.25)
        # 为了非线性变换，给circle增加10段曲线（不会播放动画）
        circle.insert_n_curves(10)
        # 给circle上的所有点施加f(z)=z^2的复变换
        self.play(circle.apply_complex_function, lambda z: z ** 2)
        # 关闭窗口并退出程序
        # exit()
