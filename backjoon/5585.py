import sys

money = 1000 - int(sys.stdin.readline())
# count = 0
#
# coin500 = money//500
# money = money%500
#
# coin100 = money//100
# money = money%100
#
# coin50 = money//50
# money = money%50
#
# coin10 = money//10
# money = money%10
#
# coin5 = money//5
# money = money%5
#
# coin = money//1
#
# print(coin500 + coin100 + coin50 + coin10 + coin5 + coin)

coin = [500, 100, 50, 10, 5, 1]
count = 0
for i in range(len(coin)):
    count += money//coin[i]
    money %= coin[i]
print(count)