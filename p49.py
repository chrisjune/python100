number = list(map(int, input().split()))

max = -1
for i in number:
    if max < i:
        max = i
print(max)
