names = input().split()
dic = {}
for name in names:
    dic[name] = dic.get(name, 0) + 1

max_name=''
for key, value in dic.items():
    if not max_name or dic[max_name] < value:
        max_name = key

print(max_name,'가 총', dic[max_name],'표로 반장이 되었습니다')

