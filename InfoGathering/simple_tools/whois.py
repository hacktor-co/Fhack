try:
    from src.Colors import TextColor
    import subprocess
except Exception as error:
    raise SystemExit, '\033[31m' + error + "\033[0m"


def MASK():
    print """   _____
               [     ]
               [ }1{ ]     <----- Whois 
               [ {0} ]
               [_____] ---> It is a bad thing
    """

def whois():

    url = raw_input(TextColor.CVIOLET + '~/info-gathering/# Whois (e.g: example.com): ')

    process = subprocess.Popen(['whois', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = process.communicate()

    print TextColor.WARNING + "======== WHOIS ========" + TextColor.WHITE
    print
    print TextColor.CYAN + out + TextColor.WHITE

    with open('./outputs/Info-Gathering/' + 'WHOIS-' + url, 'a') as file:
        file.write(out)


if __name__ == "__main__":
    whois()
