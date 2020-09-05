#CARLOS GALVAN
import matplotlib.pyplot as plt
import numpy as np
def recursion(n, c):
    if n == 0:  # if no number, then 0
        c += 0
        return c
    elif n == 1:  # once n has been broken down to 1
        if n > c:  # this only applies to 1 other wise C1 --> 0
            c += 1
        return c
    elif (n % 2) == 0:  # is even
        n /= 2  # n/2
        c += 2
        return recursion(n, c)
    elif (n % 2) == 1:  # is odd
        n = (n - 1) / 2  # (n - 1) + 2
        c += 3  # (-1) and /2 all result to the use of 3 Ones
        return recursion(n, c)
    else:
        print("Not a valid input")


x = []
y = []
max = int(input("Enter Number: "))
N = max
colors = []
area = []
diction = {}

for i in range(max):
    x.append(i)
    y.append(recursion(i, 0))
    colors.append(i)
    area.append(i / 10)

title = "1 ≤ n ≤ " + str(max)
plt.title(title)
plt.scatter(x, y, s=5, c=colors, alpha=0.5)
plt.show()
