try:
    from src.Colors import TextColor
    from .ReverseIpLookUp.reverseip import ReverseIpLookUp
    from .simple_tools.whois import whois
    from .simple_tools.FindSubDomains import Main_FindSubdomain
    from .WebSiteRecon.WebRconMainHandler import WebSiteReconMain
    import os
except Exception as err:
    raise SystemError, '\033[31m' + 'Some error happened please check it: %s' % err + '\033[0m'


# main function that control all item in information gathering
def mainInfoGathering():
    print
    selectedItem = raw_input(TextColor.GREEN + 'Fhack ~/Info-Gathering/# ' + TextColor.WHITE)
    ManageSelectedItems(selectedItem)
    print


def ManageSelectedItems(selectedItem):

    if not os.path.exists('./outputs/Info-Gathering'):
        os.mkdir('./outputs/Info-Gathering')

    if selectedItem == '1':
        ReverseIpLookUp()
    elif selectedItem == '2':
        whois()
    elif selectedItem == '3':
        print TextColor.WHITESMOKE + "[-] Please wait this module on construction"
    elif selectedItem == '4':
        Main_FindSubdomain()
    elif selectedItem == '5':
        WebSiteReconMain()
    elif selectedItem == "0":
        print
        return
    else:
        print TextColor.RED + '[-] Please select from menu' + TextColor.WHITE
