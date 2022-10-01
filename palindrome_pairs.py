import sys
from heapq import heappush, heappop, heappushpop

def palindromePairs(words):
	class Trie:
		def __init__(self, val):
			self.val = val
			self.next = {}
			self.idx = None

		def get_all(self):
			ret = []
			if self.idx != None:
				ret += [(self.val, self.idx)]
			for key in self.next:
				ret += self.next[key].get_all()
			return ret


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
					
	def ispal(word):
		i = 0
		j = len(word) - 1
		while (i < j):
			if (word[i] != word[j]):
				return False
			i += 1
			j -= 1
		return True

	trie = TrieDict(words)
	ret = []
	for i in range(len(words)):
		j = 0
		length = len(words[i])
		if (length == 0):
			continue
		if not (words[i][j] in trie.c2tr):
			continue
		cur = trie.c2tr[words[i][j]]
		j += 1

		to_visit = []

		while (j < length) and (len(cur.next) != 0):
			if not (words[i][j] in cur.next):
				break
			if cur.idx != None:
				to_visit.append((cur, j))
			cur = cur.next[words[i][j]]
			j += 1
		if cur.idx != None:
			to_visit.append((cur, j))
		if not to_visit:
			if (j == length):
				if (cur.idx == i):
					for idx0 in trie.empty:
						ret += [[idx0, i], [i, idx0]]
				if (cur.idx != None) and (i != cur.idx):
					ret.append([i, cur.idx])
				if (len(cur.next) > 0):
					passed = len(cur.val)
					vals = cur.get_all()
					for s, idx in vals:
						if ispal(s[:-passed]) and (i != idx):
							ret.append([i, idx])
			else:
				if (cur.idx != None) and ispal(words[i][j:]):
					ret.append([i, cur.idx])
		else:
			for cur, j in to_visit:
				if (j == length):
					if (cur.idx == i):
						for idx0 in trie.empty:
							ret += [[idx0, i], [i, idx0]]
					if (cur.idx != None) and (i != cur.idx):
						ret.append([i, cur.idx])
						continue
					if (len(cur.next) > 0):
						passed = len(cur.val)
						vals = cur.get_all()
						for s, idx in vals:
							if ispal(s[:-passed]) and (i != idx):
								ret.append([i, idx])
				else:
					if (cur.idx != None) and ispal(words[i][j:]):
						ret.append([i, cur.idx])
	return ret

print(palindromePairs(words))