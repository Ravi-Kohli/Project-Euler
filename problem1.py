def problem1(n):
    # initialise the list of numbers
    ls = [i for i in range(1,n) if (i%3 == 0 or i%5==0)]
    print (sum(ls))

problem1(1000)

