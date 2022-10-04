from utils.search import *
import unittest
import time
import random
import string

def generate_random_string(size=15, chars=(string.ascii_uppercase + string.ascii_lowercase + " ")):
	size = random.randint(3, size)
	return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

class TestSearchMethods(unittest.TestCase):
	
	def setUp(self):
		self.words = set()
		self.excl_words = set()
		for _ in range(100):
			self.words.add(generate_random_string())
			self.excl_words.add(generate_random_string())
		self.excl_words -= self.words
		self.trie = Trie(self.words)

	def test_precise_search(self):
		for word in self.words:
			self.assertEqual(True, precise_search(word, self.trie))
		for word in self.excl_words:
			self.assertEqual(False, precise_search(word, self.trie))

if __name__ == '__main__':
	unittest.main()