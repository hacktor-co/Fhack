try:
    import src.libs as lib
    from src.Colors import TextColor
    from Config.WebConfig import define_headerdata
    import sys
    from Config.RecOS import IsOSDarwin
    from time import sleep
except Exception as err:
    raise SystemExit, '%s' % err


def crawl(root, depth="!!"):
    if root.endswith('/'):
        root = root[0:len(root) - 1]

    if isinstance(depth, int):
        depth = str(depth)

    elif depth != "!!":
        depth = raw_input(
            TextColor.PURPLE + TextColor.BOLD + str('Enter depth of crawl / [Enter !! for auto crawling]: ') \
            + TextColor.WHITE)


    url_queue = lib.Queue()
    url_queue.put(root)
    urls_seen = set()

    counter_depth = 0

    while True:

        current_url = url_queue.get()
        urls_seen.add(current_url)

        if depth != "!!":
            if counter_depth == int(depth):
                print TextColor.WARNING + str("\n ------- Done ------- \n") + TextColor.WHITE
                break

        counter_depth = counter_depth + 1

        try:

            response = lib.requests.get(current_url, params=None,
                                        headers=define_headerdata, allow_redirects=False, verify=False)

            # algorithm of crawling on website page
            if response.status_code == 200:

                soup = lib.BS(response.content, "html.parser")

                for line in soup.find_all('a', href=True):
                    if lib.urlparse.urlparse(line['href']):
                        sleep(0.2)
                        if line['href'].startswith('http') or line['href'].startswith('https'):
                            if line['href'].startswith(root):
                                if line['href'] not in urls_seen:

                                    url_queue.put(line['href'])
                                    yield line['href']
                                else:
                                    continue
                        else:
                            if line['href'].startswith('/'):
                                if root + line['href'] not in urls_seen:

                                    url_queue.put(root + line['href'])
                                    yield root + line['href']
                                else:
                                    continue
                            elif not line['href'].startswith('/') or not \
                                    line['href'].startwith('http') or not line['href'].startswith('https'):
                                if (root + '/' + line['href']) not in urls_seen:

                                    url_queue.put(root + '/' + line['href'])
                                    yield root + '/' + line['href']
                                else:
                                    continue
                            else:
                                if line['href'] not in urls_seen:

                                    url_queue.put(line['href'])
                                    yield line['href']
                                else:
                                    continue

            else:
                return


        except Exception as err:
            raise SystemExit, '%s' % err
    url_queue.task_done()
    return
