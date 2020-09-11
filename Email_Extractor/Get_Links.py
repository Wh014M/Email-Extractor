import requests
from bs4 import BeautifulSoup


class Get_Links(object):
    def __init__(self):
        # All Links [Private]
        self.__All_Links = []

    def Search_Links(self, _URL):
        try:
            # Get HTML
            HTML = BeautifulSoup(requests.get(_URL).text, "html.parser")
            # Finding links in HTML <a href=""></a>
            self.__All_Links = [a.attrs.get("href")
                                for a in HTML.select("a[href]")]
        except Exception:
            pass

    @property
    def All_Links(self):
        return self.__All_Links
