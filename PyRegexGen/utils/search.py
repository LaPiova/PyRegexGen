from PyRegexGen.trienode import *
from PyRegexGen.trie import *

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

def precise_search(input:str, trie:Trie, partial=False, reverse=False, ignore_space=False):
	"""
	Check if a the input string is exists in the trie.
	Parameters:
	partial: When partial is True, check if the string starts with some
		string that is in the trie.
	reverse: Check if the string exists in the reverse trie.
	ignore_space: Indicates whether spaces in this string will be ignored.
	"""
	if reverse:
		init = trie.c2tr
	else:
		init = trie.c2t
	i = 0
	size = len(input)
	if ignore_space:
		while input[i] == ' ':
			i += 1
	if not (input[i] in init):
		return (False, None)
	ret = []
	cur = init[input[i]]
	if partial:
		if cur.isword:
			ret.append((cur, i))
	for j in range(i + 1, size):
		if not (input[j] in cur.next):
			if (ignore_space and (input[j] == ' ')):
				continue
			return (not (not ret), ret)
		cur = cur.next[input[j]]
		if partial:
			if cur.isword:
				ret.append((cur, j+i+1))
		j += 1
	if ((not partial) and cur.isword):
		ret.append((cur, size - 1))
	return (not (not ret), ret)

def vague_search(s:str, trie:Trie, reverse=False, ignore_space=False, mode=0):
	pass

# TODO:
# Support vague search. e.g. (whether spaces should be ingored or not,
# within which depth should search be performed,
# within which similarity should it be considered as found.
