#Carlos Galvan | group 7
#this  recursive function returns the amount of 1s in the equation
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

#this function is the first step into gererating our formula
#it generates a list that contains the steps of how to get to n all the way down to one
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

#this functions convert the floats to int inside the list
def intList(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x

# we take take the list and use it to build the formula
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

#all the code is ran here
while True:
    #User Input
    number = int(input("Enter the number: "))
    #x represent the list
    x = recursionPrinting(number,  [])
    #y represents the CN
    y = recursion(number,0)
    #displays x
    print (x)
    #these function flips it so we can build the formula
    x.reverse()
    intList(x)
    print(x)
    #word symbolizes the written out equation which was generated with eqFormat
    word = eqFormat(x)
    #This statement removes the extra parenthesis that is outside the equation
    #unless the equation is not 1, remove the first and last char
    if len(word) > 1:
        word = word[1:-1]

    #Print everything
    print("C",number," <= ",y)
    #back up clause
    #eval() uses the string version of the equation and calculates it
    #if the Original n is equal to the calculated equation that print
    if number == eval(word):
        print(eval(word), " = ",word )
    #else print and error
    else:
        print("This is wrong")
        break
