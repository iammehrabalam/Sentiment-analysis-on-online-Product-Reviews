__author__ = 'Md Mehrab Alam'

import nltk as nt
import re
from config import REGEX, POS_LIST
from analysis.loaders import get_stop_words, get_sentimental_word
from analysis.errors import CustomError
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn


class Cleaner(object):
    def __init__(self):
        '''
        stopwords: set of stopwords
        senti_m_words: set of sentiment words
        '''
        self.stopwords = get_stop_words()
        self.stemmer = nt.PorterStemmer()
        self.senti_m_words = get_sentimental_word()

    def lower_and_replace(self, data):

        '''
        Input:
        -----
        data: list or tuple of document or it may be single document

        Output:
        ------
        return sentiment word (list of list or list)
        '''

        temp = []
        if isinstance(data, list) or isinstance(data, tuple):
            for doc in data:
                temp.append(self._private_replace(doc.lower()))
            return temp
        elif isinstance(data, str):
            return [self._private_replace(data.lower())]

        else:
            raise TypeError('Must be list, tuple or string')

    def _private_replace(self, data):

        '''
        Input:
        -----
        data: single document (string)

        Output:
        ------
        return string
        '''

        for means, pattern in REGEX.iteritems():
            data = re.sub(pattern, " " + means + " ", data)
        data = re.sub('[\.\+\?%_"]+', " ", data)
        return self.filter_sentiment_words(data)

    def _stemming(self, word):
        '''
        Input:
        -----
        word: single word

        Output:
        ------
        return stemmed word
        '''

        try:
            word = self.stemmer.stem(word)
        except:
            pass
        return word

    def filter_sentiment_words(self, data):
        '''
        Input:
        -----
        data: single document (string)

        Output:
        ------
        return string contain sentiment word seprated with space
        '''

        if isinstance(data, list) or isinstance(data, tuple):
            raise CustomError('Must be string')
        collect = []
        for sentence in nt.sent_tokenize(data):
            for word_tag in nt.pos_tag(nt.word_tokenize(sentence)):
                word, tag = word_tag
                if tag in POS_LIST.keys() and (word not in self.stopwords):
                    if word in self.senti_m_words:
                        collect.append(self._stemming(word))
                    else:
                        sen_sets = wn.synsets(word, pos=POS_LIST.get(tag))
                        if sen_sets:
                            a = swn.senti_synset(sen_sets[0].name())
                            if a:
                                if a.obj_score() <= 0.7:
                                    collect.append(self._stemming(word))
        return ' '.join(list(set(collect)))
