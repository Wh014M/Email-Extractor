import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from Get_Links import Get_Links
from Get_Email import Get_Email


class Core(object):
    def __init__(self):
        # Get_Email Class Instance [Private]
        self.__Get_Email = Get_Email()
        # Get_Links Class Instance [Private]
        self.__Get_Links = Get_Links()
        # Emails [Private]
        self.__Emails = []

    def Url(self, _URL):
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
            # Add Email to List
            self.__Emails += set(self.__Get_Email._Get_Email__Emails)
        except Exception:
            pass

    @property
    def Emails(self):
        return self.__Emails
