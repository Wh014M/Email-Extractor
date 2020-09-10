import re


class Get_Email(object):
    def __init__(self):
        # Emails [Private]
        self.__Emails = []
        # Email Regex [Private]
        self.__EMAIL_REGEX = r"""[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"""

    def Search_Email(self, _HTML):
        try:
            # Finding all tags in HTML
            for Email in _HTML.find_all():
                # True if the string matches this type EmailName@DomainName
                if bool(re.match(self.__EMAIL_REGEX, Email.text)):
                    # Add Email to List
                    self.__Emails.append(Email.text)
        except Exception:
            pass

    # Get __Emails
    @property
    def Emails(self):
        return self.__Emails