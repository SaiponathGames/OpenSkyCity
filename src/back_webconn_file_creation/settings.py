__all__ = [
    'Settings'
]

import pathlib

import appdirs


class Settings:
    def __init__(self, version, home_folder=None, app_data_folder=None):
        self.appdirs_data = appdirs.AppDirs('OpenCity', 'Spar Interactive', version)
        # Main folders
        self.SOURCE_FOLDER = pathlib.Path(__file__).absolute().parent.parent
        self.BACKEND_FOLDER = pathlib.Path(__file__).absolute().parent
        self.FRONT_END_FOLDER = self.SOURCE_FOLDER / 'front_ui_display'
        self.HOME_FOLDER = ((home_folder and pathlib.Path(home_folder)) or pathlib.Path.home()) / self.appdirs_data.appauthor / self.appdirs_data.appname / self.appdirs_data.version
        self.APPDATA_FOLDER = ((app_data_folder and pathlib.Path(app_data_folder) / self.appdirs_data.appauthor / self.appdirs_data.appname / self.appdirs_data.version) or pathlib.Path(self.appdirs_data.user_data_dir))

        # Plugin folders
        self.PLUGINS_FOLDER = self.HOME_FOLDER / 'Plugins'
        self.PLUGINS_ASSETS_FOLDER = self.PLUGINS_FOLDER / 'Assets'
        self.PLUGINS_MAPS_FOLDER = self.PLUGINS_FOLDER / 'Maps'
        self.PLUGINS_THEMES_FOLDER = self.PLUGINS_FOLDER / 'Themes'
        self.PLUGINS_MODS_FOLDER = self.PLUGINS_FOLDER / 'Mods'

        # music folder
        self.MUSIC_FOLDER = self.HOME_FOLDER / 'Music'

        # Premium folders with cache.
        self.PREMIUM_BACKEND_FOLDER = self.BACKEND_FOLDER / 'premium'
        self.PREMIUM_USERS_FOLDER = self.HOME_FOLDER / 'Premium'
        self.PREMIUM_APPDATA_FOLDER = self.APPDATA_FOLDER / 'Premium'
        self.PREMIUM_ROOT_USRA_FILE = self.PREMIUM_BACKEND_FOLDER / 'premium_users.usra'
        self.PREMIUM_APPDATA_TXT_FILE = self.PREMIUM_APPDATA_FOLDER / 'premium_users.txt'
        self.PREMIUM_USERS_USRA_FILE = self.PREMIUM_USERS_FOLDER / 'premium_users.usra'

        # Special Sandbox folders with cache.
        self.SPECIAL_SANDBOX_APPDATA_FOLDER = self.APPDATA_FOLDER / 'Special Sandbox'
        self.SPECIAL_SANDBOX_BACKEND_FOLDER = self.BACKEND_FOLDER / 'special_sandbox'
        self.SPECIAL_SANDBOX_USERS_FOLDER = self.HOME_FOLDER / 'Special Sandbox'
        self.SPECIAL_SANDBOX_APPDATA_TXT_FILE = self.SPECIAL_SANDBOX_APPDATA_FOLDER / 'special_sandbox_users.txt'
        self.SPECIAL_SANDBOX_USERS_USRA_FILE = self.SPECIAL_SANDBOX_USERS_FOLDER / 'special_sandbox_users.usra'
        self.SPECIAL_SANDBOX_ROOT_USRA_FILE = self.SPECIAL_SANDBOX_BACKEND_FOLDER / 'special_sandbox_users.usra'

        # Save files and folder
        self.SAVES_FOLDER = self.HOME_FOLDER / 'Saves'
        self.SAVES_FILE_FORMATTED = 'save{number}_{city_name}.save'

        # Map file
        self.CITY_FOLDER = self.HOME_FOLDER / 'Cities'
        self.CITY_FILE_FORMATTED = '{city_name}.city'

        self.ROOTS = [self.HOME_FOLDER, self.APPDATA_FOLDER]

        self.PLUGIN_FOLDERS = [
            self.PLUGINS_FOLDER,
            self.PLUGINS_ASSETS_FOLDER,
            self.PLUGINS_MAPS_FOLDER,
            self.PLUGINS_THEMES_FOLDER,
            self.PLUGINS_MODS_FOLDER
        ]

        self.MUSIC_FOLDERS = [self.MUSIC_FOLDER]

        self.PREMIUM_FOLDERS_AND_FILES = [
            self.PREMIUM_APPDATA_FOLDER,
            self.PREMIUM_USERS_FOLDER,
            self.PREMIUM_USERS_USRA_FILE,
            self.PREMIUM_APPDATA_TXT_FILE
        ]

        self.SPECIAL_SANDBOX_FOLDERS_AND_FILES = [
            self.SPECIAL_SANDBOX_APPDATA_FOLDER,
            self.SPECIAL_SANDBOX_USERS_FOLDER,
            self.SPECIAL_SANDBOX_USERS_USRA_FILE,
            self.SPECIAL_SANDBOX_APPDATA_TXT_FILE
        ]

        self.SAVES_AND_MAPS = [
            self.SAVES_FOLDER
        ]

        self.ALL_FOLDERS = [
            self.ROOTS,
            self.PLUGIN_FOLDERS,
            [self.CITY_FOLDER],
            self.MUSIC_FOLDERS,
            self.PREMIUM_FOLDERS_AND_FILES,
            self.SPECIAL_SANDBOX_FOLDERS_AND_FILES
        ]
        self.OPENCITY_KIVY = self.FRONT_END_FOLDER / 'opencity_kivy'
        self.SOURCE_FOLDERS = [self.SOURCE_FOLDER, self.BACKEND_FOLDER, self.FRONT_END_FOLDER]
        self.SPECIAL_SANDBOX_ROOT_FOLDERS_AND_FILES = [
            self.SPECIAL_SANDBOX_BACKEND_FOLDER,
            self.SPECIAL_SANDBOX_ROOT_USRA_FILE
        ]
        self.PREMIUM_ROOT_FOLDERS_AND_FILES = [
            self.PREMIUM_BACKEND_FOLDER,
            self.PREMIUM_ROOT_USRA_FILE
        ]

        # Premium and Special Sandbox based Settings
        self.PREMIUM_ID_START = 10000000000
        self.PREMIUM_ID_END = 99999999999
        self.PREMIUM_KEY_LENGTH = 25

        self.SPECIAL_SANDBOX_ID_START = 100000000000000000000000000000
        self.SPECIAL_SANDBOX_ID_END = 999999999999999999999999999999
        self.SPECIAL_SANDBOX_KEY_LENGTH = 35

        self.KEYS_FILE = self.BACKEND_FOLDER / 'keys.key'

        self.ASSET_FILE_FORMATTED = "{asset_name}.asset"
        self.MOD_FILE_FORMATTED = "{mod_name}.mod"
        self.PLUGIN_FILE_FORMATTED = "{plugin_name}.plugin"
        self.THEME_FILE_FORMATTED = "{theme_name}.theme"
        self.MAP_FILE_FORMATTED = "{map_name}.map"
