"""Hoverable Behaviour (changing when the mouse is on the widget by O. Poyen.
License: LGPL
"""
__author__ = ['Olivier POYEN', 'Sairam', 'John Anderson']

__all__ = ['HoverBehavior', 'MyAnimation']

from kivy.animation import Animation, Parallel, Sequence
from kivy.core.window import Window
from kivy.properties import BooleanProperty, ListProperty, ObjectProperty


class HoverBehavior(object):
    """Hover behavior.
    :Events:
        `on_enter`
            Fired when mouse enter the bbox of the widget.
        `on_leave`
            Fired when the mouse exit the widget
    """

    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)
    '''Contains the last relevant point received by the Hoverable. This can
    be used in `on_enter` or `on_leave` in order to know where was dispatched the event.
    '''

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')  # noqa
        self.register_event_type('on_leave')  # noqa
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():  # noqa
            return  # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]

        # Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))  # noqa
        if self.hovered == inside:
            # We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')  # noqa
        else:
            self.dispatch('on_leave')  # noqa

    def on_enter(self):
        pass

    def on_leave(self):
        pass


from kivy.factory import Factory

Factory.register('HoverBehavior', HoverBehavior)


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
