# 시간제한 초과 
import sys
 
n = int(sys.stdin.readline())

results = []
for _ in range(3):
    results.append(list(map(int, sys.stdin.readline().split())))

total = []
rank1 = [1]*n
rank2 = [1]*n
rank3 = [1]*n
totalrank = [1]*n
for i in range(n):
    total.append(results[0][i]+results[1][i]+results[2][i])

for i in range(n):
    for j in range(n):
        if results[0][i] < results[0][j]:
            rank1[i]+=1
        if results[1][i] < results[1][j]:
            rank2[i]+=1
        if results[2][i] < results[2][j]:
            rank3[i]+=1
        if total[i] < total[j]:
            totalrank[i]+=1


print(*rank1)
print(*rank2)
print(*rank3)
print(*totalrank)


# Merge sort를 사용한 경우
# 여전히 시간제한 
import sys
 
n = int(sys.stdin.readline())

def merge_sort(arr):
    if len(arr) <2:
        return arr
    mid = len(arr) //2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l=h=0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] > high_arr[h]:
            merged_arr.append(low_arr[l])
            l+=1
        else:
            merged_arr.append(high_arr[h])
            h+=1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr


results = []
for _ in range(3):
    results.append(list(map(int, sys.stdin.readline().split())))

total = []
rank1 = []
rank2 = []
rank3 = []
totalrank = []

for i in range(n):
    total.append(results[0][i]+results[1][i]+results[2][i])

for i in range(3):
    rank1 = merge_sort(results[0])
    rank2 = merge_sort(results[1])
    rank3 = merge_sort(results[2])
    totalrank = merge_sort(total)


for i in results[0]:
    print(rank1.index(i)+1, end = ' ')
print()
for i in results[1]:
    print(rank2.index(i)+1, end = ' ')
print()
for i in results[2]:
    print(rank3.index(i)+1, end = ' ')
print()
for i in total:
    print(totalrank.index(i)+1, end = ' ')
print()


