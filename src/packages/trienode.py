class TrieNode:
	"""
	Basic class of TrieNode.
	"""
	def __init__(self, val, isword=False):
		"""
		parameters:
		val: A string represents the result from root of the trie to this node.
		next: Character keys that points to next node in the trie.
		isword: Indicates if val is a word in the set when trie is generated.
		"""
		self.val = val
		self.next = {}
		self.isword = isword

	def dfs(self):
		"""
		Start DFS from a node to print all possible words in the sub-trie of this node.
		"""
		ret = set()
		if self.isword:
			ret.add(self.val)
		for key in self.next:
			ret = ret.union(self.next[key].dfs())
		return ret
