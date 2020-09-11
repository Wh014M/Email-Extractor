class File_Read(object):
    def __init__(self):
        # URL [Private]
        self.__URL = []

    def File_R(self):
        try:
            # Read text from file
            with open(input(">>> File with URL: "), "r") as File:
                # List with URL
                self.__URL = [Url.strip() for Url in File.readlines()]
        except Exception:
            pass

    @property
    def URL(self):
        return self.__URL
