#Nested List

cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0][2])


cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)
    
    
    
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)
        
        
# ADDING AND MULTIPLYING 

list_us = ['New York', 'Chicago']
list_uk = ['London', 'Manchester']
list_all = list_us + list_uk
print (list_all)


list_numbers = [0,1] * 10
print(list_numbers)

#String Features
fav_band = 'Green Day'
print(fav_band[6])



fav_band = 'Green Day'
print(fav_band[:6])







