#-*- coding:utf-8 -*-
import sys
import gensim
import numpy as np
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


class MySentences(object):
    def __init__(self, datafile):
        self.datafile = datafile

    def __iter__(self):
        with open(self.datafile, 'r') as f_r:
            for line in f_r.readlines():
                yield line.split()

if __name__ == '__main__':
    word_vectors = KeyedVectors.load_word2vec_format('exp-vec.txt', binary=False)
    word_array = np.asarray(word_vectors.word_vec('rewrite'), dtype=np.float32)
    print word_array
    print word_array.shape
    w_vocab = word_vectors.vocab
    fre = w_vocab.get('rewrite')
    print type(w_vocab)
    print len(w_vocab)
    print fre.count
    print type(fre)
    # sentences = Mysentences('exp.txt')
    # model = Word2Vec(sentences, size=50, min_count=1)
    # model.wv.save_word2vec_format('exp-vec.txt',  binary=False)
