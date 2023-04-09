def password_is_ok(i):
    i = str(i).zfill(5)
    list_digits = [int(j) for j in i]
    a = list_digits[4] + list_digits[2] == 14
    b = list_digits[0] == 2 * list_digits[1] - 1
    c = list_digits[3] == list_digits[1] + 1
    d = list_digits[1] + list_digits[2] == 10
    e = sum(list_digits) == 30
    if a * b * c * d * e:
        return True

for i in range(0, 10 ** 5):
    if password_is_ok(i):
        print(i)
