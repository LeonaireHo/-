# n = 4
# coin = 21
# pays = [2, 1, 4, 3]

entre = list(map(int,input().split()))
n = entre[0]
coin = entre[1]
pays = list(map(int,input().split()))#第二行为每个房间要支付的数量

resultat = 0
while n>0:
    total = sum(pays)
    tour = coin // total #先算他一共可以完整的玩几轮
    coin = coin % total
    resultat += n * tour
    min_pay = min(pays)
    if coin < min_pay:
        break;
    pays.remove(max(pays)) #不能玩一整轮就删掉最大的房间再继续
    n -= 1
print(resultat)


# total = sum(pays)
# min_pay = min(pays)
# fini_tour = coin // total #先算他一共可以完整的玩几轮
# resultat = fini_tour * n
# reste = coin % total
# i = 0
# while reste >= min_pay:#再算不能玩完一整轮时的情况
#     if reste <= pays[i]:
#         reste -= pays[i]
#         resultat += 1
#     i = (i + 1) % n
# print(resultat)