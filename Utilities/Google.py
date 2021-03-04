"""
    - created on march/10/2019
    - author -> topcodermc
    - for: this module create for searching the query that user enter for google hacking
"""
try:
    import re
    import requests
    from src.Colors import TextColor
except Exception as error:
    raise SystemExit, "[+] Something is wrong in Utilities->Google as: %s" % error


def GoogleSearch(query, page_no):
    baseUrl = "https://google.com/search?q={query}&btnG=Search&hl=en-US&biw=&bih=&gbv=1&start={page_no}&filter=0". \
        format(query=query, page_no=page_no)

    response = requests.get(url=baseUrl)

    link_regx = re.compile('<cite.*?>(.*?)</cite>')
    links_list = link_regx.findall(response.content)

    for link in links_list:
        link = re.sub('<span.*>', '', link)
        yield (link.replace("<b>", '\0')).replace("</b>", '\0')


# dir_listing = "site:" + site + " intitle:index.of"
# conf_exposed = "site:" + site + " ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini"
# db_exposed = "site:" + site + " ext:sql | ext:dbf | ext:mdb"
# log_exposed = "site:" + site + " ext:log"
# bk_exposed = "site:" + site + " ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"
# login_page = "site:" + site + " inurl:login"
# sql_error = 'site:' + site + ' intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"'
# doc_exposed = 'site:' + site + ' ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv'
# php_info = 'site:' + site + ' ext:php intitle:phpinfo "published by the PHP Group"'
