import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


class Tokenize:
    def __init__(self, data_dir, output_dir):
        self.data_dir = data_dir
        self.output_dir = output_dir

    def load(self):
        tokenize_lines = []
        for file in os.listdir(self.data_dir):
            with open(self.data_dir + '/' + file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                tokenize_lines += word_tokenize(*lines)
        print(tokenize_lines, 'tokenizing')
        return tokenize_lines

    def remove_dublicates(self):
        removed_dublicates = []
        for word in self.load():
            if word not in removed_dublicates:
                removed_dublicates.append(word)
        print('after removing  dublicates')
        return removed_dublicates

    def lowering(self):
        lowered = []
        for term in self.remove_dublicates():
            lowered.append(term.lower())
        print(lowered, 'after lowering')
        return lowered

    def remove_stop_words(self, default_langs=['arabic', 'english'],):
        stop_words = set(stopwords.words(default_langs))
        stop_words = stop_words - set(['where', 'to', 'in'])
        filtered_sentence = [w for w in self.lowering() if not w in stop_words]
        print(filtered_sentence, 'after removing stop words')
        return filtered_sentence

    def stemming(self):
        stemmed = []
        ps = PorterStemmer()
        for word in self.remove_stop_words():
            stemmed.append(ps.stem(word))
        print(stemmed, 'after stemming')
        return stemmed

    def save(self):
        with open(self.output_dir + '/' + 'Tokenized.txt', 'w') as f:
            f.write(str(self.stemming()))


if __name__ == '__main__':
    tokenize = Tokenize('./DocumentCollection/', './tokenized')
    tokenize.load()
    tokenize.remove_dublicates()
    tokenize.lowering()
    tokenize.remove_stop_words()
    tokenize.stemming()
    tokenize.save()
