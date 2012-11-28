# -*- coding: utf-8 -*-

import logging
import Passage

from MyConfig import MyConfig

# Algorithms for Document Segmentation

class DocumentSegmentationAlgorithm(object):

	@classmethod
	def split_into_passages(self, document):
		pass


class FixedNumberOfLinesAlgorithm(DocumentSegmentationAlgorithm):

	@classmethod
	def split_into_passages(self, document, text):
		lines = document.split("\n")
		passage_list = []

		try:
			n_lines = int(MyConfig.get("passage_retrieval", "n_lines"))
		except:
			n_lines = 5

		# Iterating over the lines of the document
		# obtaining overlapped passages:
		# 	max(1, len(lines)-n_lines+1)
		# Don't ask: magic numbers ;-)
		for i in range(0, max(1, len(lines)-n_lines+1)):
			lines_of_text = lines[i : i+n_lines]
			# Join list of lines
			piece_of_text = "\n".join(lines_of_text)
			passage_list.append(Passage(piece_of_text, document))

		return passage_list


class SplitIntoParagraphsAlgorithm(DocumentSegmentationAlgorithm):

	@classmethod
	def split_into_passages(self, document, text):
		paragraphs = text.split("\n")

		passage_list = []
		# Iterating over the lines of the document
		# obtaining overlapped passages:
		# 	max(1, len(lines)-n_lines+1)
		# Don't ask: magic numbers ;-)
		for paragraph in paragraphs:
			passage_list.append(Passage(paragraph, document))

		return passage_list

