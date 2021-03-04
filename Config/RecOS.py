try:
    import platform
except:
    print 'Something wrong on RecOS.py file please check it'


def getLinuxDist():
    return platform.linux_distribution()


def CheckOS():
    return platform.system()


def IsOSDarwin():
    if CheckOS() == "Darwin":
        return True
    else: return False

def IsOSLinux():
    if CheckOS() == "Linux":
        return True
    else: return False