import os

import kivy
# Config.set("kivy", "log_level", "debug")
from kivy.app import App
from kivy.lang import Builder
from kivy.core.audio.audio_sdl2 import MusicSDL2  # noqa
from kivy.uix.screenmanager import Screen
from opencity_kivy.hoverbehavior import HoverBehavior  # noqa

kivy.require("1.11.1")

original_dir = os.path.realpath(os.path.dirname(__file__))
os.chdir(original_dir)

Builder.load_file("main_menu.kv")


# class ImageButton(ButtonBehavior, HoverBehavior, Image):
#
# 	def __init__(self, **kwargs):
# 		super(ImageButton, self).__init__(**kwargs)
#
#


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_music_playing = False
    def play_background_music(self):  # noqa
        if not self.background_music_playing:
            self.background_music = MusicSDL2(source="c_fast.wav")  # noqa
            self.background_music.load()
            self.background_music.bind(on_stop=self.on_background_music_stop)
            self.background_music.play()
            self.background_music_playing = True  # noqa
        # self.background_music_playing = False  # noqa

    def on_background_music_stop(self, *args):  # noqa
        if App.get_running_app().sm.current not in ("main_menu", "exit_game_menu"):
            if self.background_music_playing:
                self.background_music.stop()
        else:
            self.background_music.play()

# sm = ScreenManager(transition=NoTransition())
# sm.add_widget(MainMenu(name='main_menu'))
# # sm.add_widget(ExitGameScreen(name='exitgamescreen'))
# sm.current = 'main_menu'
#
#
# class OpenCity12(App):
# 	def __init__(self, **kwargs):
# 		super(OpenCity12, self).__init__(**kwargs)
# 		self.sound1 = SoundLoader.load("button_press.mp3")
#
# 	def build(self):
# 		return sm
#
# 	def play_button_sound(self):
# 		self.sound1.play()
#

# class OpenCity1:
#     def __init__(self, **kwargs):
#         super(OpenCity1, self).__init__(**kwargs)
#         self.x1 = 21
#         print(self.x1)

#
# if __name__ == '__main__':
# 	# OpenCity1()
# 	OpenCity12().run()
