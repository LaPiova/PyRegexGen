from PyRegexGen.trienode import *
from PyRegexGen.trie import *
from PyRegexGen.utils.search import step_search



def backtracking(s:str, idx:int, node:TrieNode):
	pass

def split_words(s:str, trie:Trie, reverse=False)->list:
	cur = None
	if not reverse:
		if not (s[0] in trie.c2t):
			return []
		cur = trie.c2t[s[0]]
	else:
		if not (s[0] in trie.c2tr):
			return []
		cur = trie.c2tr[s[0]]
	# TODO: Precisely split a string without spaces
	# by check if it can be splitted into words that
	# all of them can be found in the trie.
	return []
