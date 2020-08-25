from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("game_gui.kv")


class Game_GUI(BoxLayout):
    pass


class OpenCity(App):
    def build(self):
        return Game_GUI()


if __name__ == '__main__':
    OpenCity().run()
