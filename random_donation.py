#there are 50 people in a room with 100$ each, if each time we nootify them, they give 1 dollar to a random person in the group!
import random
random.seed()
money = 50
num = 50
money_each = []
for i in range(num):
    money_each.append(money)
#print(money_each)
count = 0
#while len(money_each) > 1:
for i in range(0, 10000):
    for i in range(len(money_each)):
        receiver_num = random.randrange(0,len(money_each))
        while money_each[receiver_num] == 0:
            receiver_num = random.randrange(0, len(money_each))

        if money_each[i] != 0:
            money_each[i] = money_each[i] - 1
            money_each[receiver_num] = money_each[receiver_num] + 1
    count = count + 1
print(money_each)
