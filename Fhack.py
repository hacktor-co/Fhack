#!usr/bin/env python

try:
    from src.Colors import TextColor
    from core.menu import ShowItems
    from src.Mask import MaskTerminal
    from src import libs
    from CoreManage import databasemanage
    from InfoGathering.ManageInfoGathering import mainInfoGathering
    from Config.FhackInitializer import InitFhack
    from NetworkPentest.mainNetworkPentest import mainNetworkPentest
    from CreateMalware.mainCreateMalware import mainCreateMalware
    from WebAttack.mainWebAppPentest import mainWebAttack
except Exception as err:
    raise SystemExit, TextColor.RED + str('\nSome thing wrong in libraries: %s\n' % err) + TextColor.WHITE

reload(libs.sys)
libs.sys.setdefaultencoding('utf-8')  # this line set the all encoding of project to utf-8

define_MAX_MenuItem = 6
define_MAX_MenuItem_WEB_ATTACK = 4


def Switch_Menu_Item(number):
    subMenu = ShowItems()
    if number == '1':  # web attack menu items
        subMenu.ItemOfWebAttack()
        mainWebAttack()
    # --------------------------------------------------
    elif number == '2':
        subMenu.ItemOfCreateMalware()
        mainCreateMalware()
    # --------------------------------------------------
    elif number == '4':
        subMenu.ItemOfNetworkPentest()
        mainNetworkPentest()
    # --------------------------------------------------
    elif number == '6':
        subMenu.ItemOfInformationGathering()
        mainInfoGathering()
    # --------------------------------------------------
    elif number == '7':
        subMenu.ItemOfManageDatabase()
        databasemanage.StartManageDBs()
    # --------------------------------------------------
    elif number == '0':
        raise SystemExit, '<-- Good Luck hacker -->'
    else:
        print 'On construction'


def main():
    InitFhack()

    global define_MAX_MenuItem

    mainMask = MaskTerminal()
    mainMask.ShowMask()
    mainMenu = ShowItems()

    while True:
        mainMenu.ShowMenu()
        choose = raw_input(TextColor.BLUE + str('Fhack~# ') + TextColor.WHITE)

        if choose > define_MAX_MenuItem and not choose.isdigit():
            print TextColor.WARNING + '\n[*]Please Enter <1-6>\n' + TextColor.WHITE
        else:
            Switch_Menu_Item(choose)


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print TextColor.RED + str(err) + TextColor.WHITE
    except KeyboardInterrupt:
        print TextColor.PURPLE + str('\nGood luck :)\n') + TextColor.WHITE
