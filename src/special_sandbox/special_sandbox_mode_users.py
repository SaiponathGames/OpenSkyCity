from src import reusable_code, settings


def special_sandbox_mode_users_writer():
    reusable_code.user_writer(settings.SPECIAL_SANDBOX_APPDATA_TXT_FILE, 'special sandbox', settings.SPECIAL_SANDBOX_ID_START, settings.SPECIAL_SANDBOX_ID_END,
                              settings.SPECIAL_SANDBOX_KEY_LENGTH)


def special_sandbox_mode_users_checker():
    return reusable_code.users_checker('special sandbox', settings.SPECIAL_SANDBOX_APPDATA_TXT_FILE)
