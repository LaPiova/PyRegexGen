from utils.search import *
import time

test1 = Trie(["test", "teast", "tebst", "tesa", "tesb"])
print(dfs_rec(test1.c2t['t']))
print(dfs(test1.c2t['t']))
print(bfs(test1.c2t['t']))
