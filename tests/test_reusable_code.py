import os

from src.reusable_code import user_writer


def test_users_writer(tmp_path, capsys):
    user_writer(os.path.join(str(tmp_path), 'premium.txt'), 'premium', 10000, 1000000, 25)
    assert capsys.readouterr().out == 'Done'
