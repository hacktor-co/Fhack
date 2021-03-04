try:
    from Config import RecOS
    from src.Colors import TextColor
    import os
except Exception as error:
    raise SystemExit, '\033[31m' + "%s" % error + "\033[0m"


def LinuxDebian_Ubuntu_Setup():
    def InstallCreateMalwareTool_Android():
        print TextColor.WARNING + "[*] Please wait for installing android tools" + TextColor.WHITE
        os.system("sudo apt-get install openjdk-11-jdk-headless")
        os.system("sudo apt-get install apktool")
        print TextColor.GREEN + "[+] Android tools installed successfully" + TextColor.WHITE

    def InstallNetowkTools():
        print TextColor.WARNING + "[*] Please wait for installing network tools" + TextColor.WHITE
        os.system("sudo apt-get install nmap")
        print TextColor.GREEN + "[+] Network tools installed successfully" + TextColor.WHITE

    InstallCreateMalwareTool_Android()
    InstallNetowkTools()


def MACOS_Setup():
    def InstallCreateMalwareTool_Android():
        print TextColor.WARNING + "[*] Please wait for instaling android tools" + TextColor.WHITE
        os.system("brew cask install java")
        os.system('brew install apktool')
        print TextColor.GREEN + "[+] Done" + TextColor.WHITE

    def InstallNetowkTools():
        print TextColor.WARNING + "[*] Please wait for installing network tools" + TextColor.WHITE
        os.system("brew install nmap")
        print TextColor.GREEN + "[+] Network tools installed successfully" + TextColor.WHITE

    InstallCreateMalwareTool_Android()
    InstallNetowkTools()


def main():
    os.system("sudo pip install -r libs_used")

    if RecOS.IsOSLinux():
        if "Ubuntu" in RecOS.getLinuxDist():
            LinuxDebian_Ubuntu_Setup()

    elif RecOS.IsOSDarwin():
        import subprocess as subproc
        command = ['brew', '-v']
        process = subproc.Popen(command, stdout=subproc.PIPE, stderr=subproc.PIPE)
        brewVersion, error = process.communicate()

        if brewVersion is not "":
            MACOS_Setup()
        else:
            print TextColor.RED + "\nPlease install brew App from the internet\n" + TextColor.WHITE


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit, TextColor.RED + '[-] Installe escaped ...' + TextColor.WHITE
