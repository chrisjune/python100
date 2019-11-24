number = int(input())
left = []
while number > 0:
    left.append(number % 2)
    number = number // 2

left.reverse()
print(''.join([str(i) for i in left]))
