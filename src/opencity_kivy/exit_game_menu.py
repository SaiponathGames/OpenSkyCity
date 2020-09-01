import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from .helper import HoverBehavior  # noqa

original_dir = os.path.realpath(os.path.dirname(__file__))
os.chdir(original_dir)

Builder.load_file("exit_game_menu.kv")


class ExitGameScreen(Screen):
    pass

# sm = ScreenManager()
# sm.add_widget(ExitGameScreen(name="exit_game"))
# sm.current = "exit_game"


# class ExitGame(App):
# 	def build(self):
# 		return sm


# if __name__ == '__main__':
# 	ExitGame().run()
