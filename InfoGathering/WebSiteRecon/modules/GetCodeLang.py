"""
    - created on march/9/2019
    - author topcodermc
    -- [ description of this module:
        this module created for get all information about programming language that used for web application
    ]
"""

try:
    import requests as reqs

    from src.Colors import TextColor
    from Utilities.WebTool.crawl import crawl
    from Utilities.Google import GoogleSearch
except Exception as error:
    raise SystemExit, TextColor.RED + \
                      str('[-] We have error on WebSiteRecon->modules->GetCodeLang as %s' % error) \
                      + TextColor.WHITE


def CheckExtensions(rUrl):
    if (
            rUrl.find('.php') is not -1 or
            rUrl.find('.php4') is not -1 or
            rUrl.find('.php3') is not -1 or
            rUrl.find('.phtml') is not -1
    ):
        return 'PHP'
    elif (
            rUrl.find('.asp') is not -1 or
            rUrl.find('.aspx') is not -1 or
            rUrl.find('.axd') is not -1 or
            rUrl.find('.asmx') is not -1 or
            rUrl.find('.ashx') is not -1 or
            rUrl.find('.asx') is not -1
    ):
        return 'ASP.net'
    elif (
            rUrl.find('.jsp') is not -1 or
            rUrl.find('.jspx') is not -1 or
            rUrl.find('.wss') is not -1 or
            rUrl.find('.do') is not -1 or
            rUrl.find('.action') is not -1
    ):
        return 'JAVA'
    elif rUrl.find('.pl') is not -1:
        return "PERL"
    elif rUrl.find('.py') is not -1:
        return "PYTHON"
    elif rUrl.find('.rhtml') is not -1 or rUrl.find('.rb') is not -1:
        return "RUBY"
    else:
        return 'none'


def Google(url):
    """
    This function use google query hacking for finding the extension of web site url
    :param url: url of web site
    :return: the thecnology
    """
    for pageCounter in xrange(1, 30):
        for item in GoogleSearch('site:{url}'.format(url=url), pageCounter):
            if CheckExtensions(item) is not 'none':
                return CheckExtensions(item)


def InSiteUrlContent(url):
    """
    This function see the urls that site has which check the content of its
    :param url: url of web site
    :return: the technology
    """
    for rUrl in crawl(url, 3):
        if CheckExtensions(rUrl) is not 'none':
            return CheckExtensions(rUrl)


def Headers(url):
    """
    This function test http headers for finding the language that we app used
    :param url: url of web site
    :return: the technology
    """
    with reqs.Session() as session:
        response = session.get(url=url, verify=False, allow_redirects=False)
        try:
            if 'php' in str(response.headers['x-powered-by'].lower()):
                return 'PHP'
            elif 'asp' in str(response.headers['x-powered-by'].lower()):
                return 'ASP.net'
            elif 'java' in str(response.headers['x-powered-by'].lower()):
                return 'JAVA'
            else:
                return None
        except:
            try:
                if 'php' in str(response.headers['X-Pingback'].lower()):
                    return 'PHP'
                elif 'asp' in str(response.headers['X-Pingback'].lower()):
                    return 'ASP.net'
                elif 'java' in str(response.headers['X-Pingback'].lower()):
                    return 'JAVA'
                else:
                    return None
            except:
                print response.cookies
                if 'php' in str(response.cookies).lower():
                    return 'PHP'
                elif 'asp' in str(response.cookies).lower():
                    return 'ASP.net'
                elif 'jse' in str(response.cookies).lower():
                    return 'JAVA'
                else:
                    return None


def FileExtensions(url):
    """
    This function test url extentions for finding language technology that web app use
    :param url: url of web site
    :return: the technology
    """
    return CheckExtensions(url)


def StartSearching():

    from sys import stdout
    print
    stdout.write(TextColor.CYAN + '~ Fhack/# Enter web url (http://example.com): ' + TextColor.WHITE)
    url = raw_input(TextColor.WHITESMOKE + '' + TextColor.WHITE)

    print TextColor.WARNING + '[*] Please wait to set the web url ...' + TextColor.WHITE

    response = reqs.get(url=url, verify=False)
    if response.status_code == 200:
        print TextColor.GREEN + '[+] Web url has been set ...' + TextColor.WHITE
        print
        print TextColor.GREEN + '\t[1] Use hard searching'
        print '\t[2] Use low searching'
        print '\t[0] Exit \n'
        selectedItem = raw_input(TextColor.CVIOLET + '~ fhack/# Enter mode that you want search (0-2): ' + TextColor.WHITE)
        if selectedItem == '1':

            print '[+] From file extentions in url: ' + FileExtensions(url)
            print '[+] From Headers: ' + Headers(url)
            print '[+] From site content: ' + InSiteUrlContent(url)
            print '[+] From Google: ' + Google(url)

        elif selectedItem == '2':
            print '[*] Please wait to findout ...'
            if FileExtensions(url) is not 'none':
                print TextColor.GREEN + '[+] Language: ' + FileExtensions(url) + TextColor.WHITE
                return
            elif Headers(url) is not None:
                print TextColor.GREEN + '[+] Language: ' + Headers(url) + TextColor.WHITE
                return
            elif InSiteUrlContent(url) is not None:
                print TextColor.GREEN + '[+] Language: ' + InSiteUrlContent(url) + TextColor.WHITE
                return
            elif Google(url) is not None:
                print TextColor.GREEN + '[+] Language: ' + Google(url) + TextColor.WHITE
                return
            else:
                print TextColor.RED + '[-] Unable to findout' + TextColor.WHITE
        elif selectedItem == '0':
            print
            return
        else:
            print TextColor.RED + '[-] Please enter input correctly'
            return

    else:
        return TextColor.RED + '[-] Web site not found :( ' + TextColor.WHITE
