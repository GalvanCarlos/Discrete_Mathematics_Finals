def recursionPrinting(n, str):
    if n == 0:  # if no number, then 0
        str = "0"
        return str
    elif n == 1:  # once n has been broken down to 1
        str.append(n)
        return str
    elif (n % 2) == 0:  # is even
        str.append(n)
        n /= 2  # n/2
        return recursionPrinting(n,str)
    elif (n % 2) == 1:  # is odd
        str.append(n)
        n = (n - 1)  # (n - 1) + 2
        return recursionPrinting(n, str)
    else:
        print("Not a valid input")



def eqFormat(n):
    eq = ""
    for i in range(len(n)):
        if n[i] == 1: #starting point
            eq = "1"
        elif n[i] == 2: #the second step, requiered to keep things neat
            eq = "( " + eq + " + 1 )"
        elif (n[i] % 2) == 0: #if the number is even, then opposite of /2 is ( X 2 )
            eq = "( " + eq + " * ( 1 + 1 ) )"
        elif (n[i] % 2) == 1:# if the number is odd, the opposite of - 1 is + 1
            eq = "( " + eq + " + 1 )"
        else: #basic else statement
            print("something went wrong")
    return eq

n = [1, 2, 4, 5, 10]
print(eqFormat(n))