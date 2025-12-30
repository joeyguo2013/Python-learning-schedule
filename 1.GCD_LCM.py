while True:
    a = input('please input number A ')
    if a == 0 or not a.isdigit():
        print("please don't input character and 0")
    else:
        break
a = int(a)
while True:
    b = input('please input number B ')
    if b == 0 or not b.isdigit():
        print("please don't input character and 0")
    else:
        break
b = int(b)
common_divisor_list = [0] * a
common_divisor = 0
common_multiple = 0
number = 0
if a > b:
    a, b = b, a
for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
        common_divisor_list[number] = int(i)
        number += 1
number = 0
while True:
    if common_divisor_list[number] > common_divisor:
        common_divisor = common_divisor_list[number]
        number += 1
    else:
        break
number = 1
while common_multiple == 0:
    if number % a == 0 and number % b == 0:
        common_multiple = number
    else:
        number += 1
print(f'The greatest common divisor is {common_divisor}')
print(f'The least common multiple is {common_multiple}')
