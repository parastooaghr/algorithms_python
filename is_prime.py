#prime_numbers
import time
def is_prime(x):
    prime = True
    for i in range(2,x):
        if x % i == 0:
            prime = False
            break
    return prime

start = time.perf_counter()
for i in range(1,100001):
    is_prime(i)
end = time.perf_counter()
print(end - start)
