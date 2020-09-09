import re


class Get_Email(object):
    # Constructor
    def __init__(self):
        # Emails [Private]
        self.__Emails = []

        # Email Regex [Private]
        self.__EMAIL_REGEX = r"""[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"""

    # Search Email
    def Search_Email(self, _HTML):
        try:
            # Finding links in HTML <a></a>
            for _Email in _HTML.find_all():
                # True if the string matches this type EmailName@DomainName
                if bool(re.match(self.__EMAIL_REGEX, _Email.text)):
                    # Add Email to List
                    self.__Emails.append(_Email.text)
        except Exception:
            pass

    # Get __Emails
    @property
    def Emails(self):
        return self.__Emails