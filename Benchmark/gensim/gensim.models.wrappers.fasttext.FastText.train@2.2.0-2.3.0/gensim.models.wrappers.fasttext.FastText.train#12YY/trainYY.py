from gensim.models.wrappers import FastText
ft_path = './fasttext'
corpus_file = './corpus.txt'
output_file = './'
model = FastText.train(ft_path=ft_path, corpus_file=corpus_file, output_file=output_file, model='cbow')
