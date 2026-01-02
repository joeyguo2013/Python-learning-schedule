#input
while True:
    number = input('What factorial do you want to multiply to?')
    if not number.isdigit() or int(number) == 0 :
        print("please don't input character and 0")
    elif int(number) > 30:
        print('your computer cannot do this!!!!it was so big!!!')
    else:
        break
number = int(number)
final_number = 0
process = 1
#Operations
for i in range(1, number + 1):
    process = process * i
    final_number = process + final_number
#print
print(f'The final number is {final_number}')