import bs4 as bs
import urllib.request

from competition import Competition


class CompetitionFactory:
    def __init__(self):
        pass


    def get_competition(self, link):
        comp = Competition()

        source = urllib.request.urlopen(link)
        soup = bs.BeautifulSoup(source, "lxml")

        self.__set_teams(soup)

        return comp


    def __set_teams(self, soup):
        tab = soup.find_all("tab")

        print(tab)
