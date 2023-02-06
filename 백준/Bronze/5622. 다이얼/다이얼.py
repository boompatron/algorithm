nums = list(input())
time = 0
for i in range(len(nums)):
    if ord(nums[i]) - 65 < 3:           #2
        time += 3
    elif ord(nums[i]) - 65 < 6:         #3
        time += 4
    elif ord(nums[i]) - 65 < 9:         #4
        time += 5
    elif ord(nums[i]) - 65 < 12:         #5
        time += 6
    elif ord(nums[i]) - 65 < 15:         #6
        time += 7
    elif ord(nums[i]) - 65 < 19:         #7
        time += 8
    elif ord(nums[i]) - 65 < 22:         #8
        time += 9
    elif ord(nums[i]) - 65 < 26:         #9
        time += 10
print(time)