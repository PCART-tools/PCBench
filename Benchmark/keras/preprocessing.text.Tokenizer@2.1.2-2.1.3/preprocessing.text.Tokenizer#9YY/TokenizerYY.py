from keras.preprocessing.text import Tokenizer
texts = ['The quick brown fox jumped over the lazy dog.', 'I never saw a lazy dog jump over a quick fox.']
tokenizer = Tokenizer(None, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\\n', lower=True)
