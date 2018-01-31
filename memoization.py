#
#created 1/31/18
#
#top-down -> memoization
#bottom-up -> tabulation
#both are dynamic programming techniques
#memoization

def fib_memoization(n:int, lookup:dict) -> int:
    if n <1:
        return -1
    #base case
    if n == 1 or n == 2:
        lookup[n]=1
    if lookup.get(n, None):
        lookup[n] = fib_memoization(n-1, lookup)+fib_memoization(n-2, lookup)
    return lookup[n]


def fib(n:int) ->int:
    if n<1:
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def main() -> int:
    my_dictionary = {}
    f = fib_memoization(6, my_dictionary)
    print(f)
    f2 = fib_tab(6, my_dictionary)
    print(f2)


if __name__ == '__main__':
    main()

#tabulation:

def fib_tab(n: int)->int:
    f = [0]*(n+1)
    #base case f[1]=1
    for i in range(2,n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]