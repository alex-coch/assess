import sys
from collections import Counter

import spacy

nlp = spacy.load("en_core_web_sm")
input_str = input()  # sys.argv[1]
doc = nlp(input_str.replace("/", " . "))
a = [ent.text for ent in doc.ents if ent.label_ in ('CARDINAL', 'GPE')]
print('<p align=right>')
for i, j in Counter(a).items():
    print(f'"{i}" was found {j}<br>')
print('</p>')
