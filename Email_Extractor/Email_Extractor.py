from Core import Core


def main():
    # Core Class Instance
    _Core = Core()
    # File
    File = open(input("File: "), 'r')
    # Urls
    Urls = [Url.strip() for Url in File.readlines()]
    for Url in set(Urls):
        # Set Url
        _Core.Url(Url)

    for Email in set(_Core._Core__Emails):
        print(Email)


if __name__ == "__main__":
    main()
