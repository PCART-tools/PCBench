from gensim.models.wrappers import FastText
ft_path = 'fasttext'
corpus_file = 'corpus.txt'
output_file = './'
model = FastText.train(ft_path,  corpus_file,  output_file,  'cbow',  100,  0.025,  5,  1,  'ns',  0.001,  5,  1, min_n=3, max_n=6, sorted_vocab=1, threads=12)
