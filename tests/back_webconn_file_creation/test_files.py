from pathlib import Path
from tempfile import TemporaryDirectory

from back_webconn_file_creation.files import (
    check_for_files,
    check_for_folders,
    create_asset_file,
    create_city_file,
    create_files,
    create_folders,
    create_map_file,
    create_mod_file,
    create_plugin_file, create_theme_file
)
from back_webconn_file_creation.settings import Settings


def delete_all_files_in_a_folder_recursively(folder: Path) -> None:
    for files in folder.iterdir():
        if not files.suffix:
            return delete_all_files_in_a_folder_recursively(files)
        files.unlink()
    folder.rmdir()


def test_check_for_files():
    settings = Settings("test_version")
    files = check_for_files(settings)
    FILES = []
    for folders in settings.ALL_FOLDERS:
        for file in folders:
            if file.suffix:
                FILES.append(file)
    assert files == FILES


def test_check_for_folders():
    settings = Settings("test_version")
    folders = check_for_folders(settings)
    FOLDERS = []
    for folders_ in settings.ALL_FOLDERS:
        for folder in folders_:
            if not folder.suffix:
                FOLDERS.append(folder)
    assert folders == FOLDERS


def test_create_folders():
    temp_folder = Path(str(TemporaryDirectory().name))
    list_of_folders = [
        temp_folder / 'test',
        temp_folder / 'var',
        temp_folder / 'nice',
        temp_folder / 'root'
    ]
    list_of_folders.sort()

    create_folders(list_of_folders)
    assert list_of_folders == [dir_ for dir_ in temp_folder.iterdir() if not dir_.suffix]
    delete_all_files_in_a_folder_recursively(temp_folder)


def test_create_files():
    temp_folder = Path(str(TemporaryDirectory().name))
    temp_folder.mkdir(parents=True)
    list_of_files = [
        temp_folder / 'test.txt',
        temp_folder / 'yar.wav',
        temp_folder / 'wav.zip',
        temp_folder / 'test.xyz'
    ]
    list_of_files.sort()
    create_files(list_of_files)
    assert list_of_files == [dir_ for dir_ in temp_folder.iterdir() if dir_.suffix]
    delete_all_files_in_a_folder_recursively(temp_folder)


def test_create_theme_file():
    home_folder = Path(str(TemporaryDirectory().name))
    app_data_folder = Path(str(TemporaryDirectory().name))
    home_folder.mkdir(parents=True)
    app_data_folder.mkdir(parents=True)
    settings = Settings("test_version", home_folder=home_folder, app_data_folder=app_data_folder)
    create_folders(check_for_folders(settings))
    create_theme_file(settings, "Sunny_Summer")
    assert (settings.PLUGINS_THEMES_FOLDER / "Sunny_Summer.theme").exists() is True
    delete_all_files_in_a_folder_recursively(app_data_folder)
    delete_all_files_in_a_folder_recursively(home_folder)


def test_create_asset_file():
    home_folder = Path(str(TemporaryDirectory().name))
    app_data_folder = Path(str(TemporaryDirectory().name))
    home_folder.mkdir(parents=True)
    app_data_folder.mkdir(parents=True)
    settings = Settings("test_version", home_folder=home_folder, app_data_folder=app_data_folder)
    create_folders(check_for_folders(settings))
    create_asset_file(settings, "Sunny_Summer")
    assert (settings.PLUGINS_ASSETS_FOLDER / "Sunny_Summer.asset").exists() is True
    delete_all_files_in_a_folder_recursively(app_data_folder)
    delete_all_files_in_a_folder_recursively(home_folder)


def test_create_city_file():
    home_folder = Path(str(TemporaryDirectory().name))
    app_data_folder = Path(str(TemporaryDirectory().name))
    home_folder.mkdir(parents=True)
    app_data_folder.mkdir(parents=True)
    settings = Settings("test_version", home_folder=home_folder, app_data_folder=app_data_folder)
    create_folders(check_for_folders(settings))
    create_city_file(settings, "Sunny_Summer")
    assert (settings.CITY_FOLDER / "Sunny_Summer.city").exists() is True
    delete_all_files_in_a_folder_recursively(app_data_folder)
    delete_all_files_in_a_folder_recursively(home_folder)


def test_create_map_file():
    home_folder = Path(str(TemporaryDirectory().name))
    app_data_folder = Path(str(TemporaryDirectory().name))
    home_folder.mkdir(parents=True)
    app_data_folder.mkdir(parents=True)
    settings = Settings("test_version", home_folder=home_folder, app_data_folder=app_data_folder)
    create_folders(check_for_folders(settings))
    create_map_file(settings, "Sunny_Summer")
    assert (settings.PLUGINS_MAPS_FOLDER / "Sunny_Summer.map").exists() is True
    delete_all_files_in_a_folder_recursively(app_data_folder)
    delete_all_files_in_a_folder_recursively(home_folder)


def test_create_mod_file():
    home_folder = Path(str(TemporaryDirectory().name))
    app_data_folder = Path(str(TemporaryDirectory().name))
    home_folder.mkdir(parents=True)
    app_data_folder.mkdir(parents=True)
    settings = Settings("test_version", home_folder=home_folder, app_data_folder=app_data_folder)
    create_folders(check_for_folders(settings))
    create_mod_file(settings, "Sunny_Summer")
    assert (settings.PLUGINS_MODS_FOLDER / "Sunny_Summer.mod").exists() is True
    delete_all_files_in_a_folder_recursively(app_data_folder)
    delete_all_files_in_a_folder_recursively(home_folder)


def test_create_plugin_file():
    home_folder = Path(str(TemporaryDirectory().name))
    app_data_folder = Path(str(TemporaryDirectory().name))
    home_folder.mkdir(parents=True)
    app_data_folder.mkdir(parents=True)
    settings = Settings("test_version", home_folder=home_folder, app_data_folder=app_data_folder)
    create_folders(check_for_folders(settings))
    create_plugin_file(settings, "Sunny_Summer")
    assert (settings.PLUGINS_FOLDER / "Sunny_Summer.plugin").exists() is True
    delete_all_files_in_a_folder_recursively(app_data_folder)
    delete_all_files_in_a_folder_recursively(home_folder)
