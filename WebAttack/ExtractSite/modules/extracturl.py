try:
    from Utilities.WebTool.crawl import crawl
    from src.Colors import TextColor
except Exception as error:
    raise SystemExit, TextColor.RED + "[-]Something is wrong in importing libraries in extracturl class" + TextColor.WHITE


class ExtractUrl:

    def __init__(self, rhost, depth):
        self.depth = depth
        self.rhost = rhost

    def Start(self):

        for item in crawl(self.rhost, self.depth):
            print item
