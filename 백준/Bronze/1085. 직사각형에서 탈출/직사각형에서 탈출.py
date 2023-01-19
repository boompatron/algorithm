x, y, w, h = map(int, input().split())
length = [x, y, abs(w - x), abs(y - h)]
print(min(length))