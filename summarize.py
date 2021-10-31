import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

class Summarizer:
    def __init__(self) -> None:
        article = None
        with open("./out/dummy.txt", 'r') as f:
            filedata = f.readlines()
            article = filedata[0].split(". ")
            f.close()

        self.sentences = []
        for sentence in article:
            print(sentence)
            self.sentences.append(sentence.replace("[^a-zA-Z", " ").split(" "))
        self.sentences.pop()
        print(self.sentences)