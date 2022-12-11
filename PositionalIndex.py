import re
import os
import json

example = [
    {
        "term": "TheTerm",
        "docs_count": 2,
        "docs": {
            "1.txt": [1, 100, 340],
            "6.txt": [2, 51]
        }
    }
]

# -> we can modify the tokanization process to calculate positions as well
# -> less effecient method is to calculate the position in separate step using KMP for example
#
# Next step: merging positions
# Q1: intersect the query with the position index, what does that mean?
# Q2: what does poistion merging mean?
#


class PositionalIndex:
    def __init__(self, inv_index_path, out_file):
        self.inv_index_path = inv_index_path
        self.out_file = out_file

    pos_index = {}

    def ensure_term(self, term, doc_file):
        if term not in self.pos_index:
            self.pos_index[term] = {
                "term": term,
                "count": 0,
                "docs": {}
            }

        if doc_file not in self.pos_index[term]["docs"]:
            self.pos_index[term]["docs"][doc_file] = []

    def insert_term(self, term, doc_file, pos):
        self.ensure_term(term, doc_file)
        self.pos_index[term]["count"] += 1
        self.pos_index[term]["docs"][doc_file].append(pos)

    def process_doc(self, doc_file):
        with open("./docs/" + doc_file) as f:
            words = re.compile(r"\s+").split(f.read())
            # TODO: get tocken from the word
            for i in range(len(words)):
                self.insert_term(words[i], doc_file, i + 1)

    def create_positional_index(self):
        for doc_file in os.listdir("./docs"):
            self.process_doc(doc_file)

    def save(self):
        self.create_positional_index()
        os.makedirs(os.path.dirname(self.out_file), exist_ok=True)
        with open(self.out_file, 'w') as f:
            f.write(json.dumps(self.pos_index))


if __name__ == "__main__":
    i = PositionalIndex('.out/indexing/inv.json',
                        '.out/indexing/pos_index.json')
    i.save()
