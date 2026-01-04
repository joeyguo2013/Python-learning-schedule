while True:
    number_one = input('every list have how many number?')
    if not number_one.isdigit() or int(number_one) == 0 :
        print("please don't input character and 0")
    elif int(number_one) > 10:
        print('your computer cannot do this!!!!it was so big!!!')
    else:
        break
#list number's number
number_one = int(number_one)
#a space Variables
number = 0
list_number = 0
one = [0] * number_one
two = [0] * number_one
number_two = 0
same = [0] * (number_one * number_one)
different = [0] * (number_one * number_one)
same_number = 0
different_number = 0


while list_number < number_one:
    number = input(f'input list "one" number {list_number + 1} number')
    if not number.isdigit():
        print("please don't input character")
        continue
    else:
        number = int(number)
        one[list_number] = number
        list_number += 1
list_number = 0
while list_number < number_one:
    number = input(f'input list "two" number {list_number + 1} number')
    if not number.isdigit():
        print("please don't input character")
        continue
    else:
        number = int(number)
        two[list_number] = number
        list_number += 1
for k in range(number_one):
    if two[k] in one:
        same[same_number] = two[k]
        same_number += 1
    else:
        different[different_number] = two[k]
        different_number += 1
while 0 in same:
    same.remove(0)
while 0 in different:
    different.remove(0)
print(f'list one and list two same got {same}')
print(f'list one and list two different got {different}')