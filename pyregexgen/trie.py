from PyRegexGen.trienode import *
class Trie:
	"""
	Basic class of Trie. A DFA that can represents a regular expression
	"""
	def __init__(self, words:set, forward=True, backward=False):
		"""
		Parameters:
		c2t: Character to nodes. A dictionary points to all roots of tries.
		c2tr: Character to nodes(reverse). A dictionary points to all roots of reversely-stored tries.
		null: If the trie set contains an empty string.
		"""
		self.c2t = {}
		self.c2tr = {}
		self.null = False
		for word in words:
			if forward:
				self.generate_forward_trie(word)
			if backward:
				self.generate_backward_trie(word)

	def generate_forward_trie(self, word):
		size = len(word)
		if len(word) == 0:
			# The word is an empty string.
			self.null = True
		else:
			if word[0] in self.c2t:
				# The root of the trie to be generated is already in the trie-set.
				i = 1
				cur = self.c2t[word[0]]
				while (i < size) and (word[i] in cur.next):
					"""
					Loop until branching out of the trie or
					the trie for this word alreayd exists.
					"""
					cur = cur.next[word[i]]
					i += 1
				if i >= size:
					# The trie for this word already exists. Set isword to True.
					cur.isword = True
				else:
					# Branched out of the existing trie. Generate new branch.
					while (i < size):
						cur.next[word[i]] = TrieNode(cur.val + word[i])
						cur = cur.next[word[i]]
						i += 1
					cur.isword = True
			else:
				"""
				Root of the trie that starts with this initial character 
				does exist in the trie-set. Generate a new trie. 
				"""
				cur = TrieNode(word[0])
				self.c2t[word[0]] = cur
				i = 1
				while (i < size):
					cur.next[word[i]] = TrieNode(cur.val + word[i])
					cur = cur.next[word[i]]
					i += 1
				cur.isword = True

	def generate_backward_trie(self, word):
		i = len(word) - 1
		if i == -1:
			self.null = True
			# The word is an empty string.
			pass
		else:
			if word[i] in self.c2tr:
				# The root of the trie to be generated is already in the trie-set.
				cur = self.c2tr[word[i]]
				i -= 1
				while (i >= 0) and (word[i] in cur.next):
					"""
					Loop until branching out of the trie or
					the trie for this word alreayd exists.
					"""
					cur = cur.next[word[i]]
					i -= 1
				if i < 0:
					# The trie for this word already exists. Set isword to True.
					cur.isword = True
				else:
					# Branched out of the existing trie. Generate new branch.
					while (i >= 0):
						cur.next[word[i]] = TrieNode(word[i] + cur.val)
						cur = cur.next[word[i]]
						i -= 1
					cur.isword = True
			else:
				"""
				Root of the trie that starts with this initial character 
				does exist in the trie-set. Generate a new trie. 
				"""
				cur = TrieNode(word[i])
				self.c2tr[word[i]] = cur
				i -= 1
				while (i >= 0):
					cur.next[word[i]] = TrieNode(word[i] + cur.val)
					cur = cur.next[word[i]]
					i -= 1
				cur.isword = True

	def update_trie(self, word, forward=True):
		if forward:
			self.generate_forward_trie(word)
		else:
			self.generate_backward_trie(word)
