num = input().split()
rank = {}
for i in num:
    rank[i] = rank.get(i,0)+1
sorted_rank = sorted(rank)
sorted_rank.reverse()

print(rank[sorted_rank[0]] + rank[sorted_rank[1]] + rank[sorted_rank[2]])


