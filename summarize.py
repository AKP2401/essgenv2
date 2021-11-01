import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
from tqdm import tqdm

class Summarizer:

    def __init__(self) -> None:
        article = None
        with open("./out/intermediate.txt", 'r', encoding="utf-8") as f:
            filedata = f.readlines()
            article = filedata[0].split(". ")
            f.close()

        self.sentences = []
        for sentence in article:
            print(sentence)
            self.sentences.append(sentence.replace("[^a-zA-Z", " ").split(" "))
        print(self.sentences)
    
    def sentence_similarity(self, sent1, sent2, stop_words=[]):
        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]

        all_words = list(set(sent1 + sent2))

        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        for w in sent1:
            if w not in stop_words:
                vector1[all_words.index(w)] += 1

        for w in sent2:
            if w not in stop_words:
                vector2[all_words.index(w)] += 1

        return 1 - cosine_distance(vector1, vector2)
    
    def build_similarity_matrix(self, stop_words):
        similarity_matrix = np.zeros((len(self.sentences), len(self.sentences)))

        for idx1 in range(len(self.sentences)):
            for idx2 in range(len(self.sentences)):
                if idx1 != idx2:
                    similarity_matrix[idx1][idx2] = self.sentence_similarity(self.sentences[idx1], self.sentences[idx2], stop_words)
        
        return similarity_matrix

                    
    
    def gen_summary(self):
        nltk.download("stopwords")
        stop_words = stopwords.words("english")
        summarize_text = []

        sentence_similarity_matrix = self.build_similarity_matrix(stop_words)

        sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
        scores = nx.pagerank(sentence_similarity_graph)

        ranked_sentence = sorted(((scores[i], s) for i,s in enumerate(self.sentences)), reverse=True)
        print("Indexes of top ranked sent are", ranked_sentence)
        print(f"Enter the number of top results to be summarized\nNote: The bigger the number more the content but lesser the accuracy\nMaximum is {len(ranked_sentence)}:", end='')
        top_n = int(input())

        for i in tqdm(range(10)):
            summarize_text.append(" ".join(ranked_sentence[i][1]))

        with open("./out/Output.txt", "w", encoding="utf-8") as f:
            f.write(". ".join(summarize_text))


if __name__=="__main__":
    ff = Summarizer()
    ff.gen_summary()