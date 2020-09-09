import requests
from bs4 import BeautifulSoup
from Get_Email import Get_Email


class Core(object):
    # Constructor
    def __init__(self, _All_Links):
        # All Links [Private]
        self.__All_Links = _All_Links

        # Get_Email Class Instance [Object]
        self.Email = Get_Email()

    # Links
    def Links(self):
        try:
            # Iterating over references in a loop
            for _Link in self.__All_Links:
                # Checks URL [HTTP or WWW]
                if _Link.startswith("http") or _Link.startswith("www"):

                    # Get HTML
                    _HTML = BeautifulSoup(
                        requests.get(_Link).text, 'html.parser')

                    # Search Email
                    self.Email.Search_Email(_HTML)
        except Exception:
            pass
