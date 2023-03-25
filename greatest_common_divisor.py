import time
def gcd_range_step(x, y):
    gcd = 1
    for i in range(min(x, y), 1, -1):
        if x % i == 0 and y % i == 0:
            gcd = i
            break
    return gcd

def gcd_range_reversed(x, y):
    gcd = 1
    for i in reversed(range(2, min(x, y) + 1)):
        if x % i == 0 and y % i == 0:
            gcd = i
            break
    return gcd


def gcd_range_norm(x, y):
    gcd = 1
    for i in range(2, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd

start = time.perf_counter()
for i in range(1, 1000000):
    gcd_range_step(100, 1405)
end = time.perf_counter()
print(f'The performance time for gcd_range_step is {end - start}s')

start = time.perf_counter()
for i in range(1, 1000000):
    gcd_range_reversed(100, 1405)
end = time.perf_counter()
print(f'The performance time for gcd_range_reversed is {end - start}s')

start = time.perf_counter()
for i in range(1, 1000000):
    gcd_range_norm(100, 1405)
end = time.perf_counter()
print(f'The performance time for gcd_range_norm is {end - start}s')
