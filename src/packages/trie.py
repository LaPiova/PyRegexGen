from trienode import *

class TrieDict:
	def __init__(self, words):
		self.c2t = {}
		self.c2tr = {}
		self.empty = set()
		for i in range(len(words)):
			self.save_word(words[i], i)
			self.save_word_r(words[i], i)

	def save_word(self, word, idx):
		size = len(word)
		if len(word) == 0:
			self.empty.add(idx)
		else:
			if word[0] in self.c2t:
				i = 1
				cur = self.c2t[word[0]]
				while (i < size) and (word[i] in cur.next):
					cur = cur.next[word[i]]
					i += 1
				if i >= size:
					cur.idx = idx
				else:
					while (i < size):
						cur.next[word[i]] = Trie(cur.val + word[i])
						cur = cur.next[word[i]]
						i += 1
					cur.idx = idx
			else:
				cur = Trie(word[0])
				self.c2t[word[0]] = cur
				i = 1
				while (i < size):
					cur.next[word[i]] = Trie(cur.val + word[i])
					cur = cur.next[word[i]]
					i += 1
				cur.idx = idx

	def save_word_r(self, word, idx):
		i = len(word) - 1
		if i == -1:
			pass
		else:
			if word[i] in self.c2tr:
				cur = self.c2tr[word[i]]
				i -= 1
				while (i >= 0) and (word[i] in cur.next):
					cur = cur.next[word[i]]
					i -= 1
				if i < 0:
					cur.idx = idx
				else:
					while (i >= 0):
						cur.next[word[i]] = Trie(word[i] + cur.val)
						cur = cur.next[word[i]]
						i -= 1
					cur.idx = idx
			else:
				cur = Trie(word[i])
				self.c2tr[word[i]] = cur
				i -= 1
				while (i >= 0):
					cur.next[word[i]] = Trie(word[i] + cur.val)
					cur = cur.next[word[i]]
					i -= 1
				cur.idx = idx