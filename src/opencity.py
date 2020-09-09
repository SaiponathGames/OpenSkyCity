import sys

from .front_ui_display.opencity_kivy.splashscreen import OpenCityApp


class OpenCity(OpenCityApp):
    build_version = "0.00.000.0345"
    Version = "0.7"
    Premium = True
    Special_sandbox = True
    debug = False
    Name = "OpenCity"
    start_screen = "main_menu"


__version__ = OpenCity.Version


def main():
    from .back_webconn_file_creation.discord_rpc_deco import with_discord_rich_presence
    from kivy.config import Config

    Config.set('kivy', 'log_level', 'info')
    if sys.platform.startswith(('win', 'linux')):
        Config.set('input', 'mouse', 'mouse,disable_multitouch')  # noqa
    opencity = OpenCity()
    print("{} v{} \nBuild ({}) \n\n\n".format(OpenCity.Name, OpenCity.Version, OpenCity.build_version))
    # from files_and_folders import folder_and_file_creator as ft
    # from premium.premium_test import premium_test as pt
    # from special_sandbox.special_sandbox_mode_test import special_sandbox_mode_test as st

    # ft()
    # print()
    # pt()
    # print()
    # st()
    # print()
    with with_discord_rich_presence(opencity, state='In the Main Menu'):
        opencity.run()
