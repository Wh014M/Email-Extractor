class File_Read(object):
    def __init__(self):
        self.__URL = []

    def File_R(self):
        try:
            # Read text from file
            with open(input(">>> File with URL: "), "r") as File:
                # List with URL
                self.__URL = [URL.strip() for URL in File.readlines()]
        except Exception:
            pass

    @property
    def URL(self):
        return self.__URL
