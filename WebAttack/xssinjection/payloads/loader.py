try:
    from src.Colors import TextColor
    from core.managesqlitedb import WebAttackDb
    from Utilities.BaseClass import ShowProgress
except Exception as err:
    raise SystemExit, '%s' % err


def XssTypeOfDepth():
    pass


def MakeSelection():
    print TextColor.WHITESMOKE + "\t\t => [1]. Use Fhack database for payloads"
    print "\t\t => [2]. Use payloads file (from ./payloads/payloads)"
    print "\t\t => [3]. Use my single payload"
    print "\t\t => [4]. Exit " + TextColor.WHITE

    choice = raw_input(TextColor.CVIOLET + "Fhack/WebAttack/XSS/# Make your choice (1-3): " + TextColor.WHITE)

    if choice == "1":
        return UseFhackDataBase()
    elif choice == "2":
        UsePayloadFiles()
    elif choice == "3":
        UseSinglePayload()
    elif choice == '4':
        return None


def UseFhackDataBase():
    allItems = WebAttackDb().__raw_query__('select * from tbl_xss_payloads')

    listUrls = list()

    counter = 0
    for item in allItems:
        ShowProgress(TextColor.CYELLOW + 'Loading the payloads', counter)
        listUrls.append(item[1])
        counter += 1

    print
    print TextColor.WARNING + str("All payload length that we load: %d" % len(allItems)) + TextColor.WHITE
    print TextColor.GREEN + str('[+] All items add to the list succcessfully!! Done.') + TextColor.WHITE

    print TextColor.CYELLOWBG2 + TextColor.RED + str('[+] Beginning scan') + TextColor.WHITE

    return listUrls


def UsePayloadFiles():
    pass


def UseSinglePayload():
    pass
