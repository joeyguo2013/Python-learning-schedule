#input number
while True:
    while True:
        a = input('please input number A ')
        if not a.isdigit() or int(a) == 0 :
            print("please don't input character and 0")
        else:
            break
    a = int(a)
    while True:
        b = input('please input number B ')
        if not b.isdigit() or int(b) == 0 :
            print("please don't input character and 0")
        else:
            break
    b = int(b)
    if a > b:
        a, b = b, a
    if b - a > 10000:
        print('your computer cannot do this!!!!it was so big!!!')
    else:
        break
#Initialize
common_divisor_list = [0] * a
common_divisor = 0
common_multiple = 0
number = 0
#GCD
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
#LCM
number = a
while common_multiple == 0:
    if number % a == 0 and number % b == 0:
        common_multiple = number
    else:
        number += 1
#print
print(f'The greatest common divisor is {common_divisor}')
print(f'The least common multiple is {common_multiple}')
