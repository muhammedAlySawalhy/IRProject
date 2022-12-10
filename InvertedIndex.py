import os

import json


def load(file_path):
    for file in os.listdir(file_path):
        with open(file_path + file, 'r', encoding='utf-8') as f:
            for line in f:
                line = json.loads(line)
                for term in line:
                    yield term, file


class InvertedIndex:
    def __init__(self, terms_path):
        self.terms_path = terms_path  # path of tokens
        self.terms = {}  # dict of terms and its docs
        self.postings = {}  # dict of terms and its postings list

    def get_terms_docs(self):
        # get all terms in a dict
        for term, file in load(self.terms_path):
            if term not in self.terms:
                self.terms[term] = [file]
            else:
                if file not in self.terms[term]:
                    self.terms[term].append(file)

    def create_index(self):
        # create index of terms and its docs
        for term in self.terms:
            for doc in self.terms[term]:
                if term not in self.postings:
                    self.postings[term] = [doc]
                else:
                    if doc not in self.postings[term]:
                        self.postings[term].append(doc)

    def save_index(self):
        # save index in a file
        print(self.postings)
        with open('./indexing/' + 'InvertedIndex.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.postings))


if __name__ == '__main__':

    index = InvertedIndex('./tokenized/')
    index.get_terms_docs()
    index.create_index()
    index.save_index()
