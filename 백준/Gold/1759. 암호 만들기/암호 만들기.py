import sys
from itertools import combinations


def solution():
    l, c = map(int, sys.stdin.readline().rstrip().split())
    g = list(map(str, sys.stdin.readline().rstrip().split()))
    g.sort()
    consonant, vowel = 0, 0
    for p in combinations(g, l):
        consonant, vowel = 0, 0
        for i in p:
            if i in ('a', 'e', 'i', 'o', 'u'):
                vowel += 1
            else:
                consonant += 1
        if consonant >= 2 and vowel >= 1:
            print(''.join(p))


if __name__ == '__main__':
    solution()
