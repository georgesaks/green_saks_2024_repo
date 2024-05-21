
#LIST

city_1 = 'New_York  city'
city_2 = 'Los Angles' 
city_3 = 'Chicago'
city_4 = 'Houston'
city_5 = 'Phoenix' 

top_cities = ['New York city', 'Los Angles', 'Chicago', 'Houston', 'Phoenix']
#print(top_cities)

#print(top_cities[0:2])
#print(top_cities[2:])
#print(top_cities)


#DEL LIST

top_cities = ['New York city', 'Los Angles', 'Sigapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[:]
#print(top_cities)

#ADDING LIST

book_rating = [6, 9, 0, 4]
book_rating.append(4)
#print(book_rating)

book_rating = [6, 9, 0, 4]
book_rating.insert(1, 10)
#print(book_rating)

#lterating List
spendings = [32.4, 20.5, 8.4, 45.0]
sum = 0.0
for spending in spendings:
    sum += spending
#    print('Money spent:', sum)




#CHANGING ELEMENT POSITION

top_cities = ['New York city', 'Los Angles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0],top_cities[4] = top_cities[4], top_cities[0]
#print(top_cities)

top_cities = ['New York city', 'Los Angles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
#print(top_cities)


#CHECKING ELEMENT PRESENSE
invited_guess = ['kate', 'Dave', 'Mary', 'Joe', 'Anne']
name = input('what is your name? ')
#if name in invited_guess:
#    print('Welcome')
#else:
#    print('You are not invited ')


#LIST COMPREHENSION


#numbers = [i for i in range(1, 101)]
#print(numbers)

#numbers = [i for i in range(1, 101) if i % 3 != 0]
#print(numbers)


#Add and Multiplying

list_numbers = [0, 1] * 10
print(list_numbers)


text = 'please capitalize me'
text_cap = text.upper()
print(text_cap)


#tuple

first = 5
second = 7
first, second = second, first



greades = {}
greades['John'] = 'A-'
greades['Mary'] = 'B'
print(greades)

greades.update({'John': 'A'})
print(greades)



def greet ():
    print('Hello_World.py')
greet()