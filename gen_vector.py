import gensim
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
glove_file = './data/embeddings/glove.6B.300d.txt'
tmp_file = './data/embeddings/word2vec-glove.6B.300d.txt'
glove2word2vec(glove_file, tmp_file)
