import os

import kivy
from kivy.config import Config

Config.set("kivy", "log_level", "debug")
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

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
    pass

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
