"""
    - created on march/12/2019
    - author topcodermc
    -- [ description of this module:
        Sql injection mask
    ]
"""

try:
    from src.Colors import TextColor
except Exception as error:
    raise SystemExit, TextColor.RED + '[-] Error on mask: %s' % error


def MASK():
    print
