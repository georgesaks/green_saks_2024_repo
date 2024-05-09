#CHANGING ELEMENT POSITION

first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)


top_cities = ['New York', 'Houston', 'Singapore', 'Chicago', 'Los Angles', 'Phoenix']
top_cities[0], top_cities[5] = top_cities[5], top_cities[0]
print(top_cities)

top_cities = ['New York', 'Houston', 'Singapore', 'Chicago', 'Los Angles', 'Phoenix']
top_cities.sort()
print(top_cities)


random_numbers = [2, 7, -3, 0, 4]
random_numbers.sort()
print(random_numbers)


random_numbers = [2, 7, -3, 0, 4]
random_numbers.sort(reverse=True)
print(random_numbers)


top_cities = ['New York', 'Houston', 'Singapore', 'Chicago', 'Los Angles', 'Phoenix']
print(sorted(top_cities))
print(top_cities)


#CHECKING ELEMENT PRESENCE
invited_guests = ['George', 'Cynthia', 'Anne', 'Maria', 'Joe', 'Adam', 'Keery']
name = input('What is your name? ')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited!')
    
    
#COPYING LISTS
name_original = 'Jon Jones'
name_new = name_original
name_original = 'Dave Saks'
print(name_original, name_new)
    

# LIST COMPREHENSION

#numbers = [1, 2, 3, 4]
numbers = []
for i in range (1,110):
    numbers.append(i)
print(numbers)

#OR 

numbers =[i for i in range (1,101)]
print(numbers)



numbers =[i for i in range (1,101) if i % 3 !=0]
print(numbers)















