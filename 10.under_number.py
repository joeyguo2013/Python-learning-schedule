negative = 0
while True:
    number = input('give me a int number I can let it be under')
    if number.isdigit():
        break
    elif number.startswith('-') and number[1:].isdigit():
        number = number.replace('-', '')
        negative = 1
        break
    else:
        print('please input number')
if int(number) // 2 == 0:
    print(number)
else:
    if negative == 1:
        number = -int(number[::-1])
        print(number)
    else:
        number = number[::-1]
        print(number)