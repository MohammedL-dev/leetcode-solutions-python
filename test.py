a = [0, 1, 1, 1, 0, 1]

import random

choice = 0
x = int(input())
a = 0
b = 0
c = 0
d = 0
for i in range(1, x+1):
    # Generate a random length between 3 and 9
    list_length = random.randint(3, 8)

# Generate a list of 0s and 1s with the random length
    random_list = [random.choice([0, 1]) for _ in range(list_length)]
    #random_list.append(1)
    random.shuffle(random_list)
    num_bullet = 0
    for bullet in random_list:
    	num_bullet += bullet
    void_bullet = list_length - num_bullet
    #print(random_list, num_bullet, void_bullet)
    #choice = input()
    #print(0 if random_list[0] == 1 else 1)
    #random_list.pop(0)
    #print(random_list)
    #choice = input()
    a += 1 if num_bullet > void_bullet else 0
    b += 1 if num_bullet < void_bullet else 0
    c += 1 if num_bullet == 0 else 0
    d += 1 if void_bullet == 0 else 0
print(a, b, c, d, x-a-b)