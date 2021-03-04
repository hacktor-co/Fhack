try:
    import src.libs as lib
    from .Mask import MASK
    from src.Colors import TextColor
    import json
    import os
    from Config.RecOS import IsOSDarwin
except Exception as err:
    raise SystemError, '\033[0m' + 'Something is wrong with libraries: %s' % err + '\033[0m'


def LOW():  # with some data
    DEFINE_HEADERS = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    try:
        print
        url = raw_input('\033[94m' + '==> Enter site url or ip (e.g.:example.com): ' + '\033[0m')

        if not os.path.exists(
                './outputs/Info-Gathering/' + 'LOW-' + url):  # check that destination file is exist or  not
            open('./outputs/Info-Gathering/' + 'LOW-' + url, 'a')  # if not we create that file

        response = lib.requests.post(url='https://domains.yougetsignal.com/domains.php',
                                     data={
                                         'remoteAddress': url
                                     },
                                     headers=DEFINE_HEADERS, verify=False)

        jsonRes = json.loads(response.text)

        remoteAddress = jsonRes['remoteAddress']
        remoteIpAddress = jsonRes['remoteIpAddress']

        print '\033[34m' + "[+] Remote address is: %s" % remoteAddress + '\033[0m'
        print '\033[34m' + "[+] Remote Ip address is: %s" % remoteIpAddress + '\033[0m'

        print
        print '\033[31m' + '-----------------Domains on this Server-----------------' + "\033[0m"
        print

        with open('./outputs/Info-Gathering/' + 'LOW-' + url, 'a') as file:
            for item in jsonRes['domainArray']:
                print '\033[33m' + str(item[0]) + '\033[0m'
                file.write(str(item[0]) + '\n')
    except Exception:
        raise SystemExit, '\033[31m' + 'Something is wrong: check your input or email topcodermc@gmail.com' + '\033[0m'

    print '================================================'


def HIGH():
    DEFINE_HEADERS = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    try:

        print
        url = raw_input('\033[94m' + '==> Enter site url or ip (e.g.:example.com): ' + '\033[0m')

        if not os.path.exists(
                './outputs/Info-Gathering/' + 'HIGH-' + url):  # check that destination file is exist or  not
            open('./outputs/Info-Gathering/' + 'HIGH-' + url, 'a')  # if not we create that file

        response = lib.requests.get(url='https://viewdns.info/reverseip/',
                                    params={'host': url, 't': '1'},
                                    headers=DEFINE_HEADERS, verify=False)

        start = response.content.find('Last Resolved Date')
        end = response.content.find('</td></tr></table>')
        result = ""
        for item in xrange(start, end):
            result += response.content[item]

        soup = lib.BS(result, "html.parser")

        list_of_cells = []
        for cell in soup.find_all('td'):
            text = cell.text.strip()
            list_of_cells.append(text)

        counter = 0
        while counter < len(list_of_cells):
            if counter % 2 == 0:
                print '\033[33m' + list_of_cells[counter] + '\033[0m'
                with open('./outputs/Info-Gathering/' + 'HIGH-' + url, 'a') as file:
                    file.write(str(list_of_cells[counter]) + '\n')
            counter += 1
            # else: # get Last Resolved Date
            #     print list_of_cells[counter]
    except Exception as error:
        raise SystemExit, '\033[31m' + 'Something is wrong: %s ==> check your input or email topcodermc@gmail.com' % error + '\033[0m'

    print '================================================'


def ReverseIpLookUp():
    if not os.path.exists('./outputs/Info-Gathering'):
        os.mkdir('./outputs/Info-Gathering')

    MASK()
    print
    selectedDepth = raw_input(TextColor.WHITESMOKE + 'info-gath/ReverseIp/# Selecte one item: ' + TextColor.WHITE)

    if selectedDepth == '1':
        LOW()
    elif selectedDepth == '2':
        HIGH()
    else:
        raise SystemExit, TextColor.RED + '[-] Please Enter number from subment items' + TextColor.WHITE
