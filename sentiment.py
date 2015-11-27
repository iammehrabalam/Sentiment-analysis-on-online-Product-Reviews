#!/usr/bin/env python

from __future__ import division
from analysis.preprocess import Cleaner
from analysis.learning import FeatureVectorTfIdf, NaiveBayes

__author__ = 'Md Mehrab Alam'

cleaner = Cleaner()
feature_tfidf = FeatureVectorTfIdf()
classifier = NaiveBayes()


class TrainingAndTesting(object):
    def __init__(self):
        self.cleaner = Cleaner()
        self.feature_tfidf = FeatureVectorTfIdf()
        self.classifier = NaiveBayes()

    def train_me(self, traning_data, traning_data_type):
        data_clean = self.cleaner.lower_and_replace(traning_data)
        t = self.feature_tfidf.extract_features(data_clean)
        self.classifier.training(t, traning_data_type)

    def test_me(self, test_data):
        data_clean = self.cleaner.lower_and_replace(test_data)
        t = self.feature_tfidf.word_vectors_tfidf(data_clean)
        result = self.classifier.testing(t)
        return result

    @classmethod
    def model_evaluation(cls, test_label, original_label):
        if len(test_label) != len(original_label):
            print 'Error!! label length not equal'
            return ''
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for i in range(len(test_label)):
            if test_label[i] == 'negative':
                if test_label[i] == original_label[i]:
                    tn = tn + 1
                else:
                    fn = fn + 1
            else:
                if test_label[i] == original_label[i]:
                    tp = tp + 1
                else:
                    fp = fp + 1
        p = tp + fn
        n = tn + fp
        recall = tp / p
        precision = tp / (tp + fp)
        return {
            'Total Test data:': len(test_label),
            'Correcly predicted': (tp + tn),
            'Wrong Predicted': len(test_label) - (tp + tn),
            'Accuracy': ((tp + tn) / (p + n)) * 100,
            'Error rate': ((fp + fn) / (p + n)) * 100,
            'Recall': recall,
            'precision': precision,
            'f1 score': (2 * precision * recall) / (precision + recall)
        }

    def get_amazon_data(self, query='Mobile', total_reviews=5):
        from amazon import Amazon
        obj = Amazon()
        review, rating = obj.search(query=query, total_reviews=total_reviews)
        return [review, rating]
