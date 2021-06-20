import bs4 as bs
import urllib.request

from competition import Competition
from competition_factory import CompetitionFactory


base_url = "https://www.robotevents.com/robot-competitions/college-competition"
source = urllib.request.urlopen(base_url).read()
soup = bs.BeautifulSoup(source, "lxml")

comp_divs = soup.find_all("div", class_="results")[0]
urls = [a["href"] for a in comp_divs.find_all("a")]



comps = []
fact = CompetitionFactory()

for url in urls[0]:
    comps.append(fact.get_competition(url))
