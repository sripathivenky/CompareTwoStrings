import json
import os
from abc import ABC
from typing import Optional, Awaitable

import jsonschema
import tornado
from tornado import gen
from tornado.web import RequestHandler
from tornado.web import HTTPError
from jsonschema import validate
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CompareTwoStringController(RequestHandler):
    """
    Controller to that implements REST Base for Compare Two String controllers
    """

    def prepare(self) -> Optional[Awaitable[None]]:
        """
        Method that interpret incoming request before action.
        :return: None
        """
        self.default_version = "v1"
        if self.request.path.startswith("/v2/"):
            self.default_version = "v2"

    @gen.coroutine
    def get(self, *args):
        self.send_error(405)
        return NotImplementedError

    @gen.coroutine
    def post(self):
        """
        POST request method, this will read that user input data and it will then be parsed with the JSON data schema.
        Once the schema data is valid we will then be passed down to the Similarity algorithm.
        :return: None
        """
        data = self.request.body
        current_dir = os.path.dirname(__file__)
        schema_file = open(os.path.abspath(f"{current_dir}/../json_input_schema/input_data_file.json"))
        json_object = json.load(schema_file)
        schema_file.close()
        data_object = json.loads(data)
        try:
            validate(data_object, json_object)
        except jsonschema.exceptions.ValidationError as schemaError:
            return self.send_error(400, message="Bad Data")
        value = self.get_jaccard_sim(data_object['text_one'], data_object['text_two'])
        if self.default_version == "v2":
            value = self.get_cosine_sim(data_object['text_one'], data_object['text_two'])
            self.write({"data": value.min()})
            self.finish()
            return

        self.write({"data": value})
        self.finish()
        return

    def get_jaccard_sim(self, str1, str2):
        """
        Implementation Od JAccord algorithm.
        https://en.wikipedia.org/wiki/Jaccard_index
        :param str1: Input String
        :param str2: Input String two to compare
        :return:  score
        """
        # Get the Set values for each word.
        a = set(str1.split())
        b = set(str2.split())
        # Get the intersection of the words
        c = a.intersection(b)
        # Score the based of intersection.
        return float(len(c)) / (len(a) + len(b) - len(c))

    def get_cosine_sim(self, *strs):
        """
        Implementaion of Cosine Similarity
        https://en.wikipedia.org/wiki/Cosine_similarity
        :param strs:
        :return: score
        """
        # Create vectors for the words.
        vectors = [t for t in self.get_vectors(*strs)]
        return cosine_similarity(vectors)

    def get_vectors(self, *strs):
        """
        Helper to generate vectorizer.
        :param strs:
        :return: vectorized object
        """
        text = [t for t in strs]
        vectorizer = CountVectorizer(text)
        vectorizer.fit(text)
        return vectorizer.transform(text).toarray()