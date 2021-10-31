from googs import Googs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class Run():
    def __init__(self) -> None:
        # ADBLOCK_RULES = ['https://easylist-downloads.adblockplus.org/ruadlist+easylist.txt',  
        #          'https://filters.adtidy.org/extension/chromium/filters/1.txt']
        self.paragraph = ""
        # rule_files = [link.rpartition('/')[-1] for link in ADBLOCK_RULES]
        # for rule_url, rule_file in zip(ADBLOCK_RULES, rule_files):
        #     r = requests.get(rule_url)
        #     with open(rule_file, 'w', encoding="utf-8") as f:
        #         print(r.text, file=f)
        # self.remover = AdRemover(*rule_files)

    def __scrape(self, link ):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        with open("out/Python.txt", "w+", encoding="utf-8") as f:
            para = driver.find_elements_by_id("bodyContent")
            p_tags = para.find_elements_by_tag_name("p")

            for p_tag in para:
                f.write(f"\t{p_tag.text}\n\n")
            f.close()



    def run(self, topic:str, limit:int=5):
        # links = Googs().search(topic=topic, limit=limit)
        # print("Fetch Done")
        links = ["https://en.wikipedia.org/wiki/Python_(programming_language)"]
        for i in range(limit):
            self.__scrape(links[i])
        print("Scraping Done")
        
Run().run("Python", 1)