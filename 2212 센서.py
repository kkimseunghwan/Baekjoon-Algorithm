
N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))

cut = []
while len(cut) < K-1:
    max, index = 0, 0
    for i in range(N-1):
        if (arr[i+1] - arr[i]) > max and (i not in cut):
            max = (arr[i+1] - arr[i])
            index = i
    
    cut.append(index)

new_arr = []
l = 0
for i in sorted(cut):
    new_arr.append(arr[l:i+1])
    l = i+1

new_arr.append(arr[l:])

max = 0
for a in new_arr:
    if len(a) > 1:
        max += a[-1] - a[0]

print(max)
