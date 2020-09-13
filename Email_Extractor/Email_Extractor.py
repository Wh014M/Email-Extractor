from Core import Core
from File_Read import File_Read
from File_Write import File_Write


def main():
    try:
        # Read text from file
        _File_Read.File_R()
        for URL in set(_File_Read._File_Read__URL):
            _Core.URL(URL)
        # Write text to file
        _File_Write.File_W(_Core._Core__Emails)
    except Exception:
        pass


if __name__ == "__main__":
    _Core = Core()
    _File_Read = File_Read()
    _File_Write = File_Write()
    print(" ___                       ___     ___  __        __  ___  __   __")
    print("|__   |\/|  /\  | |    __ |__  \_/  |  |__)  /\  /  `  |  /  \ |__)")
    print("|___  |  | /~~\ | |___    |___ / \  |  |  \ /~~\ \__,  |  \__/ |  \ \n")
    main()
