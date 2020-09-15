import pathlib
import random
from typing import List

try:
    from . import file as file_module, settings
except ImportError:
    from src.back_webconn_file_creation import file as file_module, settings


def check_for_files(settings_: settings.Settings) -> List[pathlib.Path]:
    FILES = []
    for folders in settings_.ALL_FOLDERS:
        for file in folders:
            if file.suffix:
                FILES.append(file)
    return FILES


def check_for_folders(settings_: settings.Settings) -> List[pathlib.Path]:
    FOLDERS = []
    for folders in settings_.ALL_FOLDERS:
        for folder in folders:
            if not folder.suffix:
                FOLDERS.append(folder)
    return FOLDERS


def create_folders(folders: List[pathlib.Path]) -> None:
    for folder in folders:
        if not folder.exists():
            folder.mkdir(exist_ok=True, parents=True)


def create_files(files: List[pathlib.Path]) -> None:
    for file in files:
        if not file.exists():
            file.touch()


def create_save_file(settings_: settings.Settings, safe_file_num, city_name):
    save_file = settings_.SAVES_FOLDER / str(settings_.SAVES_FILE_FORMATTED.format(number=safe_file_num, city_name=city_name))
    return save_file.touch()


def create_city_file(settings_: settings.Settings, city_name):
    city_file = settings_.CITY_FOLDER / str(settings_.CITY_FILE_FORMATTED.format(city_name=city_name))
    return city_file.touch()


def create_theme_file(settings_: settings.Settings, theme_name):
    theme_file = settings_.PLUGINS_THEMES_FOLDER / str(settings_.THEME_FILE_FORMATTED.format(theme_name=theme_name))
    return theme_file.touch()


def create_mod_file(settings_: settings.Settings, mod_name):
    mod_file = settings_.PLUGINS_MODS_FOLDER / str(settings_.MOD_FILE_FORMATTED.format(mod_name=mod_name))
    mod_file.touch()


def create_plugin_file(settings_: settings.Settings, plugin_name):
    plugin_file = settings_.PLUGINS_FOLDER / str(settings_.PLUGIN_FILE_FORMATTED.format(plugin_name=plugin_name))
    plugin_file.touch()


def create_asset_file(settings_: settings.Settings, asset_name):
    asset_file = settings_.PLUGINS_ASSETS_FOLDER / str(settings_.ASSET_FILE_FORMATTED.format(asset_name=asset_name))
    asset_file.touch()


def create_map_file(settings_: settings.Settings, map_name):
    map_file = settings_.PLUGINS_MAPS_FOLDER / str(settings_.MAP_FILE_FORMATTED.format(map_name=map_name))
    map_file.touch()


if __name__ == '__main__':
    app_settings = settings.Settings()
    create_folders(check_for_folders(app_settings))
    create_files(check_for_files(app_settings))
    # create_save_files(10, 'Test')
    asset_file_contents = ['Beautiful_Tree', 'Truck_Station', '2_Way_Train_Station', 'Train_Tracks']
    plugin_file_contents = ['Metro_Overhaul', 'Bus_Mod', 'Status', 'City_Icon']
    mod_file_contents = ['Track_Change', 'District_State_Country', '72_Tiles', 'Too_Hard_Mod', 'Too_Easy_Mod']
    theme_file_contents = ['Winter_Special', 'Summer_Special', 'European', 'Sunny_Summer', 'Toys']
    city_file_contents = file_module.file_read(app_settings.BACKEND_FOLDER / 'some_city_names.txt', encoding='utf-8')
    map_files_contents = ['Riverah', 'Mountainia', 'Hillyia', 'Bulliya']
    for number in range(5):
        if len(list(app_settings.CITY_FOLDER.iterdir())) > 20:
            break
    create_city_file(app_settings, random.choice(city_file_contents))
    create_theme_file(app_settings, random.choice(theme_file_contents))
    create_mod_file(app_settings, random.choice(mod_file_contents))
    create_asset_file(app_settings, random.choice(asset_file_contents))
    create_map_file(app_settings, random.choice(city_file_contents))
    create_plugin_file(app_settings, random.choice(asset_file_contents))
