#IF STATEMENT

#user_age = int(input('what is your age? '))
#if user_age > 30:
#    print('You are over 30 yrs old')
#    print('Sorry you do not qualify')
#elif user_age == 30:
#     print('you are exactly 30 yrs old')
 #    print('You will need to meet the additional conditions to qualify')
#else:
#    print('You are 30 yrs old or younger')
#    print ('Congratulations, you qualify')


#<  less than
#>  greater than
#<= less than or equal
#>= greater than or equal 
## == equals
#!= not equals


password = input('Do you know the secret password? ')
if password != '--secret':
    print('not correct')
else:
    print('correct password')

if True:
    print('conditions met')
    
if 2 == 2:
    print('true')


if 2 == 2.0:
    print('true')
    
    
#JOINING MULTILE CONDITIONS 
user_age = int (input('what is your age? '))
user_country = input('what is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange programm')
else:
    print('Sorry you dont qualify')
    
    
#ANOTHER CONDITION    
user_country = input('what is your country? ')

if user_country == 'Germany' or user_country == 'Sweeden' or user_country == 'Norway':
    print('You can apply for a German student exchange programm')
else:
    print('You are not from Germany')
      
    
#ANOTHER CONDITION
user_age = int (input('what is your age? '))
user_country = input('what is your country? ')
    
if not user_country == 'Germany' and user_age < 25 or user_country == 'Germany' and user_age < 23:
    print('You qualify')
else:
    print('Yon dont qualify')
    
#ORDE    
#    NOT
#    AND 
#    OR


# NESTED STATEMENTS

answer_a =input('Do you like travelling y/n: ')
if answer_a == 'y':
    answer_b == input('And do you like Asia? y/n: ')
    if answere_b == 'y':
        print('Excellent! You can win a ticket to Thailand')
else:
    print('Sorry to hear that')