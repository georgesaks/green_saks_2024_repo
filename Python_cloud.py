#WHILE LOOPS
#while condition
 #   print(something)

print(30 // 2)

ages = {'Jones': 30, 'Levi': 25, 'John': 20}
age = ages.get('kevin')
print(age)


def hello(name, sal):
    print(sal, name, sep=",")


for num in range(1, 10, 2):
    if num % 3:
        print(num)
#while 1 < 2:
#    print('something')
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)
    
count = 1
while count <= 4:
    print('looping')
    count += 1

#for loop

#for temp_variable in sequence


    
    
name = input('what is your name? ')

if len(name) >= 6:
    print('Your name is long')
elif len(name) == 5:
    print('your name is exactly 5 characters')
elif len(name) >= 4:
    print('Your name is 4  or more characters')
else:
    print('Your name is short.')




#ages = { 'Kevin' : 59, 'alex' : 23, 'Josh' : 40 }
#print(ages [Kayla] = 21)






my_list = [1, 4, 3, 8, 2]
print(reversed(my_list))



my_list = [1, 4, 3, 8, 2]
print(sorted(my_list))


test_str = 'testing'
print(test_str[0:5])



fahrenheit = float(input('what temperature (in fahrenheit) would you like converted to celsius? '))
celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, 'F is', round(celsius, 2), 'C')


name = input('what is your name? ')
color = input('what is your favorate color: ')
age = int(input('How old are you today? '))

#print('is ' + str(age) + ' years old', end=' ')
#print('and loves the color ' + color + '.', end='')

print(name, 'is', age,'years old and loves the color', color + '.', sep=',')
