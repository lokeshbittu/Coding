

from collections import Counter

def searching(word, letters):
    word = set(word)
    count = 0
    for i in word:
        if i in letters:
            count += 1

    return count

def findwords(words, letters):
    list = []
    for word in words:
        n = len(word)
        a = searching(word, letters)
        list.append(a)
    return list

words = ["hi","bye","bebe"]
letters = "iye"

# result = [1,2,1]

print(findwords(words, letters))