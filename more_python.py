#print('Hello_World!', end='.')

#first_name = 'John'
#print('Your first name is', first_name, 'Welcome!', sep='-', end='.')

#IF STATEMENTS

user_age = int(input('what is your age? '))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry you dont qualify')
elif user_age == 30:
    print('You are exactly 30 years')
else:
    print('You are 30 years old or younger')
    print('Congratulations, you qualify')
    
    
password = input('Do you know the secret password? ')
if password != '--secret':
    print('not correct')
else:
    print('correct password')
    
    
    
    
    
answer_a = input('Do you like travelling ? y/n')
if answer_a == 'y':
    print('Good')
else:
    print('sorry to hear that!')
    
    
    
counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('finished')


#FOR LOOPS
for shoe in 'Hello!!':
    print('current shoe:', shoe)
    
    
    
    
for counter in range(1,30, 3):
    print(counter)
print('finsihed')



#BREAK

while True:
    name = input('Enter your name or Exit to close the program: ')
    if (name == 'Exit'):
        break
    print('Hello', name)
    
    
#CONTINUE
for i in range (1,21):
    if i % 5 == 0:
        continue
    print(i)
    
    
print('pass' + 'word')
    
    
    
        # TODO: write code...)