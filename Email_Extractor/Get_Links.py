import requests
import re
from bs4 import BeautifulSoup
from Get_Email import Get_Email

class Get_Links(object):

    # Constructor
    def __init__(self, _Url):

        # Url [Public]
        self.Url = _Url

    # Search Links
    def Search_Links(self):

        # Get HTML
        _Response = requests.get(self.Url)

        # HTML 
        _Beautiful_Soup = BeautifulSoup(_Response.text, 'html.parser')

        # Finding a Link in HTML
        self.__All_Links = [a.attrs.get('href') for a in _Beautiful_Soup.select('a[href]')]
        
        # Remove Duplicates
        self.__All_Links = set(self.__All_Links)

        # Get_Email [Object]
        Email = Get_Email()

        for _Link in self.__All_Links:

            # Check Url
            if(_Link.startswith("http") or _Link.startswith("www")):

                # Get HTML
                _Response = requests.get(_Link)

                # HTML 
                _Beautiful_Soup = BeautifulSoup(_Response.text,'html.parser')

                # Search Email
                Email.Search_Email(_Beautiful_Soup)