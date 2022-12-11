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

    def calculate_positions(self, term, doc_id):
        positions = []
        with open('docs/' + doc_id, 'r') as f:
            for line in f:
                line = line.split()
                if term not in line: continue
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
        os.makedirs(os.path.dirname(self.out_file), exist_ok=True)
        with open(self.out_file, 'w') as f:
            f.write(json.dumps(self.create_positional_index()))


if __name__ == "__main__":
    i = PositionalIndex('.out/indexing/inv.json',
                        '.out/indexing/pos_index.json')
    i.save()
