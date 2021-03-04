try:
    from src.Colors import TextColor
    import src.libs as libs
    from .ReconMask import MainMask
    from .modules.GetGeoInfos import GetGeoInfs
    from .modules.GetCodeLang import StartSearching
    import os
    import sys
except Exception as error:
    raise SystemExit, "\033[31m" + "Something wrong in importing the library in WebsiteReconMainHandler" + "\033[0m"


def SubMenu():
    MainMask()

    print

    sys.stdout.write(TextColor.CVIOLET + '\t\t[1]. Get geo info')
    print '\t[2]. Get language of site'

    if not os.path.exists('./outputs/Info-Gathering/WebRecon'):
        os.mkdir('./outputs/Info-Gathering/WebRecon')


def WebSiteReconMain():
    SubMenu()

    print

    selectedSubMenuItem = raw_input(TextColor.CVIOLET + '~fhack/InfoGathering/[WebRecon]# ' + TextColor.WHITE)

    if selectedSubMenuItem == '1':
        GetGeoInfs()
    elif selectedSubMenuItem == '2':
        StartSearching()
    elif selectedSubMenuItem == '0':
        print
        return
