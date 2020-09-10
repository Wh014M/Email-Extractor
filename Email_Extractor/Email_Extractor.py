import os
from Core import Core


def main():
    try:
        # Core Class Instance
        _Core = Core()
        # File
        File = open(input("File: "), 'r')
        # Urls
        Urls = [Url.strip() for Url in File.readlines()]
        for Url in set(Urls):
            # Set Url
            _Core.Url(Url)
        # Clear Console
        Clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
        Clear()
        # Output
        for Email in set(_Core._Core__Emails):
            print(Email)
    except Exception:
        pass


if __name__ == "__main__":
    main()
