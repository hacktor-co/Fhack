"""
    - created on march/9/2019
    - author topcodermc
    - with this module we can findout what database that web application used
"""
# -*- coding: utf-8 -*-
try:
    import requests as reqs
    from src.Colors import TextColor

    from InfoGathering.WebSiteRecon.modules.GetCodeLang import FileExtensions
except Exception as error:
    raise SystemExit, TextColor.RED + '[-] We have error in sqlinjection->modules->TechnologyRecon' + TextColor.WHITE


class TechnologyRecon:

    def __init__(self, url):
        self.url = url


    def CheckLang(self):
        """ get the programming language of the web application """
        if FileExtensions(self.url) is not 'none':
            return FileExtensions(self.url)
