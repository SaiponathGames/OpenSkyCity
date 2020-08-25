import pathlib
import random

import file as file_module
from typing import List

import settings


def check_for_files() -> List[pathlib.Path]:
    FILES = []
    for folders in settings.ALL_FOLDERS:
        for file in folders:
            # print(file.is_file())
            if file.suffix:
                # print(file, "in if")
                FILES.append(file)
    return FILES


def check_for_folders() -> List[pathlib.Path]:
    FOLDERS = []
    for folders in settings.ALL_FOLDERS:
        for folder in folders:
            if not folder.suffix:
                FOLDERS.append(folder)
    return FOLDERS


def create_folders(folders: List[pathlib.Path]):
    for folder in folders:
        if not folder.exists():
            folder.mkdir(exist_ok=True)


def create_files(files: List[pathlib.Path]):
    for file in files:
        if not file.exists():
            if file.name.startswith(('save', '{}.map')):
                continue
            file.touch()


def create_save_files(number_of_save_files, map_name):
    for i in range(number_of_save_files):
        save_file = settings.SAVES_FOLDER / str(settings.SAVES_FILE_FORMATTED.format(number=i, map_name=map_name))
        save_file.touch()


def create_map_files(number_of_map_files):
    contents = file_module.file_read(settings.ROOT_FOLDER / 'some_city_names.txt', encoding='utf-8')
    for number in range(number_of_map_files):
        if len(list(settings.MAPS_FOLDER.iterdir())) > 20:
            break
        map_file = settings.MAPS_FOLDER / str(settings.MAP_FILE_FORMATTED.format(map_name=random.choice(contents)))
        map_file.touch()


if __name__ == '__main__':
    create_folders(check_for_folders())
    create_files(check_for_files())
    create_save_files(10, 'Test')
    create_map_files(10)
