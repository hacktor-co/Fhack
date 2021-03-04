# -*- coding: utf-8 -*-
try:
    import requests as reqs
    import src.libs as lib
    from src.Colors import TextColor
    from Config.WebConfig import define_headerdata
    from multiprocessing import Pool, cpu_count
    from core.managesqlitedb import DirectoryFinerDB
    import os
except Exception as err:
    raise SystemExit, TextColor.RED + "Something is wrong: %s" % err + TextColor.WHITE

reqs.packages.urllib3.disable_warnings()

def run_thread(url_list):
    response = reqs.get(url=url_list, headers=define_headerdata,
                        verify=False).status_code
    if response == 200:
        print TextColor.GREEN + '[+] Found %s => status code:ls' \
                                ' %s' % (url_list, response) + TextColor.WHITE
        fileName = lib.urlparse.urlparse(url_list)[1]
        with open('./outputs/DirFinder/' + str(fileName), 'a+') as file:
            file.write(url_list + "\n")
    else:
        print TextColor.RED + '[-] Not found %s => status code: %s' % (url_list, response) + TextColor.WHITE


def start_check_url(url_list_items, rhost):
    if rhost.endswith('/'):
        rhost = rhost[0: len(rhost) - 1]

    finalUrls = list()
    for item in url_list_items:
        finalUrls.append(rhost + "/" + item.strip('\n'))

    # create multi thread and then check urls that exists or not
    pool = Pool(processes=cpu_count() + 4)
    pool.map(run_thread, finalUrls)
    pool.join()

    print
    print TextColor.GREEN + "[+] Done !!!" + TextColor.WHITE


def Menu(rhost):
    print TextColor.CYAN + str('|----- Directory attack -----|')
    print '|1. Use wordlist <Dictionary>'
    print '|2. Use fhack database <Dictionary>'
    print '|3. Use bruteforce' + TextColor.WHITE

    if not os.path.exists('./outputs/DirFinder'):
        os.mkdir('./outputs/DirFinder')

    if not os.path.exists('./outputs/DirFinder/' + lib.urlparse.urlparse(rhost)[1]): #check that destination file is exist or  not
        open('./outputs/DirFinder/' + lib.urlparse.urlparse(rhost)[1], 'a')#if not we create that file


def CheckRhost():
    """ Function
        in this function first we check web site which is online or not
        then show menu to start
    """
    print
    rhost = raw_input(TextColor.PURPLE + ' ==> Enter url (e.g: http://example.com): ' + TextColor.WHITE)
    print TextColor.WARNING + str('[*] Checking RHOST --> %s' % rhost) + TextColor.WHITE
    try:
        reqs.packages.urllib3.disable_warnings()
        response = reqs.get(url=rhost, headers=define_headerdata,
                            verify=False, allow_redirects=False)
        if response.status_code == 200:
            print TextColor.GREEN + str('[+] rhost has been set!! -- Done.') + TextColor.WHITE
            lib.sleep(.5)
            Menu(rhost)
            return rhost
        else:
            print TextColor.RED + 'Something wrong with rhost can not reach the rhost' + TextColor.WHITE
            return None
    except Exception as err:
        print TextColor.RED + str("Something is wrong %s" % err) + TextColor.WHITE
        return None


def WithWorldList(wordlist, rhost):
    path_list = set()
    print TextColor.WARNING + str('[*] please wait to load lines of %s' % wordlist) + TextColor.WHITE
    with open(wordlist, 'r') as file:
        for item in file.readlines():
            if item.startswith('/'):
                path_list.add(item[1: len(item)])
            else:
                path_list.add(item)
    print TextColor.GREEN + str('[+] All items add to the list succcessfully!! Done.') + TextColor.WHITE

    print TextColor.CYELLOWBG2 + TextColor.RED + str('[+] Beginning scan') + TextColor.WHITE
    start_check_url(path_list, rhost)


def UseFhackDataBase(rhost):
    """
    If user select the fhack database for searching directories then
    script run this function and select all item in database then test them
    :param rhost: the web site url
    :return: nothing
    """

    allItems = DirectoryFinerDB().__raw_query__('select * from tbl_dirs')

    listUrls = list()
    for item in allItems:
        listUrls.append(item[1])

    print TextColor.GREEN + str('[+] All items add to the list succcessfully!! Done.') + TextColor.WHITE

    print TextColor.CYELLOWBG2 + TextColor.RED + str('[+] Beginning scan') + TextColor.WHITE
    start_check_url(listUrls, rhost)


def Start():
    rhost = CheckRhost()  # first we check that rhost is online or not

    choice = raw_input(TextColor.PURPLE + 'Fhack/DirFinder/#Enter your choice: ' + TextColor.WHITE)

    if choice == "1":
        filePath = raw_input(TextColor.HEADER + str('[*] Enter wordlist path: ') + TextColor.WHITE)
        WithWorldList(filePath, rhost)
    elif choice == "2":
        UseFhackDataBase(rhost)
    elif choice == "3":
        # todo = Work on directory bruteforce
        print 'not work yet !! email: topcodermc@gmail.com'
        pass


if __name__ == "__main__":
    try:
        Start()
    except KeyboardInterrupt:
        raise SystemExit, "Good luck"
