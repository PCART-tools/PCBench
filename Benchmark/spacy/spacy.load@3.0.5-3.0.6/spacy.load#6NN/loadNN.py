import spacy
from pathlib import Path
model_name = 'en_core_web_sm'
disable_components = ['ner', 'parser']
exclude_components = ['tagger']
custom_config = {'nlp': {'batch_size': 1000}}
nlp = spacy.load(model_name,  disable_components,  exclude_components)
doc = nlp('This is a sample text for processing in spaCy.')
for token in doc:
    print(token.text, token.lemma_, token.pos_)
