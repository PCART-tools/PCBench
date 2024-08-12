from gensim.models.wrappers import FastText
ft_path = 'fasttext'
corpus_file = 'corpus.txt'
output_file = './'
model = FastText.train(ft_path,  corpus_file, output_file=output_file, model='cbow', size=100, alpha=0.025, window=5, min_count=1, loss='ns', sample=0.001, negative=5, iter=1, min_n=3, max_n=6, sorted_vocab=1)
