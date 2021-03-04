try:
    from src.Colors import TextColor
    import src.libs as lib
    from Config.WebConfig import define_headerdata
    from sys import stdout
    import re
except Exception as error:
    raise SystemExit, "\033[31m" + "Some error happened: %s" % error + "\033[0m"


def MASK():
    print


def CleanUrl(rhost):
    """
    Delete protocol and www from url if it's exists
    :param rhost: Get website url
    :return:
    """
    return re.sub('.*www\.', '', rhost, 1).split('/')[0].strip()


def GetSubDomains(rhost):
    subdomains = []

    if rhost.startswith('https://'):
        target = CleanUrl(rhost[8:])
    elif rhost.startswith('http://'):
        target = CleanUrl(rhost[7:])

    req = lib.requests.get("https://crt.sh/?q=%.{rhost}&output=json".format(rhost=target))

    if req.status_code != 200:
        print TextColor.RED + "[-] Information not available!" + TextColor.WHITE
        return

    for (key, value) in enumerate(req.json()):
        subdomains.append(value['name_value'])

    print(TextColor.WARNING + "\n[*] =========== SUBDOMAINS OF TARGET: {rhost} =========== [*] \n".format(
        rhost=target)) + TextColor.WHITE

    subdomains = sorted(set(subdomains))

    for subdomain in subdomains:
        print TextColor.GREEN + str("[+] {subdomain}".format(subdomain=subdomain)) + TextColor.WHITE

        with open('./outputs/Info-Gathering/' + 'SUBDOMAIN-' + target, 'a') as file:
            file.write(subdomain + "\n")

    print


def Main_FindSubdomain():
    MASK()

    stdout.write(TextColor.CVIOLET + str('~ Fhack/# Enter web url: ') + TextColor.WHITESMOKE)
    rhost = raw_input('')

    print TextColor.WARNING + str('[*] Please wait to set web host') + TextColor.WHITE

    try:
        responseCode = lib.requests.get(url=rhost, headers=define_headerdata, allow_redirects=False,
                                        verify=False).status_code
    except Exception as error:
        print TextColor.RED + str('Some error happend: %s' % error) + TextColor.WHITE
        return

    if responseCode == 200:
        print TextColor.GREEN + str('[+] Web Host set successfully') + TextColor.WHITE
        GetSubDomains(rhost)
    else:
        print TextColor.RED + str('[-] Web host not set check it then try again') + TextColor.WHITE
        return


if __name__ == "__main__":
    Main_FindSubdomain()
