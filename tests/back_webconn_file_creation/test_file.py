from pathlib import Path
from tempfile import TemporaryDirectory, TemporaryFile

import pytest
from back_webconn_file_creation.file import binary_file_append, binary_file_copy, binary_file_read, binary_file_write, file_append, file_copy, file_read, file_write


@pytest.mark.parametrize(['content', 'as_list', 'result'], [["Hello World!", False, "Hello World!"], ["Hello World", True, ["Hello World"]]])
def test_file_read(content, as_list, result):
    temp_file = Path(str(TemporaryFile().name))
    temp_file.open('w').write(str(content))
    assert file_read(temp_file, as_list=as_list) == result
    temp_file.unlink()


def test_file_write():
    temp_file = Path(str(TemporaryFile().name))
    file_write(temp_file, "Hello World!")
    assert temp_file.open('r').read().replace('\n', '') == "Hello World!"
    temp_file.unlink()


@pytest.mark.parametrize(['content', 'result'], [[["Hello World!", "Test One!"], "Hello World!Test One!"], [["Hello World!\n", "Test One!"], "Test One!"]])
def test_file_append(content, result):
    temp_folder = Path(str(TemporaryDirectory().name))
    temp_file = (temp_folder / 'test.txt')
    temp_folder.mkdir(parents=True)
    temp_file.touch()
    temp_file.open('w').write(content[0])
    file_append(temp_file, content[1])
    assert file_read(temp_file, as_list=True)[-1] == result
    temp_file.unlink()


def test_file_copy():
    temp_file_1 = Path(str(TemporaryFile().name))
    temp_file_1.open('w').write("Hello, this is a test!")
    temp_file_2 = Path(str(TemporaryFile().name))
    file_copy(temp_file_1, temp_file_2)
    assert temp_file_2.open().read() == "Hello, this is a test!"
    temp_file_1.unlink()
    temp_file_2.unlink()


@pytest.mark.parametrize(['content', 'as_list', 'result'], [[b"Hello World!", False, b"Hello World!"], [b"Hello World", True, [b"Hello World"]]])
def test_binary_file_read(content, as_list, result):
    temp_file = Path(str(TemporaryFile().name))
    temp_file.open('wb').write(bytes(content))
    assert binary_file_read(temp_file, as_list=as_list) == result
    temp_file.unlink()


def test_binary_file_write():
    temp_file = Path(str(TemporaryFile().name))
    binary_file_write(temp_file, b"Hello World!")
    assert temp_file.open('rb').read().replace(b'\n', b'') == b"Hello World!"
    temp_file.unlink()


@pytest.mark.parametrize(['content', 'result'], [[[b"Hello World!", b"Test One!"], b"Hello World!Test One!"], [[b"Hello World!\n", b"Test One!"], b"Test One!"]])
def test_binary_file_append(content, result):
    temp_folder = Path(str(TemporaryDirectory().name))
    temp_file = (temp_folder / 'test.txt')
    temp_folder.mkdir(parents=True)
    temp_file.touch()
    temp_file.open('wb').write(content[0])
    binary_file_append(temp_file, content[1])
    assert binary_file_read(temp_file, as_list=True)[-1] == result
    temp_file.unlink()


def test_binary_file_copy():
    temp_file_1 = Path(str(TemporaryFile().name))
    temp_file_1.open('wb').write(b"Hello, this is a test!")
    temp_file_2 = Path(str(TemporaryFile().name))
    binary_file_copy(temp_file_1, temp_file_2)
    assert temp_file_2.open("rb").read() == b"Hello, this is a test!"
    temp_file_1.unlink()
    temp_file_2.unlink()
