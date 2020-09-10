import requests
from bs4 import BeautifulSoup


class Get_Links(object):
    def __init__(self, _Url):
        # Url [Private]
        self.__Url = _Url

        # All Links [Private]
        self.__All_Links = []

    def Search_Links(self):
        try:
            # Get HTML
            HTML = BeautifulSoup(requests.get(self.__Url).text, "html.parser")

            # Finding links in HTML <a href=""></a>
            self.__All_Links = [a.attrs.get("href") for a in HTML.select("a[href]")]
        except Exception:
            pass

    # Get __All_Links
    @property
    def All_Links(self):
        return self.__All_Links
