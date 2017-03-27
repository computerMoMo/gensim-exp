#-*- coding:utf-8 -*-
import sys
import gensim
import numpy as np
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

class Mysentences(object):
    def __init__(self, datafile):
        self.datafile = datafile
    def __iter__(self):
        with open(self.datafile, 'r') as f_r:
            for line in f_r.readlines():
                yield line.split()

if __name__ == '__main__':
    # word_vectors = KeyedVectors.load_word2vec_format('/data/GoogleNews-vectors-negative300.bin', binary=True)
    # word_array = np.asarray(word_vectors.word_vec('hello'), dtype=np.float32)
    # print word_array
    # print word_array.shape
    sentences = Mysentences('exp.txt')
    model = Word2Vec(sentences, size=50, min_count=1)
    print model.wv['Anyone']
    model.save('exp_w2v.w2v')
