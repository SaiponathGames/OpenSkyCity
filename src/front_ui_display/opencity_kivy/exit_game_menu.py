import os

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from ...back_webconn_file_creation.settings import Settings

from .helper import HoverBehavior  # noqa

settings = Settings()
# original_dir = os.path.realpath(os.path.dirname(__file__))
# print(original_dir)
# os.chdir(original_dir)

Builder.load_file(str(settings.OPENCITY_KIVY / "exit_game_menu.kv"))


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
