import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from Get_Links import Get_Links
from Get_Email import Get_Email


class Core(object):
    def __init__(self, _Url):
        # Get_Email Class Instance [Private]
        self.__Email = Get_Email()

        # Get_Links Class Instance [Private]
        self.__Links = Get_Links(_Url)

        # Url [Private]
        self.__Url = _Url

    def Links(self):
        try:
            # Search Links
            self.__Links.Search_Links()

            # Iterating over references in a loop
            for Link in tqdm(set(self.__Links._Get_Links__All_Links), desc=self.__Url):
                # True if the link starts with HTTP or WWW
                if Link.startswith(("http", "www")):
                    # Get HTML
                    HTML = BeautifulSoup(requests.get(Link).text, "html.parser")

                    # Search Email
                    self.__Email.Search_Email(HTML)

                else:
                    # Get HTML
                    HTML = BeautifulSoup(requests.get(self.__Url + Link).text, "html.parser")

                    # Search Email
                    self.__Email.Search_Email(HTML)

            for Email in set(self.__Email._Get_Email__Emails):
                print(Email)
        except Exception:
            pass