counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished')    


secret_number = 14
user_input = int(input('Try to guess the secret number from 0 t0 20: '))
while user_input != secret_number:
    print('wrong!')
    user_input = int(input('Try to guess the secret number from 0 t0 20:'))
print('Perfect! You guessed the secret number')


#FOR LOOPS

for letter in 'hello!':
    print('current letter:' , letter)
    

#FOR NUMBERS
for counter in range(1,11,3):
    print(counter)
print('Finish')

#=====================================================================================================
#   BREAK AND CONTINUE

while True:
    name = input('Enter your name or EXIT to clsoe the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)


for i in range (1,21):
    if i % 5 == 0:
        continue
    print(i)




#i = 2 
#while i < 5:
    print(i)
#else:
 #   print('else:', i)



python_released = 1994
user_input = int(input('guess the year when python 1.0 was realeased? '))
while user_input != python_released:
    print('wrong!')

    print('Hint year is greater input year on new line ')
    user_input = int(input('guess the year when python was released? '))
print('correct')







