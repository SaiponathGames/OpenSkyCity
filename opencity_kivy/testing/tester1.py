from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.video import Video


class VideoPlay(Screen):
    def __init__(self, **kwargs):
        super(VideoPlay, self).__init__(**kwargs)
        self.video1 = Video(source="..\GTAtitles.mpg")
        box_layout = BoxLayout()
        box_layout.add_widget(self.video1)
        self.add_widget(box_layout)

    def on_enter(self):
        self.video1.allow_stretch = True
        self.video1.state = "play"


if __name__ == "__main__":
    sm = ScreenManager()
    sm.add_widget(VideoPlay(name="videoplay"))
    sm.current = "videoplay"


    class Game(App):
        def build(self):
            return sm

    Game().run()
