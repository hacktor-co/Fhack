"""
    - created on march/27/2019
    - author topcodermc
    -- [ description of this module:
        create this file for make url of union select phrase
    ]
"""


def makeurl(columns=None, url=None, character=None):

    numbers = list()
    for item in xrange(1, columns + 1):
        numbers.append(str(item) * 4)

    numberString = str()
    for item in numbers:
        numberString += item + ', '

    urlFace = url.replace('=', '=-') + character + " COMMANDS " + numberString[:-2]

    output = dict()
    output['urlFace'] = urlFace
    output['numbers'] = numbers

    return output
