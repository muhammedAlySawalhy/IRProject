import os


class InvertedIndex:
    def __init__(self, terms_path, docs_path, dest_path):
        self.terms_path = terms_path
        self.docs_path = docs_path
        self.dest_path = dest_path

    def Indexing(self):
        # check if the term in document
        # check how manytimes it exists return the time
        # create dict with term,docid,times
        index = {}


if __name__ == '__main__':

    index = InvertedIndex(
        './tokenized/', './DocumentCollection/', './indexing')
    with open('./indexing/' + 'invertedIndex.txt', 'w', encoding='utf-8') as f:
        for i in index.Indexing():
            f.write(i)
    index.get_terms()
    index.get_documents()
