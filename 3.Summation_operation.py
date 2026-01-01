#input
while True:
    while True:
        a = input('What do you want to find the sum of?')
        if not a.isdigit() or int(a) == 0:
            print("please don't input character and 0")
        else:
            break
    a = int(a)
    while True:
        b = input('How many numbers do you want to add?')
        if not b.isdigit() or int(b) == 0 :
            print("please don't input character and 0")
        else:
            break
    b = int(b)
    if b > 10000:
        print('your computer cannot do this!!!!it was so big!!!')
    else:
        break
pure_process = [0] * b
number = 0
for i in range(0, b):
    number = number * 10 + a
    print(number)
    pure_process[i] = number
#print
print(f'all number sum is {sum(pure_process)}')