import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from PIL import Image
import urllib.request
import io
import pysftp
import paramiko
from app.machine_learning.schemas.gender_detect_input import GenderDetectNameInput


class GenderDetectionNameBayes:
    model_vector: CountVectorizer = None
    model_bayes = None

    def __init__(self, params_input: GenderDetectNameInput = None, model_path=['./app/machine_learning/ml_modeling/model_bayes_vector.pickle',
                               './app/machine_learning/ml_modeling/model_bayes.pickle']):

        # Load bi vector
        f = open(model_path[0], 'rb')
        self.model_vector = pickle.load(f)
        f.close()

        # Load
        f = open(model_path[1], 'rb')
        self.model_bayes = pickle.load(f)
        f.close()

    def predict_prob(self, params_input: GenderDetectNameInput):
        """
        :param params_input: ["Fullname_1", "Fullname_2"]
        :return: [[predict_prob_for_male, predict_prob_for_female]]
        """
        name_input = params_input.name_input
        processing_input = [self.gender_features(k, self.model_vector, self.model_vector.get_feature_names_out()) for k in name_input]
        classify_gender = self.model_bayes.prob_classify_many(processing_input)
        t = [[x.prob(1), x.prob(0)] for x in classify_gender]
        return t

    def predict(self, params_input: GenderDetectNameInput):
        """
        :param params_input:
        :return: [0/1: male - 1, female - 0]
        """
        name_input = params_input.name_input
        processing_input = [self.gender_features(k, self.model_vector, self.model_vector.get_feature_names_out()) for k in
                            name_input]
        classify_gender = self.model_bayes.classify_many(processing_input)
        t = [x for x in classify_gender]

        return t

    @staticmethod
    def gender_features(full_name, bi_vector, features):
        t = bi_vector.transform([full_name]).toarray()
        return dict(zip(features, t[0]))