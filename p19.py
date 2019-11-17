num = list(map(int, input().split()))
sum = 1
for i in range(num[1]):
    sum *= num[0]

# num[0] ** num[1]

print(sum)

