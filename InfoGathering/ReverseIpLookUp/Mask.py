from src.Colors import TextColor


def MASK():
    print TextColor.GREEN + """             
                                            
                                            +=====+
                                           /| { } | --> Server
                        +-----------+     / | --- |
            Reverse Ip  |example.com| ---/  | --- |
          ---+--+-----> |-----------|       |     |
            RDNS        |   FHACK   |ViewDNS| --- |
                        |           |       +-----+
                        +-----------+           HOST
                                            
                <========================================= < < <
                    { example1.com, example2.com, ... }
    """ + TextColor.WHITE

    SubItems()


def SubItems():
    print TextColor.CVIOLET + '\t\t==> [1]. LOW'
    print '\t\t==> [2]. HARD with more details' + TextColor.WHITE
