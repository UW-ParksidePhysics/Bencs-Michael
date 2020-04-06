##3.34
##not going to lie, had trouble with this one so i looked for help online and tore apart a solution to understand how it was done

def sieve(N):
    numbers = list(range(2, (N + 1))) #creates a value called numbers with a range from 2 to n+1
    primes = [] #creates a variable called primes
    for p in range(len(numbers)): #inserts p as variable in given range (numbers)
        if numbers [p] != 0: #if p isnt 0 then...
            primes.append(numbers[p]) #it adds p to list
            for i in range(numbers[p], (N + 1), numbers[p]): #repeats from variable p to max N + 1 with a step of p
                numbers[i - 2] = 0
    return primes #sets resulting list as primes
primes100 = sieve(100)
print(primes100)
