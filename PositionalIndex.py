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
    def __init__(self, inv_index_path, output_dir, file_name):
        self.output_dir = output_dir
        self.inv_index_path = inv_index_path
        self.file_name = file_name

    def calculate_positions(self, term, doc_id):
        positions = []
        with open('DocumentCollection/' + doc_id, 'r') as f:
            for line in f:
                line = line.split()
                positions.append([line.index(term), doc_id])

        return positions

    def create_positional_index(self):
        pos_index = {}
        with open(self.inv_index_path, 'r') as f:
            inv_index = json.loads(f.read())
            for term in inv_index.keys():
                docs = inv_index[term]
                pos_index[term] = {
                    "term": term,
                    "count": 0,
                    "docs": {}
                }

                for doc in docs:
                    positions = self.calculate_positions(term, doc)
                    pos_index[term]["count"] += len(positions)
                    pos_index[term]["docs"][doc] = positions

        return pos_index

    def save(self):
        with open(self.output_dir + '/' + self.file_name, 'w') as f:
            f.write(json.dumps(self.create_positional_index()))


i = PositionalIndex('indexing/invertedindex.txt',
                    'indexing/', 'positional_index.txt')

i.save()
