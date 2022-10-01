
class Trie:
	def __init__(self, val):
		self.val = val
		self.next = {}
		self.idx = None

	def dfs(self):
		ret = []
		if self.idx != None:
			ret += [(self.val, self.idx)]
		for key in self.next:
			ret += self.next[key].dfs()
		return ret
