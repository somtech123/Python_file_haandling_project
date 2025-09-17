import os
from collections import defaultdict, Counter
import re
import math

class Search:

#load all text file
    def load_documents(self,folder='mini_search_engine\data'):
        docs = {}
        for i, filename in enumerate(os.listdir(folder), 1):
            if filename.endswith('.txt'):
                with open(os.path.join(folder, filename), 'r', encoding='utf-8') as f:
                    docs[i] = {'name': filename, 'text': f.read()}
        return docs
    

    #build inverted index using TF-IDF
    def build_index(self,docs):
        index = defaultdict(dict)

        doc_length = {}
        for doc_id, doc in docs.items():
            words = re.findall(r"\w+", doc['text'].lower())
            count = Counter(words)
            doc_length[doc_id] = len(words)
            for word, freq in count.items():
                index[word][doc_id] = freq
        return index, doc_length
    
    #search function

    def search(self,query, docs, index, doc_length):
        words = query.lower().split()
        scores = Counter()
        N = len(docs)

        for word in words:
            if word in index:
                df = len(index[word]) #document frequency
                idf = math.log(N / (1 + df))
                for doc_id, tf in index[word].items():
                    scores[doc_id] += (tf / doc_length[doc_id] * idf)
        result = [(docs[doc_id]['name'], score) for doc_id, score in scores.most_common()]
        return result
    

