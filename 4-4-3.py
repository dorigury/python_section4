import urllib.request as req
import simplejson as json
import os.path

#URL
url = "https://api.github.com/repositories"

#경로 & 파일명
savename = "d:/bbb/repo.json"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

items = json.load(open(savename, 'r', encoding="utf-8"))
#itmes = json.loads(open(savename, 'r', encoding="utf-8")).read()

for item in items:
    print(item["full_name"] + " - " + item["owner"]["url"])
