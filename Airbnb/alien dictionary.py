# Time:  O(n)
# Space: O(|V|+|E|) = O(26 + 26^2) = O(1)

import collections


# topo sort
class Solution0:
    def alienOrder(self, words) -> str:
        pre = collections.defaultdict(set)  # {character A : characters that is in front of A}
        is_pre = collections.defaultdict(set)  # {character A : characters that is in front of A}
        n = len(words)
        # get relations between characters using words list
        for i in range(n - 1):
            a, b = words[i], words[i + 1]
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    pre[b[j]].add(a[j])
                    is_pre[a[j]].add(b[j])
                    break
        letters = set(list(''.join(words)))
        cur = [c for c in letters if not pre[c]]
        while len(cur) != len(letters):
            nxt = cur[:]
            for c in cur:
                for after in is_pre[c]:
                    if c in pre[after]:
                        pre[after].remove(c)
                        if not pre[after]:
                            nxt.append(after)
            if nxt == cur:
                return ''
            cur = nxt
        return ''.join(cur)


# DFS solution.
class Solution2(object):
    def alienOrder(self, words):
        visited = {}
        for c in ''.join(words):
            visited[c] = False
        graph = collections.defaultdict(set)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    graph[w1[i]].add(w2[i])
                    break

        def valid(ancestors, curr):
            if curr in ancestors:
                return False # invalid, there is a circle
            if visited[curr]:
                return True
            visited[curr] = True
            for nxt in graph[curr]:
                if not valid(ancestors | {curr}, nxt):
                    return False
            res.append(curr) # add the one which has no prior character
            return True

        res = []
        for p in visited:
            if not valid(set(), p):
                return ''
        return ''.join(res[::-1])
print(Solution2().alienOrder(["a","b","ca","cc"]))

# a: b, c
# b: c