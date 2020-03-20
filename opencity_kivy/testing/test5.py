from kivy.app import App
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from myanim import MyAnim


class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
        self.img1 = Image(source="F:\PyCharm Python Works\Kivy Test\opencityicon (1).png")
        box_layout = BoxLayout()
        self.add_widget(box_layout)
        box_layout.add_widget(self.img1)

    def on_enter(self, *args):
        animation = MyAnim(d=1, x=560) + MyAnim(d=1)
        print(animation.widgets)
        animation.start(self.img1)
        print(animation.widgets)


sm = ScreenManager()
sm.add_widget(ScreenOne(name='screen_one'))
sm.current = 'screen_one'


class Test(App):
    def build(self):
        return sm


if __name__ == '__main__':
    Test().run()
