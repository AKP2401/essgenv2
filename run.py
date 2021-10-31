from googs import Googs
from selenium import webdriver
from selenium.webdriver.common.by import By
from summarize import Summarizer
import tqdm


class Run():
    def __init__(self) -> None:
        self.paragraph = ""

    def __scrape(self, link ):
        text = ""
        options = webdriver.ChromeOptions()
        options.headless = True
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



    def run(self, topic:str, limit:int=5):
        links = Googs().search(topic=topic, limit=limit)
        print("Fetch Done")
        print("Scraping...")
        for i in tqdm.tqdm(range(limit)):
            self.paragraph += self.__scrape(links[i])
        with open("./out/intermediate.txt", 'w') as f:
            f.write(self.paragraph)
            f.close()
        summ = Summarizer()
        summ.gen_summary()

if __name__=="__main__":
    Topic = input("Enter the Topic name: ")
    Num_Pg = int(input("Enter the number of pages to be scraped: "))
    RR = Run()
    RR.run(Topic, Num_Pg)