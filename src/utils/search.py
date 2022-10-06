from trie.trienode import *
from trie.trie import *

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

def step_search(node:TrieNode, c):
	if c in node.next:
		return node.next[c]
	return None

def precise_search(input:str, trie:Trie, reverse=False, ignore_space=False):
	if reverse:
		init = trie.c2tr
	else:
		init = trie.c2t
	i = 0
	if ignore_space:
		while input[i] == ' ':
			i += 1
	if not (input[i] in init):
		return (False, None)
	cur = init[input[i]]
	for c in input[i + 1:]:
		if not (c in cur.next):
			if (ignore_space and (c == ' ')):
				continue
			return (False, cur)
		cur = cur.next[c]
	return (cur.isword, cur)

def vague_search(s:str, trie:Trie, reverse=False, ignore_space=False, mode=0):
	pass

# TODO:
# Support vague search. e.g. (whether spaces should be ingored or not,
# within which depth should search be performed,
# within which similarity should it be considered as found.
