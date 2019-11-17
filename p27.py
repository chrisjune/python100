name = input().split()
score = list(map(int, input().split()))

dic = {}
for i in range(len(name)):
    dic[name[i]]=score[i]

print(dic)
