from tokenized import Tokenize
import os

non_tokenized_path = r'E:\IR_project'
tokenized_path = r'E:\IR_project\tokenized'
if not os.path.exists(tokenized_path):
    os.makedirs(tokenized_path)

tokenized = Tokenize(non_tokenized_path)
extract = tokenized.extract_files()
