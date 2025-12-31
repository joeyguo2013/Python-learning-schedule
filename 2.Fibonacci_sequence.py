#input number
while True:
    number = input('How far do you want to count the Fibonacci sequence?')
    if not number.isdigit() or int(number) == 0 :
        print("please don't input character and 0")
    else:
        break
number = int(number) + 1
Fibonacci_list =[0] * (number - 1)


#Fibonacci sequence
for i in range(0, number - 1):
    if i == 0 or i == 1:
        Fibonacci_list[i] = 1
    else:
        Fibonacci_list[i] = Fibonacci_list[i - 1] + Fibonacci_list[i - 2]
#print
print(Fibonacci_list)