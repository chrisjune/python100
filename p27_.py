keys = input().split()
values = list(map(int, input().split()))

dic = {}
for i in zip(keys, values):
    dic[i[0]] = i[1]
print(dic)
