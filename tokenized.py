import os
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


class Tokenize:
    def __init__(self, file_name, output_dir):
        self.file_name = file_name
        self.output_dir = output_dir
        self.tokens = set()

    def load(self):

        with open('DocumentCollection/' + self.file_name, 'r', encoding='utf-8') as f:
            lines = f.read()
            for word in word_tokenize(lines.lower()):
                self.tokens.add(word)

    def remove_stop_words(self, default_langs=['arabic', 'english'],):
        self.load()
        stop_words = set(stopwords.words(default_langs))
        stop_words = stop_words - set(['where', 'to', 'in'])
        self.tokens = self.tokens - stop_words

    def stemming(self):
        stemmed = []
        self.remove_stop_words()
        ps = PorterStemmer()
        for word in self.tokens:
            stemmed.append(ps.stem(word))
        print(stemmed, 'after stemming')
        return stemmed

    def save(self):
        with open(self.output_dir + '/' + self.file_name, 'w') as f:
            f.write(json.dumps(self.stemming()))


if __name__ == '__main__':
    for file in os.listdir('./DocumentCollection/'):
        tokenize = Tokenize(file, './tokenized')
        tokenize.save()
