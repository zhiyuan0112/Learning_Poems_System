#!python3

import pickle
from train1 import defaultdictFunc	# for pickle
from util import modelFile
from decode import computeScore, generateAppreciation
import sys

class PoemAppreciationAPI:
	def __init__(self):
		#with open(modelFile, 'rb') as modelFileObj:
		with open("model/model.pickle", 'rb') as modelFileObj:
			self.keywords, self.keywords_characters = pickle.load(modelFileObj)
	
	def appreciate(self, poem, numClauses=3, XMLin=False, XMLout=False):
		if XMLin:
			poem = poem.split(' |||| ')[0]
		scores = computeScore(poem, self.keywords, self.keywords_characters)
		#print(scores[:10])
		result = generateAppreciation(scores, numClauses)
		if XMLout:
			result = '<answer org="BIT—CS">'+result+'</answer>'
		return result

if __name__ == '__main__':
	p = PoemAppreciationAPI()
	poem = '两个黄鹂鸣翠柳，一行白鹭上青天。窗含西岭千秋雪，门泊东吴万里船。' #'床前明月光，疑是地上霜。举头望明月，低头思故乡。'
	result = p.appreciate(poem)
	print(result)
