import os
os.environ['KIVY_VIDEO'] = 'gstplayer'
import sys

import kivy  # noqa
from kivy.config import Config

Config.set('kivy', 'log_level', 'info')
if sys.platform.startswith(('win', 'linux')):
    Config.set('input', 'mouse', 'mouse,disable_multitouch')  # noqa
Config.set('graphics', 'fullscreen', 'auto')

import src.opencity

if __name__ == '__main__':
    def resourcePath():
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS)
        return os.path.join(os.path.abspath("."))


    # noinspection PyUnresolvedReferences
    kivy.resources.resource_add_path(resourcePath())
    src.opencity.main()
