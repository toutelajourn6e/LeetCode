class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words)
        memo = {}
        ans = []

        def check(word, depth):
            if word in memo:
                return

            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]
                if new_word in words_set or not word:
                    memo[word] = True
                    ans.append(depth + 1)
                    check(new_word, depth + 1)

        for word in sorted(words, key=len, reverse=True):
            check(word, 1)
        
        return max(ans) if ans else 1

            