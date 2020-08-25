__all__ = [

    # Main folders
    'ROOT_FOLDER',
    'HOME_FOLDER',
    'APPDATA_FOLDER',

    # Plugin folders
    'PLUGINS_FOLDER',
    'PLUGINS_ASSETS_FOLDER',
    'PLUGINS_MAPS_FOLDER',
    'PLUGINS_MODS_FOLDER',
    'PLUGINS_THEMES_FOLDER',

    # Music
    'MUSIC_FOLDER',

    # Premium folder with cache
    'PREMIUM_ROOT_FOLDER',
    'PREMIUM_APPDATA_FOLDER',
    'PREMIUM_USERS_FOLDER',
    'PREMIUM_ROOT_USRA_FILE',
    'PREMIUM_APPDATA_TXT_FILE',
    'PREMIUM_USERS_USRA_FILE',

    # Special Sandbox folder with cache.
    'SPECIAL_SANDBOX_ROOT_FOLDER',
    'SPECIAL_SANDBOX_USERS_FOLDER',
    'SPECIAL_SANDBOX_APPDATA_FOLDER',
    'SPECIAL_SANDBOX_USERS_USRA_FILE',
    'SPECIAL_SANDBOX_APPDATA_TXT_FILE',
    'SPECIAL_SANDBOX_ROOT_USRA_FILE',

    # Save files and folder
    'SAVES_FOLDER',
    'SAVES_FILE_FORMATTED',

    # Map files and folder
    'MAPS_FOLDER',
    'MAP_FILE_FORMATTED',

    # Collective lists to make it easy to create.
    'ROOTS',
    'PLUGIN_FOLDERS',
    'PREMIUM_FOLDERS_AND_FILES',
    'MUSIC_FOLDERS',
    'SPECIAL_SANDBOX_FOLDERS_AND_FILES',
    'SAVES_AND_MAPS',

    # ALL Folders
    'ALL_FOLDERS'

]

import pathlib
import sys


def get_datadir() -> pathlib.Path:
    """
    Returns a parent directory path
    where persistent application data can be stored.

    # linux: ~/.local/share
    # macOS: ~/Library/Application Support
    # windows: C:/Users/<USER>/AppData/Roaming
    """

    home = pathlib.Path.home()

    if sys.platform == "win32":
        return home / "AppData/Local"
    elif sys.platform == "linux":
        return home / ".local/share"
    elif sys.platform == "darwin":
        return home / "Library/Application Support"


# Main folders
ROOT_FOLDER = pathlib.Path(__name__).absolute().parent
HOME_FOLDER = pathlib.Path.home() / 'OpenCity'
APPDATA_FOLDER = get_datadir() / 'OpenCity'

# Plugin folders
PLUGINS_FOLDER = HOME_FOLDER / 'Plugins'
PLUGINS_ASSETS_FOLDER = PLUGINS_FOLDER / 'Assets'
PLUGINS_MAPS_FOLDER = PLUGINS_FOLDER / 'Maps'
PLUGINS_THEMES_FOLDER = PLUGINS_FOLDER / 'Themes'
PLUGINS_MODS_FOLDER = PLUGINS_FOLDER / 'Mods'

# music folder
MUSIC_FOLDER = HOME_FOLDER / 'Music'

# Premium folders with cache.
PREMIUM_ROOT_FOLDER = ROOT_FOLDER / 'premium'
PREMIUM_USERS_FOLDER = HOME_FOLDER / 'Premium'
PREMIUM_APPDATA_FOLDER = APPDATA_FOLDER / 'Premium'
PREMIUM_ROOT_USRA_FILE = PREMIUM_ROOT_FOLDER / 'premium_users.usra'
PREMIUM_APPDATA_TXT_FILE = PREMIUM_APPDATA_FOLDER / 'premium_users.txt'
PREMIUM_USERS_USRA_FILE = PREMIUM_USERS_FOLDER / 'premium_users.usra'

# Special Sandbox folders with cache.
SPECIAL_SANDBOX_APPDATA_FOLDER = APPDATA_FOLDER / 'Special Sandbox'
SPECIAL_SANDBOX_ROOT_FOLDER = ROOT_FOLDER / 'special_sandbox'
SPECIAL_SANDBOX_USERS_FOLDER = HOME_FOLDER / 'Special Sandbox'
SPECIAL_SANDBOX_APPDATA_TXT_FILE = SPECIAL_SANDBOX_APPDATA_FOLDER / 'special_sandbox_users.txt'
SPECIAL_SANDBOX_USERS_USRA_FILE = SPECIAL_SANDBOX_USERS_FOLDER / 'special_sandbox_users.usra'
SPECIAL_SANDBOX_ROOT_USRA_FILE = SPECIAL_SANDBOX_ROOT_FOLDER / 'special_sandbox_users.usra'

# Save files and folder
SAVES_FOLDER = HOME_FOLDER / 'Saves'
SAVES_FILE_FORMATTED = 'save{number}_{map_name}.save'

# Map file
MAPS_FOLDER = HOME_FOLDER / 'Maps'
MAP_FILE_FORMATTED = '{map_name}.map'

ROOTS = [ROOT_FOLDER, HOME_FOLDER, APPDATA_FOLDER]

PLUGIN_FOLDERS = [
    PLUGINS_FOLDER,
    PLUGINS_ASSETS_FOLDER,
    PLUGINS_MAPS_FOLDER,
    PLUGINS_THEMES_FOLDER,
    PLUGINS_MODS_FOLDER
]

MUSIC_FOLDERS = [MUSIC_FOLDER]

PREMIUM_FOLDERS_AND_FILES = [
    PREMIUM_ROOT_FOLDER,
    PREMIUM_APPDATA_FOLDER,
    PREMIUM_USERS_FOLDER,
    PREMIUM_USERS_USRA_FILE,
    PREMIUM_APPDATA_TXT_FILE,
    PREMIUM_ROOT_USRA_FILE
]

SPECIAL_SANDBOX_FOLDERS_AND_FILES = [
    SPECIAL_SANDBOX_ROOT_FOLDER,
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
