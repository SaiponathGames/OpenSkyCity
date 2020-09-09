import kivy  # noqa
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')

import src.opencity

if __name__ == '__main__':
    src.opencity.main()
