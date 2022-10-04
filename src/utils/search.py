from trie.trienode import *
from trie.trie import *

# TODO:
# Support search target str in the trie.
# Support max layers of search.

def dfs_rec(node:TrieNode, target:str=None, layer:int=None) -> set:
	"""
	Start DFS from a node to print all possible words in the sub-trie of this node.
	"""
	ret = set()
	if node.isword:
		ret.add(node.val)
	for key in node.next:
		ret = ret.union(dfs(node.next[key]))
	return ret

def dfs(node:TrieNode, target:str=None) -> set:
	ret = set()
	if node.isword:
		ret.add(node.val)
	cont = [node.next[key] for key in node.next]
	while cont:
		cur = cont.pop()
		if cur.isword:
			ret.add(cur.val)
		cont += [cur.next[key] for key in cur.next]
	return ret

# TODO:
# Support max layers of search.
def bfs(node:TrieNode, target:str=None, layer:int=None) -> set:
	"""
	Start BFS from a node to print all possible words in the sub-trie of this node.
	"""
	ret = set()
	if node.isword:
		ret.add(node.val)
	cont = []
	for key in node.next:
		cont = [node.next[key]] + cont
	while cont:
		cur = cont.pop()
		if cur.isword:
			ret.add(cur.val)
		for key in cur.next:
			cont = [cur.next[key]] + cont
	return ret

def precise_search(input:str, trie:Trie, reverse=False) -> bool:
	if reverse:
		init = trie.c2tr
	else:
		init = trie.c2t
	if not (input[0] in init):
		return False
	cur = init[input[0]]
	for c in input[1:]:
		if not (c in cur.next):
			return False
		cur = cur.next[c]
	return cur.isword


