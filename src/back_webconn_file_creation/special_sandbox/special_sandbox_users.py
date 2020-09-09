from .. import reusable_code, settings

settings_ = settings.Settings()


def special_sandbox_mode_users_writer():
    reusable_code.user_writer(settings_.SPECIAL_SANDBOX_APPDATA_TXT_FILE, 'special sandbox', settings_.SPECIAL_SANDBOX_ID_START, settings_.SPECIAL_SANDBOX_ID_END,
                              settings_.SPECIAL_SANDBOX_KEY_LENGTH)


def special_sandbox_mode_users_checker():
    return reusable_code.users_checker('special sandbox', settings_.SPECIAL_SANDBOX_APPDATA_TXT_FILE)
