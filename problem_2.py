def problem_2(n):
    # list of fibonacci numbers being initialised
    fib = [1,1]
    
    if n <= 2:
        return fib[n-1]
    else:
        #check for the fibonacci number in the list
        if list(fib) == n:
            return fib[n-1]
        
        else:
            fib_n_1 = problem_2(n-1)
            fib_n_2 = problem_2(n-2)
            fib_sum = fib_n_1 + fib_n_2
            #fib.append(fib_n_1 + fib_n_2)
            return(fib_sum)
            print(fib_sum)

problem_2(10)