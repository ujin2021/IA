prices = {'apple':1500, 'orange':1000, 'pear':2000, 'banana':500, 'pineapple':3000}
my_basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

#show the name of fruits in my basket ending with 'e'(do not show the same names twice)
endWithE = set()
for i in range(0, len(my_basket)):
    if((my_basket[i])[len(my_basket[i])-1] == 'e'):
        endWithE.add(my_basket[i])

print(len(endWithE))