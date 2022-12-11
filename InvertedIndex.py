import os

import json


def load(tokens_dir):
    for file in os.listdir(tokens_dir):
        with open(tokens_dir + "/" + file, 'r', encoding='utf-8') as f:
            terms = json.loads(f.read())
            for term in terms:
                yield term, file


class InvertedIndex:
    def __init__(self, tokens_dir, out_file):
        self.tokens_dir = tokens_dir  # path of tokens
        self.terms = {}  # dict of terms and its docs
        self.postings = {}  # dict of terms and its postings list
        self.out_file = out_file

    def get_terms_docs(self):
        # get all terms in a dict
        for term, tokens_file in load(self.tokens_dir):
            doc_file = tokens_file.replace(".json", ".txt")
            if term not in self.terms:
                self.terms[term] = [doc_file]
            else:
                if doc_file not in self.terms[term]:
                    self.terms[term].append(doc_file)

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
        os.makedirs(os.path.dirname(self.out_file), exist_ok=True)
        with open(self.out_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.postings))


if __name__ == '__main__':
    index = InvertedIndex('./.out/tokens/', './.out/indexing/inv_index.json')
    index.get_terms_docs()
    index.create_index()
    index.save_index()
