# coding: utf-8
from __future__ import unicode_literals

import spacy


class LanguageModel(object):
    def __init__(self, nlp_model):
        self._nlp = None
        self.nlp_model = nlp_model

    def create_nlp_pipeline(self):
        try:
            nlp = spacy.load(self.nlp_model)
        except IOError:
            nlp = spacy.load("en")
        return nlp

    @property
    def nlp(self):

        if not self._nlp:
            self._nlp = self.create_nlp_pipeline()
        return self._nlp

    def get_nlp(self):
        return self._nlp