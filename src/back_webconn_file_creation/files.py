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
            if file.name.startswith(('save', '{}.map')):
                continue
            file.touch()


def create_save_files(settings_: settings.Settings, number_of_save_files, map_name):
    for i in range(number_of_save_files):
        save_file = settings_.SAVES_FOLDER / str(settings_.SAVES_FILE_FORMATTED.format(number=i, map_name=map_name))
        save_file.touch()


def create_city_files(settings_: settings.Settings, number_of_city_files):
    contents = file_module.file_read(settings_.BACKEND_FOLDER / 'some_city_names.txt', encoding='utf-8')
    for number in range(number_of_city_files):
        if len(list(settings_.CITY_FOLDER.iterdir())) > 20:
            break
        city_name = random.choice(contents)
        city_file = settings_.CITY_FOLDER / str(settings_.CITY_FILE_FORMATTED.format(city_name=city_name))
        city_file.touch()
        create_save_files(settings_, 3, city_name)


def create_theme_files(settings_: settings.Settings, number_of_theme_files):
    contents = ['Winter_Special', 'Summer_Special', 'European', 'Sunny_Summer', 'Toys']
    for number in range(number_of_theme_files):
        theme_file = settings_.PLUGINS_THEMES_FOLDER / str(settings_.THEME_FILE_FORMATTED.format(theme_name=random.choice(contents)))
        theme_file.touch()


def create_mod_files(settings_: settings.Settings, number_of_mod_files):
    contents = ['Track_Change', 'District_State_Country', '72_Tiles', 'Too_Hard_Mod', 'Too_Easy_Mod']
    for number in range(number_of_mod_files):
        mod_file = settings_.PLUGINS_MODS_FOLDER / str(settings_.MOD_FILE_FORMATTED.format(mod_name=random.choice(contents)))
        mod_file.touch()


def create_plugin_files(settings_: settings.Settings, number_of_plugin_files):
    contents = ['Metro_Overhaul', 'Bus_Mod', 'Status', 'City_Icon']
    for number in range(number_of_plugin_files):
        plugin_file = settings_.PLUGINS_FOLDER / str(settings_.PLUGIN_FILE_FORMATTED.format(plugin_name=random.choice(contents)))
        plugin_file.touch()


def create_asset_files(settings_: settings.Settings, number_of_asset_files):
    contents = ['Beautiful_Tree', 'Truck_Station', '2_Way_Train_Station', 'Train_Tracks']
    for number in range(number_of_asset_files):
        asset_file = settings_.PLUGINS_ASSETS_FOLDER / str(settings_.ASSET_FILE_FORMATTED.format(asset_name=random.choice(contents)))
        asset_file.touch()


def create_map_files(settings_: settings.Settings, number_of_map_files):
    contents = file_module.file_read(settings_.BACKEND_FOLDER / 'some_city_names.txt', encoding='utf-8')
    for number in range(number_of_map_files):
        map_file = settings_.PLUGINS_MAPS_FOLDER / str(settings_.MAP_FILE_FORMATTED.format(map_name=random.choice(contents)))
        map_file.touch()


if __name__ == '__main__':
    app_settings = settings.Settings()
    create_folders(check_for_folders(app_settings))
    create_files(check_for_files(app_settings))
    # create_save_files(10, 'Test')
    create_city_files(app_settings, 5)
    create_theme_files(app_settings, 3)
    create_mod_files(app_settings, 4)
    create_asset_files(app_settings, 2)
    create_map_files(app_settings, 4)
    create_plugin_files(app_settings, 2)
