from kivy.animation import Animation, Parallel, Sequence
from kivy.properties import ListProperty

__all__ = ['MyAnimation']
__author__ = ['John Anderson', 'Sairam']


class MySequence(Sequence):
    widgets = ListProperty([])
    animated_widgets = ListProperty([])

    def start(self, widget):
        self.widgets.append(widget)
        self.animated_widgets.append(widget)
        super(MySequence, self).start(widget)

    def stop(self, widget):
        if widget in self.widgets:
            self.widgets.remove(widget)
        super(MySequence, self).stop(widget)

    def __add__(self, animation):
        return MySequence(self, animation)

    def __and__(self, animation):
        return MyParallel(self, animation)


class MyParallel(Parallel):
    widgets = ListProperty([])
    animated_widgets = ListProperty([])

    def start(self, widget):
        self.widgets.append(widget)
        self.animated_widgets.append(widget)
        super(MyParallel, self).start(widget)

    def stop(self, widget):
        if widget in self.widgets:
            self.widgets.remove(widget)
        super(MyParallel, self).stop(widget)

    def __add__(self, animation):
        return MySequence(self, animation)

    def __and__(self, animation):
        return MyParallel(self, animation)


class MyAnimation(Animation):
    widgets = ListProperty([])
    animated_widgets = ListProperty([])

    def start(self, widget):
        self.widgets.append(widget)
        self.animated_widgets.append(widget)
        super(MyAnimation, self).start(widget)

    def stop(self, widget):
        if widget in self.widgets:
            self.widgets.remove(widget)
        super(MyAnimation, self).stop(widget)

    def __add__(self, animation):
        return MySequence(self, animation)

    def __and__(self, animation):
        return MyParallel(self, animation)

