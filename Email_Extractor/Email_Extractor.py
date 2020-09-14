from File_Write import File_Write
from File_Read import File_Read
from Core import Core


def main():
    try:
        # Read text from file
        _File_Read.File_R()
        for URL in set(_File_Read._File_Read__URL):
            _Core.URL(URL)
        # Write text to file
        _File_Write.File_W(set(_Core._Core__Emails))
    except Exception:
        pass


if __name__ == "__main__":
    _File_Write = File_Write()
    _File_Read = File_Read()
    _Core = Core()
    print(" ___                       ___     ___  __        __  ___  __   __")
    print("|__   |\/|  /\  | |    __ |__  \_/  |  |__)  /\  /  `  |  /  \ |__)")
    print("|___  |  | /~~\ | |___    |___ / \  |  |  \ /~~\ \__,  |  \__/ |  \ \n")
    main()
