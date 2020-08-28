import sys


class OpenCity:
    build = "0.00.000.0125"
    Version = "0.4"
    Premium = True
    Special_sandbox = True
    debug = False
    Name = "OpenCity"


__version__ = OpenCity.Version

if __name__ == '__main__':
    from discord_rpc_deco import with_discord_rich_presence
    from kivy.config import Config

    Config.set('kivy', 'log_level', 'info')
    if sys.platform.startswith(('win', 'linux')):  # noqa
        Config.set('input', 'mouse', 'mouse,disable_multitouch')  # noqa

    print("{} v{} \nBuild ({}) \n\n\n".format(OpenCity.Name, OpenCity.Version, OpenCity.build))
    # from files_and_folders import folder_and_file_creator as ft
    # from premium.premium_test import premium_test as pt
    # from special_sandbox.special_sandbox_mode_test import special_sandbox_mode_test as st
    import opencity_kivy.splashscreen as ss

    # ft()
    # print()
    # pt()
    # print()
    # st()
    # print()
    with with_discord_rich_presence(OpenCity, state='In the Main Menu'):
        ss.OpenCityApp().run()
