import urllib.request as req
from bs4 import BeautifulSoup
import os.path

url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "d:/bbb/forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

info = {}
for location in soup.find_all("location"):
    loc = location.find("city").string
    #print(loc)
    weather = location.find_all("tmn")
    #print(weather)
    if not (loc in info):
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)

#print(info)
#print(info.keys())

with open('d:/bbb/forecast.txt','wt') as f:
    for loc in sorted(info.keys()):
        print("+", loc)
        f.write(str(loc) + '\n')
        for n in info[loc]:
            print("-", n)
            f.write ('\t' + str(n) +'\n')
