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


def create_map_files(settings_: settings.Settings, number_of_map_files):
    contents = file_module.file_read(settings_.BACKEND_FOLDER / 'some_city_names.txt', encoding='utf-8')
    for number in range(number_of_map_files):
        if len(list(settings_.MAPS_FOLDER.iterdir())) > 20:
            break
        map_name = random.choice(contents)
        map_file = settings_.MAPS_FOLDER / str(settings_.MAP_FILE_FORMATTED.format(map_name=map_name))
        map_file.touch()
        create_save_files(settings_, 3, map_name)


if __name__ == '__main__':
    app_settings = settings.Settings()
    create_folders(check_for_folders(app_settings))
    create_files(check_for_files(app_settings))
    # create_save_files(10, 'Test')
    create_map_files(app_settings, 5)
