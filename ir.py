import os
import argparse

from Tokenize import Tokenize
from InvertedIndex import InvertedIndex
from PositionalIndex import PositionalIndex


def ir():
    parser = argparse.ArgumentParser(
        prog='IR System',
        description='Preprocessing documents and searching system',)
    parser.add_argument('-t', '--tokens', action='store_true')
    parser.add_argument('-p', '--pos-index', action='store_true')
    parser.add_argument('-i', '--inv-index', action='store_true')
    parser.add_argument('-a', '--all', action='store_true')

    args = parser.parse_args()
    tokens = args.tokens or args.all
    inv_index = args.inv_index or args.all
    pos_index = args.pos_index or args.all

    if tokens:
        for file in os.listdir('./docs/'):
            tokenize = Tokenize(file, './.out/tokens')
            tokenize.save()

    if inv_index:
        index = InvertedIndex('./.out/tokens',
                              './.out/indexing/inv_index.json')
        index.get_terms_docs()
        index.create_index()
        index.save_index()

    if pos_index:
        i = PositionalIndex('.out/indexing/inv_index.json',
                            '.out/indexing/pos_index.json')
        i.save()


if __name__ == "__main__":
    ir()

