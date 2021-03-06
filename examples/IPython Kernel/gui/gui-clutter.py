#!/usr/bin/env python
"""Simple Clutter example to manually test event loop integration.

This is meant to run tests manually in ipython as:

In [1]: %gui clutter

In [2]: %run gui-clutter.py
"""

from gi.repository import Clutter, GLib


def on_click(*args):
    print(args)


def stage_key(element, event):
    if event.keyval == Clutter.Escape:
        clutter_quit()


def clutter_quit(*args):
    Clutter.main_quit()


Clutter.init([])
stage = Clutter.Stage()

stage.connect('destroy', clutter_quit)
stage.set_size(400, 400)

actor = Clutter.Actor()
actor.set_size(*stage.get_size())
actor.set_background_color(Clutter.Color.new(255, 147, 8, 255))
actor.connect('button-press-event', on_click)
actor.set_reactive(True)
actor.set_pivot_point(0.5, 0.5)

transition = Clutter.PropertyTransition(property_name='rotation-angle-z')
transition.set_duration(5000)
transition.set_from(0.0)
transition.set_to(360.0)
transition.set_animatable(actor)
transition.set_repeat_count(-1)
transition.start()


stage.add_child(actor)
stage.connect('key-press-event', stage_key)
stage.show()

try:
    from IPython.lib.inputhook import enable_clutter
    enable_clutter()
except ImportError:
    Clutter.main()
