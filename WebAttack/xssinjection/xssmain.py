try:
    from src.Colors import TextColor
    import src.libs as lib
    from Config.WebConfig import define_headerdata
    from .payloads.loader import MakeSelection
    from Config.RecOS import IsOSDarwin, IsOSLinux
    from Utilities.BaseClass import ShowProgress
    from Utilities.WebTool.crawl import crawl
except Exception as err:
    raise SystemExit, 'Something is wrong: %s' % err


def PrintXssMask():
    maskString = TextColor.GREEN + str("""
    
                Do want search XSS vulnerability ?
                
                                            vulnerable site
                     __.__.__.__.__           ____   __ 
                    (              )         |    | |==|
                    (   Find XSS   ) <====>  |____| |  |
                    (______________)         /::::/ |__|
                      (_)     (_)
                      |=|     |=|
    
    """) + TextColor.WHITE
    return maskString


def MainXSS():
    print PrintXssMask()

    output = MakeSelection()

    if output is None:
        return

    root = raw_input(
        TextColor.PURPLE + TextColor.BOLD +
            'XssAttack/# Enter site url (e.g.: http://example.com): ' + TextColor.WHITE
    )

    for rhost in crawl(root, 0):
        StartAttack(output, rhost)


def StartAttack(output, rhost):
    if type(output) == list:

        define_headerdata['referer'] = rhost

        findXss = False
        counter = 0

        for item in output:
            if item == " " or item == '\n' or item == "":
                continue

            response = lib.requests.get(url=rhost, headers=define_headerdata, verify=False)

            if response.status_code is not 200:
                continue

            if IsOSDarwin():  # parser os lxml not working on mac OS <Darwin>
                soup = lib.BS(response.content, "html.parser")
            else:
                soup = lib.BS(response.content, "lxml")

            ShowProgress('... Testing payload [%d] please wait ' % counter, counter)
            counter += 1

            with lib.requests.Session() as session:
                for line in soup.find_all('input', {'type': 'text'}):

                    parameter = str(lib.urlparse.urlparse(line['name'])[2])

                    response = session.get(url=rhost, params={parameter: str(item)}, verify=False)
                    
                    if response.content.find(str(item)) is not -1:
                        print
                        counter += 1

                        ShowProgress('... Testing payload [%d] please wait ' % counter, counter)
                        print
                        print TextColor.GREEN + '[+] => XSS found with: %s\ninput [name=%s]\nurl => %s' \
                              % (item, lib.urlparse.urlparse(line['name'])[2], rhost) + TextColor.WHITE
                        print
                        findXss = True

            if findXss:
                break

    if not findXss:
        print TextColor.RED + '\n[-]This url [%s] is not vulnerabale' % rhost + TextColor.WHITE
        print


if __name__ == "__main__":
    try:
        MainXSS()
    except Exception as err:
        raise SystemExit, TextColor.RED + 'Something is wrong: %s' % err + TextColor.RED
