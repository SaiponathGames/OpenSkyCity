import kivy
import os
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition

kivy.require("1.11.1")

original_dir = os.path.realpath(os.path.dirname(__file__))
os.chdir(original_dir)

Builder.load_file("main_menu.kv")


class MainMenu(Screen):
	pass


sm = ScreenManager(transition=NoTransition())
sm.add_widget(MainMenu(name='main_menu'))
# sm.add_widget(ExitGameScreen(name='exitgamescreen'))
sm.current = 'main_menu'


class OpenCity12(App):
	def build(self):
		return sm


# class OpenCity1:
#     def __init__(self, **kwargs):
#         super(OpenCity1, self).__init__(**kwargs)
#         self.x1 = 21
#         print(self.x1)

#
if __name__ == '__main__':
	# OpenCity1()
	OpenCity12().run()
