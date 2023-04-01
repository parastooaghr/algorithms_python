def Fibonnaci(n):
    n_2 = 0
    n_1 = 1
    for i in range(1,n+1):
        fib_number = n_1 + n_2
        n_2 = n_1
        n_1 = fib_number
    return fib_number

def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False

count = 1
sum = 0
fib_num = 0

while fib_num < 4*10**6:
    if isEven(fib_num):
        sum = sum + fib_num
    fib_num = Fibonnaci(count)
    count = count + 1

print(sum)




