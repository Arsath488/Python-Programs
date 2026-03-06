from collections import Counter


n = int(input())
words = []

for _ in range(n):
    words.append(input().strip())


word_counts = Counter(words)


print(len(word_counts))


print(*(word_counts.values()))
