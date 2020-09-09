__all__ = [
    'Settings'
]

import pathlib

import appdirs


class Settings:
    appdirs_data = appdirs.AppDirs('OpenCity', 'Spar Interactive', "0.7")
    # Main folders
    SOURCE_FOLDER = pathlib.Path(__file__).absolute().parent.parent
    BACKEND_FOLDER = pathlib.Path(__file__).absolute().parent
    FRONT_END_FOLDER = SOURCE_FOLDER / 'front_ui_display'
    HOME_FOLDER = pathlib.Path.home() / appdirs_data.appauthor / appdirs_data.appname / appdirs_data.version
    APPDATA_FOLDER = pathlib.Path(appdirs_data.user_data_dir)

    # Plugin folders
    PLUGINS_FOLDER = HOME_FOLDER / 'Plugins'
    PLUGINS_ASSETS_FOLDER = PLUGINS_FOLDER / 'Assets'
    PLUGINS_MAPS_FOLDER = PLUGINS_FOLDER / 'Maps'
    PLUGINS_THEMES_FOLDER = PLUGINS_FOLDER / 'Themes'
    PLUGINS_MODS_FOLDER = PLUGINS_FOLDER / 'Mods'

    # music folder
    MUSIC_FOLDER = HOME_FOLDER / 'Music'

    # Premium folders with cache.
    PREMIUM_BACKEND_FOLDER = BACKEND_FOLDER / 'premium'
    PREMIUM_USERS_FOLDER = HOME_FOLDER / 'Premium'
    PREMIUM_APPDATA_FOLDER = APPDATA_FOLDER / 'Premium'
    PREMIUM_ROOT_USRA_FILE = PREMIUM_BACKEND_FOLDER / 'premium_users.usra'
    PREMIUM_APPDATA_TXT_FILE = PREMIUM_APPDATA_FOLDER / 'premium_users.txt'
    PREMIUM_USERS_USRA_FILE = PREMIUM_USERS_FOLDER / 'premium_users.usra'

    # Special Sandbox folders with cache.
    SPECIAL_SANDBOX_APPDATA_FOLDER = APPDATA_FOLDER / 'Special Sandbox'
    SPECIAL_SANDBOX_BACKEND_FOLDER = BACKEND_FOLDER / 'special_sandbox'
    SPECIAL_SANDBOX_USERS_FOLDER = HOME_FOLDER / 'Special Sandbox'
    SPECIAL_SANDBOX_APPDATA_TXT_FILE = SPECIAL_SANDBOX_APPDATA_FOLDER / 'special_sandbox_users.txt'
    SPECIAL_SANDBOX_USERS_USRA_FILE = SPECIAL_SANDBOX_USERS_FOLDER / 'special_sandbox_users.usra'
    SPECIAL_SANDBOX_ROOT_USRA_FILE = SPECIAL_SANDBOX_BACKEND_FOLDER / 'special_sandbox_users.usra'

    # Save files and folder
    SAVES_FOLDER = HOME_FOLDER / 'Saves'
    SAVES_FILE_FORMATTED = 'save{number}_{map_name}.save'

    # Map file
    MAPS_FOLDER = HOME_FOLDER / 'Maps'
    MAP_FILE_FORMATTED = '{map_name}.map'

    ROOTS = [BACKEND_FOLDER, HOME_FOLDER, APPDATA_FOLDER]

    PLUGIN_FOLDERS = [
        PLUGINS_FOLDER,
        PLUGINS_ASSETS_FOLDER,
        PLUGINS_MAPS_FOLDER,
        PLUGINS_THEMES_FOLDER,
        PLUGINS_MODS_FOLDER
    ]

    MUSIC_FOLDERS = [MUSIC_FOLDER]

    PREMIUM_FOLDERS_AND_FILES = [
        PREMIUM_BACKEND_FOLDER,
        PREMIUM_APPDATA_FOLDER,
        PREMIUM_USERS_FOLDER,
        PREMIUM_USERS_USRA_FILE,
        PREMIUM_APPDATA_TXT_FILE,
        PREMIUM_ROOT_USRA_FILE
    ]

    SPECIAL_SANDBOX_FOLDERS_AND_FILES = [
        SPECIAL_SANDBOX_BACKEND_FOLDER,
        SPECIAL_SANDBOX_APPDATA_FOLDER,
        SPECIAL_SANDBOX_USERS_FOLDER,
        SPECIAL_SANDBOX_ROOT_USRA_FILE,
        SPECIAL_SANDBOX_USERS_USRA_FILE,
        SPECIAL_SANDBOX_APPDATA_TXT_FILE
    ]

    SAVES_AND_MAPS = [
        MAPS_FOLDER,
        SAVES_FOLDER
    ]

    ALL_FOLDERS = [
        ROOTS,
        PLUGIN_FOLDERS,
        MUSIC_FOLDERS,
        SAVES_AND_MAPS,
        PREMIUM_FOLDERS_AND_FILES,
        SPECIAL_SANDBOX_FOLDERS_AND_FILES
    ]

    # Premium and Special Sandbox based Settings
    PREMIUM_ID_START = 10000000000
    PREMIUM_ID_END = 99999999999
    PREMIUM_KEY_LENGTH = 25

    SPECIAL_SANDBOX_ID_START = 100000000000000000000000000000
    SPECIAL_SANDBOX_ID_END = 999999999999999999999999999999
    SPECIAL_SANDBOX_KEY_LENGTH = 35

    KEYS_FILE = BACKEND_FOLDER / 'keys.key'

    OPENCITY_KIVY = FRONT_END_FOLDER / 'opencity_kivy'
