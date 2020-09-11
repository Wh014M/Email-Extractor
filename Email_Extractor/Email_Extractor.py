from Core import Core
from File_Read import File_Read
from File_Write import File_Write


def main():
    try:
        # Logo
        logo()
        # Core Class Instance
        _Core = Core()
        # File_Read Class Instance
        _File_Read = File_Read()
        # File_Write Class Instance
        _File_Write = File_Write()
        # Read text from file
        _File_Read.File_R()
        for URL in set(_File_Read._File_Read__URL):
            # Set Url
            _Core.Url(URL)
        # Write text to file
        _File_Write.File_W(_Core._Core__Emails)
    except Exception:
        pass

def logo():
    print(r'''
 ___                       ___     ___  __        __  ___  __   __  
|__   |\/|  /\  | |    __ |__  \_/  |  |__)  /\  /  `  |  /  \ |__) 
|___  |  | /~~\ | |___    |___ / \  |  |  \ /~~\ \__,  |  \__/ |  \ 
                                                                    
''')
if __name__ == "__main__":
    main()
