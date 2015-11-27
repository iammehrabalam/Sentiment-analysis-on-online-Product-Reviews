__author__ = 'Md Mehrab Alam'

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB as Mnb


class FeatureVectorTfIdf(object):

    def __init__(self):
        self.cvector_obj = CountVectorizer()
        self.tfidf_obj = TfidfTransformer(norm="l2")

    def extract_features(self, data):
        # fit_transform get train data and extract features

        count_vect = self.cvector_obj.fit_transform(data)
        return self.tf_idf_vector(count_vect)

        # You can get the list of features
        # print self.cvector_obj.get_feature_names()

    def word_vectors_tfidf(self, vect_data):
        '''convert documents into matrix'''

        vect_data = self.cvector_obj.transform(vect_data)
        return self.tf_idf_vector(vect_data)

    def tf_idf_vector(self, vect_data):
        '''convert documnet matrix into idf matrix '''
        self.tfidf_obj.fit(vect_data)

        '''convert into tf-idf matrix'''
        tfidf = self.tfidf_obj.transform(vect_data)
        return tfidf


class NaiveBayes(object):
    def __init__(self):
        self.naive_obj = Mnb()

    def training(self, tfidf_vect, tclass):
        self.train = self.naive_obj.fit(tfidf_vect, tclass)

    def testing(self, tfidf_vect):
        test = self.train.predict(tfidf_vect)
        return test
