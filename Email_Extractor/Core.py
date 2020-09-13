import requests

from Get_Links import Get_Links
from Get_Email import Get_Email
from bs4 import BeautifulSoup
from tqdm import tqdm


class Core(object):
    def __init__(self):
        self.__Get_Email = Get_Email()
        self.__Get_Links = Get_Links()
        self.__Emails = []

    def URL(self, _URL):
        try:
            # Search Links
            self.__Get_Links.Search_Links(_URL)
            for Link in tqdm(
                set(self.__Get_Links._Get_Links__All_Links), desc=">>> " + _URL
            ):
                # True if the link starts with HTTP or WWW
                if Link.startswith(("http", "www")):
                    # Get HTML
                    HTML = BeautifulSoup(
                        requests.get(Link).text, "html.parser")
                    # Search Email
                    self.__Get_Email.Search_Email(HTML)
                else:
                    # Get HTML
                    HTML = BeautifulSoup(requests.get(
                        _URL + Link).text, "html.parser")
                    # Search Email
                    self.__Get_Email.Search_Email(HTML)
            # Add Emails to List
            self.__Emails += set(self.__Get_Email._Get_Email__Emails)
        except Exception:
            pass

    @property
    def Emails(self):
        return self.__Emails
