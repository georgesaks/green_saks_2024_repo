top_cities = ['New York', 'Houston', 'Chicago', 'Los Angles', 'Phoenix']
print(top_cities)
print(top_cities[0])
print(top_cities[-1])
print(top_cities[-5])
print(top_cities[3:])
print(top_cities[:])
print(top_cities[10:15])
print(top_cities[:2])

# DELETING LIST ELEMENTS 
#top_cities = ['New York', 'Houston', 'Singapore' 'Chicago', 'Los Angles', 'Phoenix']
top_cities = ['New York', 'Houston', 'Singapore', 'Chicago', 'Los Angles', 'Phoenix']
del top_cities[:]
print(top_cities)

#ADDING NEW ELEMENT TO LISTS
book_rating =[7,3,4,8,1]
book_rating.append(2)
print(book_rating)

book_rating = [7, 9, 5, 6, 8]
book_rating.insert(2, 3)
print(book_rating)



#ITERATING LIST
top_cities = ['New York', 'Houston', 'Singapore', 'Chicago', 'Los Angles', 'Phoenix']
for big_cities in top_cities:
    print('huge city:' , big_cities )
    
    
    
spendings = [34.5, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent:', sum)


paying = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2987.34, 4069.78, 1000.0]

low = 0
normal = 0
high = 0

for month in paying:
    if month < 1000.0:
        low += 1
    elif month <= 2500:
        normal +=1
    else:
        high += 1
print('Numbers of months with low paying:' + str(low) + ', normal payings: ' + str(normal) + ', high payings: ' + str(high) + '-')






    





