from PyRegexGen.utils.search import *
import unittest
from pdb import set_trace
import time
import random
import string

def generate_random_string(size=15, chars=(string.ascii_uppercase + string.ascii_lowercase + " ")):
	size = random.randint(3, size)
	return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

def eliminate_space(input:str)->str:
	ret = ""
	for c in input:
		if c == ' ':
			continue
		ret += c
	return ret

class TestSearchMethods(unittest.TestCase):
	
	def setUp(self):
		self.words = set()
		self.excl_words = set()
		self.words_no_space = set()
		for _ in range(100):
			word = generate_random_string()
			self.words.add(word)
			self.words_no_space.add(eliminate_space(word))
			self.excl_words.add(generate_random_string())
		self.excl_words -= self.words
		self.trie = Trie(self.words)
		self.trie_no_space = Trie(self.words_no_space)
		self.btrie = Trie(self.bad_words)

	def test_precise_search(self):
		for word in self.words:
			ret, node = precise_search(word, self.trie)
			self.assertEqual(True, ret)
		for word in self.excl_words:
			ret, node = precise_search(word, self.trie)
			self.assertEqual(False, ret)

	def test_precise_search_ignore_space(self):
		for word in self.words:
			ret, node = precise_search(word, self.trie_no_space, ignore_space=True)
			self.assertEqual(True, ret)
		for word in self.excl_words:
			ret, node = precise_search(word, self.trie, ignore_space=True)
			self.assertEqual(False, ret)


if __name__ == '__main__':
	unittest.main()