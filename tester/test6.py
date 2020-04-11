import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


class MyAppApp(App):
    def build(self):
        layout = GridLayout(cols=10)
        for num in range(201, 301):
            num = str(num)
            button = Button(text=num)
            sound = SoundLoader.load("button_press.mp3")
            button.bind(on_press=lambda *args: sound.play())
            layout.add_widget(button)
        return layout


MyAppApp().run()