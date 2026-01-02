# Input processing
while True:
    a = input('What do you want to find the sum of? ')
    if not a.isdigit() or int(a) == 0:
        print("Please don't input characters or 0")
    elif int(a) >= 10:
        print('Your input cannot be bigger than 10')
    else:
        break
a = int(a)

while True:
    b = input('How many numbers do you want to add? ')
    if not b.isdigit() or int(b) == 0:
        print("Please don't input characters or 0")
    elif int(b) > 10000:
        print('Your computer cannot handle this! It is too big!')
    else:
        break
b = int(b)

# Generate each number
pure_process = [0] * b
number = 0
for i in range(b):
    number = number * 10 + a
    print(number)
    pure_process[i] = number

# Print the sum
print(f'The sum of all numbers is {sum(pure_process)}')
