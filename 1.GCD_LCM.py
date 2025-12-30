a = int(input('please input number A'))
b = int(input('please input number B'))
common_divisor_list = [0] * a
common_divisor = 0
common_multiple = 0
number = 0
if a > b:
    a, b = b, a
for i in range(1, a + 1):
    if a % i == 0 and b % i == 0 and i <= a:
        common_divisor_list[number] = int(i)
        number += 1
number = 0
while True:
    if common_divisor_list[number] > common_divisor:
        common_divisor = common_divisor_list[number]
        number += 1
    else:
        break
number = 0
while common_multiple == 0:
    if number % a == 0 and number % b == 0 and number != 0:
        common_multiple = number
        break
    else:
        number += 1
print(f'The greatest common divisor is{common_divisor}')
print(f'The least common multiple is{common_multiple}')
