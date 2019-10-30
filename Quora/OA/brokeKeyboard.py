def solution(words, validLetter):
    validLetter = set(validLetter)
    def judge(word):
        return all(c in validLetter for c in word.lower() if c.isalpha())
    return sum([judge(word) for word in words.split()] or [0])
print(solution('3 + 2 = 5', []))

