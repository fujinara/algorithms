from typing import (
    List,
)
 
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
 
    def alien_order(self, words: List[str]) -> str:
        g = {c: set() for w in words for c in w}
        for i in range(1, len(words)):
            word1, word2 = list(words[i - 1]), list(words[i])
            minlen = min(len(word1), len(word2))
            if word1[:minlen] == word2[:minlen] and len(word1) > len(word2):
                return ""
            for j in range(minlen):
                if word1[j] != word2[j]:
                    g[word1[j]].add(word2[j])
                    break
        
        color = {}
        for c in g:
            color[c] = 0
 
        order = []
        isPossible = True
 
        def dfs(v):
            nonlocal isPossible
            if not isPossible:
                return
            color[v] = 1
            for i in g[v]:
                if color[i] == 0:
                    dfs(i)
                elif color[i] == 1:
                    isPossible = False
            color[v] = 2
            order.append(v)

        for c in sorted(g.keys(),reverse=True):
            if color[c] == 0:
                dfs(c)

        return "".join(order[::-1]) if isPossible else ""


sol = Solution()
print(sol.alien_order(["wrt","wrf","er","ett","rftt"]))