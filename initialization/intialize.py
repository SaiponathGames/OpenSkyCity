class OpenCity:
    build = "0.00.000.0141"
    Version = "v1.4.1"
    Premium = True
    Special_sandbox = True
    debug = False
    Name = "OpenCity"


if __name__ == '__main__':
    from files_and_folders.files_and_folder_creator import folder_and_file_creator as ft
    from premium.premium_test import premium_test as pt
    from special_sandbox.special_sandbox_mode_test import special_sandbox_mode_test as st
    import opencity_kivy.splashscreen as ss
    print("{} {} \nBuild ({}) \n\n\n".format(OpenCity.Name, OpenCity.Version, OpenCity.build))
    ft()
    print()
    pt()
    print()
    st()
    print()
    ss.OpenCity123().run()
