class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def k_edit_distance(words, target, k):
    # build trie
    root = TrieNode()
    for w in words:
        curr = root
        for c in w:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = w

    res = []

    # preDist[j] means the edit distance between curr and target[:j]
    def dfs(curr, preDist, node):
        if node.word:
            if preDist[len(target)] <= k:
                res.append(curr)

        for c in node.children:
            curDist = [0] * (len(target) + 1)
            curDist[0] = len(curr) + 1
            for j in range(1, len(preDist)):
                '''
                如果dp[i][j]表示当前trie树所构成的prefix字符串的前i个字符和target字符串的
                前j个字符的编辑距离的话，按照以前的做法，如果当前第i个和第j个字符不相同的话，则有目前的对应关系： 
                dp[i - 1][j - 1] + 1 replace => prevDp[j - 1] + 1 
                dp[i][j - 1] + 1 insert => dp[j - 1] + 1
                dp[i - 1][j] + 1 delete => prevDp[j] + 1
                '''
                if target[j - 1] == c:
                    curDist[j] = preDist[j - 1]
                else:
                    curDist[j] = min(curDist[j - 1], preDist[j], preDist[j - 1]) + 1
            dfs(curr + c, curDist, node.children[c])  #

    dfs('', list(range(len(target) + 1)), root)

    return res


print(k_edit_distance(["abcd", "abc", "abd", "ad", "c", "cc"], 'abcd', 2))
