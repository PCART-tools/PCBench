from gensim.models import Word2Vec
fname = '/home/zhang/glove.6B.50d.w2v.txt'
model = Word2Vec.load_word2vec_format(fname,  None, binary=False, norm_only=True, encoding='utf8', unicode_errors='strict')
