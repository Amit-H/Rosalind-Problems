'''
n = number of months
k = number of rabits

fib = each number is the previous 2 added together
'''

def rabbits (n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rabbits(n-1, k) + k*rabbits(n-2, k) # Fibonacci formula plus the k modifier

n = 29
k = 2

print(rabbits(n, k))
