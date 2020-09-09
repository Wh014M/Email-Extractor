from Get_Links import Get_Links
from Core import Core


# Main
def main():
    # Get_Links Class Instance
    _Links = Get_Links("https://limon.kg/")

    # Search Links
    _Links.Search_Links()

    # Core Class Instance
    _Core = Core(_Links._Get_Links__All_Links, "https://limon.kg/")

    # Links
    _Core.Links()


# Check
if __name__ == "__main__":
    main()
