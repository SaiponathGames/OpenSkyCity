from .. import reusable_code, settings


def premium_users_writer():
    reusable_code.user_writer(settings.PREMIUM_APPDATA_TXT_FILE, 'premium', settings.PREMIUM_ID_START, settings.PREMIUM_ID_END, settings.PREMIUM_KEY_LENGTH)


def premium_users_checker():
    return reusable_code.users_checker('premium', settings.PREMIUM_APPDATA_TXT_FILE)
