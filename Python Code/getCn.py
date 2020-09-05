def recursion(n, c):
    if n == 0:  # if no numbe, then 0
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


nList = []
for i in range(201):
    nList.append(i)

print(nList)

for i in range(len(nList)):
    print("C", i, ": ", recursion(nList[i], 0))

while False:
    number = input("Enter a number to calculate: ")
    print(recursion(int(number), 0))
