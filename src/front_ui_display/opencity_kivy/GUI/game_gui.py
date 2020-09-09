from threading import Thread

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("game_gui.kv")


class Game_GUI(BoxLayout):
    pass


class OpenCity(App):
    is_app_stopped = False

    def build(self):
        return Game_GUI()

    def on_stop(self):
        self.is_app_stopped = True


if __name__ == '__main__':
    opencity = OpenCity()


    def _while():
        while not opencity.is_app_stopped:
            x = 10
            x += 1


    thread = Thread(target=_while)
    thread.start()
    opencity.run()
    thread.join()
