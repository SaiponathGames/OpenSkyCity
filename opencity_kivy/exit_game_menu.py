import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


original_dir = os.path.realpath(os.path.dirname(__file__))
os.chdir(original_dir)

Builder.load_file("exit_game_menu.kv")



class ExitGameScreen(Screen):
    pass


