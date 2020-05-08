#8.	Count the number for each kind of fruits in my basket. (You may represent them as a dict)

prices = {'apple':1500, 'orange':1000, 'pear':2000, 'banana':500, 'pineapple':3000}
my_basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

dict_basket = {}
for i in range(0, len(my_basket)):
    dict_basket[my_basket[i]] = my_basket.count(my_basket[i])
print(dict_basket)