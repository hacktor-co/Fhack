"""
    - created on march/20/2019
    - author topcodermc
    -- [ description of this module:
        check kind of error that this cluase make
    ]
"""

import json

class ErrorType:

    def __init__(self, responseText):
        self.response = responseText

    def ErrorBase(self):
        '''
        if column error exist in content so we send true
        :return:
        '''

        with open("./WebAttack/sqlinjection/payloads/OrderByInjectionAndError.json") as jsonFile:
            errorList = json.load(jsonFile)
            for item in errorList["mysql"]["error"]:
                if self.response.lower().find(item.lower().replace('number', str(1000))) is not -1:
                    return True
            return False


def CheckErrorType(response):
    errorType = ErrorType(response)

    if errorType.ErrorBase():
        return 'ErrorBase'
    else:
        return 'ContentBase'
