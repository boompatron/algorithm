import heapq
from collections import defaultdict


def solution(genres, plays):
    n = len(genres)
    song_by_genre = defaultdict(list)
    plays_sum = defaultdict(int)
    play_hq = []
    ans = []
    for i in range(n):
        plays_sum[genres[i]] += plays[i]
        song_by_genre[genres[i]].append((-plays[i], i))
    for key in song_by_genre.keys():
        song_by_genre[key].sort()
    for key in plays_sum.keys():
        heapq.heappush(play_hq, (-plays_sum[key], key))

    while play_hq:
        total_plays, genre = heapq.heappop(play_hq)
        for i in range(min(2, len(song_by_genre[genre]))):
            ans.append(song_by_genre[genre][i][1])
    return ans