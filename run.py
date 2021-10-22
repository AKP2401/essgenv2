import urllib
from googs import Googs
from bs4 import BeautifulSoup
from adremove import AdRemover
import re, requests
import lxml.html
import urllib.request


class Run():
    def __init__(self) -> None:
        ADBLOCK_RULES = ['https://easylist-downloads.adblockplus.org/ruadlist+easylist.txt',  
                 'https://filters.adtidy.org/extension/chromium/filters/1.txt']
        self.paragraph = ""
        rule_files = [link.rpartition('/')[-1] for link in ADBLOCK_RULES]
        for rule_url, rule_file in zip(ADBLOCK_RULES, rule_files):
            r = requests.get(rule_url)
            with open(rule_file, 'w', encoding="utf-8") as f:
                print(r.text, file=f)
        self.remover = AdRemover(*rule_files)

    def __scrape(self, link ):
        html = requests.get(link).text
        document = lxml.html.document_fromstring(html)
        self.remover.remove_ads(document)
        clean_html = lxml.html.tostring(document)
        print(clean_html)

    def run(self, topic:str, limit:int=5):
        links = Googs().search(topic=topic, limit=limit)
        print("Fetch Done")
        for i in range(limit):
            self.__scrape(links[i])
        print("Scraping Done")
        
Run().run("Python", 1)