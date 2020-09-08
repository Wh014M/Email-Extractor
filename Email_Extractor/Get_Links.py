import requests
from bs4 import BeautifulSoup
from Get_Email import Get_Email


class Get_Links(object):
    # Constructor
    def __init__(self, _Url):

        # Url [Private]
        self.__Url = _Url

    # Search Links
    def Search_Links(self):
        try:
            # Get HTML
            _HTML = BeautifulSoup(
                requests.get(self.__Url).text, 'html.parser')

            # Finding links in HTML <a href=""></a>
            self.__All_Links = [a.attrs.get('href')
                                for a in _HTML.select('a[href]')]

            # Remove Duplicates
            self.__All_Links = set(self.__All_Links)
        except Exception:
            pass

    # Sort Url
    def Sort_Url(self):
        # Get_Email Class Instance [Object]
        Email = Get_Email()

        try:
            # Iterating over references in a loop
            for _Link in self.__All_Links:
                # Checks URL [HTTP or WWW]
                if _Link.startswith("http") or _Link.startswith("www"):

                    # Get HTML
                    _HTML = BeautifulSoup(
                        requests.get(_Link).text, 'html.parser')

                    # Search Email
                    Email.Search_Email(_HTML)
        except Exception:
            pass
