prices = {'apple':1500, 'orange':1000, 'pear':2000, 'banana':500, 'pineapple':3000}
my_basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

#9.	How much do I pay for the fruits in my basket.

total = 0
i = 0
my_basket.sort()
while(i < len(my_basket)):
    total += prices[my_basket[i]] * my_basket.count(my_basket[i])
    i += my_basket.count(my_basket[i])

print(total)