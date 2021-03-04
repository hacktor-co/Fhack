try:
    from src.Colors import TextColor
    import os
    from core.managesqlitedb import DirectoryFinerDB
    import src.libs as lib
    from core.menu import ShowItems
except Exception as err:
    TextColor.RED + str(err) + TextColor.WHITE


def StartManageDBs():
    subMenu = ShowItems()
    while True:

        choice = raw_input(TextColor.CVIOLET + str('Enter your choice<1-5> (0) to exit: ') + TextColor.WHITE)

        if choice == '1':  # show all database that fhack use
            ShowAllDBs()
        elif choice == '2':  # insert data to database
            all_tables = ShowAllDBs()
            db = raw_input(TextColor.CVIOLET + str("Which table do you want to insert data?: ") + TextColor.WHITE)
            try:
                InsertMethod(all_tables[int(db)])
            except Exception as err:
                print TextColor.RED + str('Wrong: %s' % (err)) + TextColor.WHITE
                break
        elif choice == '3':  # raw query for sqlite
            all_tables = ShowAllDBs()
            db = raw_input(TextColor.CVIOLET + str("Which table do you want to use raw query?: ") + TextColor.WHITE)
            try:
                RawQuery(all_tables[int(db)])
            except Exception as err:
                print TextColor.RED + str('Wrong: %s' % err) + TextColor.WHITE
                break

        elif choice == '0':
            print
            print
            break
        else:
            print 'Please Select <1-5>'

        subMenu.ItemOfManageDatabase()


def ShowAllDBs():
    """
    In this function we search for all database that fhack use
    :return:
    """
    # list_of_files = {}
    list_of_alldbs = list()
    for (dirpath, dirnames, filenames) in os.walk('.'):
        for filename in filenames:
            # list_of_files[filename] = os.sep.join([dirpath, filename])
            if filename.endswith('.db'):
                list_of_alldbs.append(filename)

    print

    counter = 0
    make_table = lib.mytable(['Count', 'Name'])
    for item in list_of_alldbs:
        make_table.add_row([str(counter), item])
        counter += 1
    print TextColor.CYELLOW + str(make_table) + TextColor.WHITE + "\n"

    return list_of_alldbs


def InsertMethod(table):
    if str(table) == 'dirbrute.db':

        print TextColor.CYAN + str("\t\t[1].Add file to it") + TextColor.WHITE
        print TextColor.CYAN + str("\t\t[2].Add one record to it") + TextColor.WHITE

        selectedItem = raw_input("Select one of them: ")

        if selectedItem == '1':
            values = raw_input('Enter your file path<full_path>: ')

            with open(values, 'r') as file:
                for item in file.readlines():
                    try:
                        DirectoryFinerDB().__insert_data__((str(item).strip('\n'),))
                    except:
                        pass

            print TextColor.GREEN + str("\n\nitem added on database successfully\n\n") + TextColor.WHITE

        elif selectedItem == '2':
            item = raw_input('Enter your value: ')
            try:
                DirectoryFinerDB().__insert_data__((str(item),))
            except Exception as err:
                print TextColor.RED + str('Something is wrong: %s' % err) + TextColor.WHITE
            print TextColor.GREEN + str("\n\nitem added on database successfully\n\n") + TextColor.WHITE
        elif selectedItem == '0':
            return
        else:
            raise SystemExit, TextColor.RED + str("\n\nSomething is wrong please enter 1-2\n\n") + TextColor.WHITE


def RawQuery(db):
    if str(db) == 'dirbrute.db':

        list_of_allTables = DirectoryFinerDB().__raw_query__("SELECT name FROM sqlite_master WHERE type='table';")

        counter = 0
        make_table = lib.mytable(['Count', 'Table Name'])
        for item in list_of_allTables:
            make_table.add_row([str(counter), item[0]])
            counter += 1
        print TextColor.CYELLOW + str(make_table) + TextColor.WHITE + "\n"

        while True:
            query = raw_input(
                TextColor.CVIOLET + str("FHack/DbManagement/#Enter raw query ('exit' to return): ") + TextColor.WHITE)

            if query == "exit":
                break

            list_of_allOutPut = DirectoryFinerDB().__raw_query__(query)

            counter = 0
            make_table = lib.mytable(['Count', 'Value'])
            for item in list_of_allOutPut:
                make_table.add_row([str(counter), item])
                counter += 1
            print TextColor.CYELLOW + str(make_table) + TextColor.WHITE + "\n"
