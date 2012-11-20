# -*- coding: utf-8 -*-

import logging
from MyConfig import MyConfig
from query import *

class PassageAlgorythm(object):

	@classmethod
	def calculate_score(self, question, text):
		pass

class SimilarityAlgorithm(PassageAlgorythm):

	@classmethod
	def calculate_score(self, question, passage):
		rank = passage.document.rank
		q = question.text
		text = passage.text

		# Remove stopwords from question and passage
		# and split it into words
		q = StopwordsAlgorythm.formulate_query(q).split()
		text = StopwordsAlgorythm.formulate_query(text).split()

		# Filter all words in passage that they are
		# not present in question
		words = filter(lambda x: x in q, passage.text.split())

		# Our initial score is the number of coincidences
		score = len(words)

		try:
			num = int(MyConfig.get("search_engine", "n_results"))
		except:
			logger = logging.getLogger("qa_logger")
			logger.warning("search_engine:n_results not found")
			return score

		# Reverse rank order from 1..n to n..1
		rank = num - rank + 1

		# Normalize rank from n..1 to 1..0
		rank = (rank - 1) / (num - 1)

		# Weight score by rank
		score = score * rank

		return score
