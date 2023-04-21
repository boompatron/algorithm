import heapq
import sys
T = int(input())
for _ in range(T):
    n = int(input())
    heap = []  # 최대 힙
    min_heap = [] # 최소 힙
    visited = [0] * n
    for i in range(n):
        oper, num = sys.stdin.readline().split()

        if oper == 'I':
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(heap, (-int(num), i))
            visited[i] = 1
        else:
            if num == '1':   
                # 이미 제거된 정수 제거
                while heap and not visited[heap[0][1]]:
                    heapq.heappop(heap)
                 # 최댓값 삭제
                if heap:
                    visited[heap[0][1]] = 0
                    heapq.heappop(heap)
                 
            else:             # 최솟값 삭제
                # 이미 제거된 정수 제거
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
				# 최솟값 삭제
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

    if 1 not in visited:
        print('EMPTY')
    else:
        while heap and not visited[heap[0][1]]:
            heapq.heappop(heap)
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)

        print(-heap[0][0], min_heap[0][0])