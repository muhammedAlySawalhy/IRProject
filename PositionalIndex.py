
import os
import json


class positionalIndex:
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
        positionalIndex = {}
        with open(self.inv_index_path, 'r') as f:
            for line in f:
                line = json.loads(line)
                terms = list(line.keys())
                for term in terms:
                    docs = line[term]
                    for doc in docs:
                        position = self.calculate_positions(term, doc)
                        if term not in positionalIndex:
                            positionalIndex[term].append(
                                [len(docs), *position])
        return positionalIndex

    def save(self):
        with open(self.output_dir + '/' + self.file_name, 'w') as f:
            f.write(json.dumps(self.create_positional_index()))


i = positionalIndex('indexing/invertedindex.txt',
                    'indexing/', 'positional_index.txt')

i.create_positional_index()
i.save()
