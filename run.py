from googs import Googs
from selenium import webdriver
from selenium.webdriver.common.by import By
from summarize import Summarizer
import tqdm
import os


class Run():
    def __init__(self) -> None:
        self.paragraph = ""

    def __scrape(self, link ):
        try:
            text = ""
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument("--disable-logging")
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            driver = webdriver.Chrome(options=options)
            driver.get(link)
            para = driver.find_elements(By.TAG_NAME, "p")

            for p_tag in para:
                text += str(p_tag.text)
            return text
        except:
            print("\nPage scrape error")
            return ""


    def run(self, topic:str, limit:int=5):
        links = Googs().search(topic=topic, limit=limit)
        print("Fetch Done")
        print("Scraping...")
        for i in tqdm.tqdm(range(limit)):
            self.paragraph += self.__scrape(links[i])
        if not os.path.isdir("out"):
            os.mkdir("out")
        with open("./out/intermediate.txt", 'w', encoding="utf-8") as f:
            f.write(self.paragraph)
            f.close()
        summ = Summarizer()
        summ.gen_summary()

if __name__=="__main__":
    Topic = input("Enter the Topic name: ")
    Num_Pg = int(input("Enter the number of pages to be scraped: "))
    RR = Run()
    RR.run(Topic, Num_Pg)