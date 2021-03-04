try:
    from src.Colors import TextColor
    import os
except Exception as err:
    raise SystemExit, "Something wrong: %s" % (str(err))


def InitFhack():
    os.system('cls' if os.name == 'nt' else 'clear')

    if not os.path.exists('outputs'):
        os.mkdir('./outputs')
