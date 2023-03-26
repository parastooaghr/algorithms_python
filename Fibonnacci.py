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

count = 0
num = 0
sum = 0
while num < 20:
    num = Fibonnaci(count)
    if isEven(num):
        sum = sum + num
    count = count + 1
print(sum)




