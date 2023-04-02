#roll a dice and see if after 1,000,000 times oof rolling, the probability of the numbers of dice is the same.
import random
import matplotlib.pyplot as plt
random.seed()
dice_num = []
for i in range(0,6):
    dice_num.append(0)

for i in range(0,1000000):
    dice = random.randrange(0,6)
    dice_num[dice] = dice_num[dice] + 1

plt.bar(range(1,7),dice_num)
plt.show()
print(dice_num)
