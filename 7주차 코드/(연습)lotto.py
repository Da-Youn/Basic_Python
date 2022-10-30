import random
lotto = []

while len(lotto) <= 6:
    selected = random.randint(1,45)
    if selected in lotto:
        continue
    else:
        lotto.append(selected)

lotto.sort()
print(lotto)

# for i in range(6):
#    print(random.randint(1,45))
