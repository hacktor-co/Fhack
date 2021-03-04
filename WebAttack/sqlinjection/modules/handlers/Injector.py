"""
    - created on march/18/2019
    - author topcodermc
    -- [ description of this module:
        test order by phrase for get count of columns in the target database
    ]
"""
try:
    from src.Colors import TextColor
except Exception as error:
    raise SystemExit, TextColor.RED + "[-] Have problem in OrderByInjectionMothods.py as: %s" % error + TextColor.WHITE


def StartInjectionMethods(db, url, character):
    if db == 'mysql' or db.endswith('mysql'):
        from ..procs.mysql.GetColumns.Injector import Start
        return Start(url, character, db)
