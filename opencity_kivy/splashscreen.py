import os

from kivy.animation import Animation
from myanimation import MyAnimation
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import NoTransition, Screen, ScreenManager
from kivy.uix.video import Video
from exit_game_menu import ExitGameScreen
from main_menu import MainMenu
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty


original_dir = os.path.realpath(os.path.dirname(__file__))
os.chdir(original_dir)

print(original_dir)
audio_playback = True


def do_nothing(*args):
	for _ in args:
		pass


class ScreenOne(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.img = Image(source="Spar Interactive.png", opacity=0)
		box_layout = BoxLayout()
		self.add_widget(box_layout)
		box_layout.add_widget(self.img)

	def on_new_anim_complete(self, *args):
		do_nothing(self, *args)
		change_screen_to('screen_two')

	def on_enter(self):
		self.img.opacity = 0
		new_anim = Animation(duration=4, opacity=0)
		new_anim.bind(on_complete=self.on_new_anim_complete)
		animation1 = Animation(duration=3) + Animation(duration=4, opacity=1) + Animation(duration=5) + new_anim
		animation1.start(self.img)


class ScreenTwo(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.img2 = Image(source="OpenCity_Icon.png", opacity=0)
		self.img3 = Image(source="opencityicon (1).png", opacity=0)
		self.label1 = Label(text="Just a place holder audio", opacity=0, pos_hint={"x": 0, "bottom": 1}, size_hint=[0.2, 0.1])
		your_anim = Animation(d=4, opacity=1)
		your_anim.bind(on_start=self.on_anim1_start)
		anim2 = Animation(d=4, opacity=0)
		anim2.bind(on_complete=self.on_anim2_complete)
		anim3 = Animation(d=2) if audio_playback else Animation(d=5)
		self.animation1 = Animation(d=3) + your_anim + Animation(d=4) + anim2 + anim3
		float_layout = FloatLayout()
		self.add_widget(float_layout)
		float_layout.add_widget(self.label1, index=1)
		float_layout.add_widget(self.img2)
		float_layout.add_widget(self.img3)

	def on_anim2_complete(self, *dt):
		do_nothing(dt)
		if audio_playback:
			self.label1.text = ""
			change_screen_to('screen_three')
		if not audio_playback:
			change_screen_to('kivy_splash')

	def on_anim1_start(self, *args):
		do_nothing(*args)
		if audio_playback:
			self.label1.text = "Just a place holder audio"
			sound1 = SoundLoader.load(os.path.join(original_dir, "OpenCity1.mp3"))
			sound1.play()

	def on_enter(self):
		self.img2.opacity = 0
		self.img3.opacity = 0
		self.label1.opacity = 1
		# print("audio_playback = ", audio_playback)
		if audio_playback:
			self.animation1.start(self.img2)
		else:
			self.animation1.start(self.img3)


class ScreenThree(Screen):

	def __init__(self, **kwargs):
		super(ScreenThree, self).__init__(**kwargs)
		self.video1 = Video(source=os.path.join(original_dir, "cityCC0.mpg"))
		float_layout = FloatLayout()
		self.label1 = Label(text="Just a place holder video", opacity=0, pos_hint={"x": 0, "bottom": 1}, size_hint=[0.2, 0.1])
		# self.label2 = Label(text="loading video", opacity=0)
		# pos_hint = {"x": 0, "bottom": 1}, size_hint=[0.2, 0.1]
		self.add_widget(float_layout)
		float_layout.add_widget(self.label1, index=0)
		# float_layout.add_widget(self.label2)
		float_layout.add_widget(self.video1, index=1)
		self.video1.opacity = 0

	def video1_play(self, *dt):
		do_nothing(dt)
		self.video1.state = "play"
		# self.event1 = Clock.schedule_interval(partial(print, self.video1.loaded), 0.5)
		self.label1.opacity = 1
		self.video1.opacity = 1
		# self.label2.opacity = 0
		self.video1.volume = 1

	def on_video1_eos(self, *dt):
		do_nothing(dt, self)
		global audio_playback
		# print(self.video1.loaded)
		# Clock.schedule_once(self.video1_play)
		audio_playback = False
		change_screen_to('screen_two')
		# self.event1.cancel()

	def on_enter(self):
		self.video1.allow_stretch = True
		self.video1.state = "play"
		self.label1.opacity = 1
		self.video1.bind(eos=self.on_video1_eos)
		# self.label2.opacity = 1
		Clock.schedule_once(self._adjust_opacity, 1)
		# self.event1 = Clock.schedule_interval(self._check_loaded, 0.5)

	# def _check_loaded(self, *dt):
	#     if self.video1.loaded:
	#         self.video1.play = True
	#     do_nothing(dt, self.video1.loaded)

	def _adjust_opacity(self, *dt):
		do_nothing(dt)
		self.video1.opacity = 1


class KivySplash(Screen):
	def __init__(self, **kwargs):
		super(KivySplash, self).__init__(**kwargs)
		# anim1 = MyAnimation(duration=4, opacity=0)
		# anim1.bind(on_complete=self.on_anim1_complete)
		# self.animation1 = MyAnimation(duration=3) + MyAnimation(duration=4, opacity=1) + MyAnimation(duration=5) + anim1
		self.img1 = Image(source=os.path.join(original_dir, "Kivy-logo-black-512.png"), opacity=0)
		self.img2 = Image(source=os.path.join(original_dir, "python-powered-w-200x80.png"), opacity=0)
		self.label1 = Label(text="Powered by:", font_size=48, opacity=0)
		anim1 = MyAnimation(duration=4, opacity=0)
		self.i1 = 0
		self.animated_objects = []
		anim1.bind(on_complete=self.on_anim1_complete)
		self.animation = MyAnimation(duration=3 + self.i1)
		box_layout = BoxLayout(orientation="vertical")
		box_layout1 = BoxLayout()
		box_layout.add_widget(self.label1)
		box_layout1.add_widget(self.img1)
		box_layout1.add_widget(self.img2)
		box_layout.add_widget(box_layout1)
		self.add_widget(box_layout)

	def on_enter(self, *args):
		for i, widget in enumerate((self.label1, self.img2, self.img1)):
			anim1 = MyAnimation(duration=4, opacity=0)
			anim1.bind(on_complete=self.on_anim1_complete)
			self.animation = MyAnimation(duration=3 + i) + MyAnimation(duration=4, opacity=1) + MyAnimation(duration=5 - i) + anim1
			self.animation.start(widget)
			self.animated_objects.append(widget)

	def on_anim1_complete(self, *args):
		do_nothing(self, *args)
		if self.label1 in self.animated_objects:
			change_screen_to("main_menu")


sm = ScreenManager(transition=NoTransition())
sm.add_widget(ScreenOne(name="screen_one"))
sm.add_widget(ScreenTwo(name="screen_two"))
sm.add_widget(ScreenThree(name="screen_three"))
sm.add_widget(KivySplash(name="kivy_splash"))
sm.add_widget(MainMenu(name="main_menu"))
sm.add_widget(ExitGameScreen(name="exit_game_screen"))
sm.current = "screen_one"


def change_screen_to(screen, *args):
	do_nothing(*args)
	sm.current = screen


# Clock.schedule_once(partial(change_screen_to, 'screen_two'), 18)
# Clock.schedule_once(partial(change_screen_to, 'screen_three'), 36)
# Clock.schedule_once(App.stop, 32)
# Clock.schedule_once(Window.close, 32)


class OpenCityApp(App):
	icon = StringProperty(os.path.join(original_dir, "OpenCity_Icon.png"))

	def build(self):
		return sm


#
if __name__ == "__main__":
	OpenCityApp().run()
	# source = os.path.join(current_dir, "opencityicon.png")
	# Label(text="OpenCity", font_size=150, opacity=0)
