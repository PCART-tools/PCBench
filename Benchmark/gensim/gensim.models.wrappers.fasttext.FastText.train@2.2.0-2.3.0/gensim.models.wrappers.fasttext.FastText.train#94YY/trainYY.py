from gensim.models.wrappers import FastText
ft_path = './fasttext'
corpus_file = './corpus.txt'
output_file = './'
model = FastText.train(ft_path,  corpus_file,  output_file,  'cbow',  100,  0.025,  5,  1, loss='ns', sample=0.001, negative=5, iter=1, min_n=3)
