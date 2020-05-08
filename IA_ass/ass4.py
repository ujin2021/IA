def sentence(basket):
    basket.sort()
    count_dict = {}
    count_list = list()
    result = 'There are '
    count_num = {1: 'a', 2: 'two', 3: 'three'}
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in basket:
        count_dict[i] = basket.count(i)

    for key in count_dict:
        temp_word = ''
        if(count_dict[key] == 1):
            if(key[0] in vowel):
                temp_word = count_num[count_dict[key]] + 'n ' + key
            else:
                temp_word = count_num[count_dict[key]] + ' ' + key

        elif(count_dict[key] == 2 or count_dict[key] == 3):
            temp_word = count_num[count_dict[key]] + ' ' + key + 's'

        else:
            temp_word = 'many ' + key + 's'

        count_list.append(temp_word)

    count_list[len(count_list)-1] = 'and ' + count_list[len(count_list)-1]
    result = result + ', '.join(count_list) + ' in the basket.'

    return result

fruits = ['orange', 'pear', 'pear', 'apple', 'orange', 'banana']
print(sentence(fruits))
#'There are an apple, a banana, two oranges, and two pears in the basket.'
many_oranges = ['apple', 'orange', 'orange', 'orange','pear', 'orange']
print(sentence(many_oranges))
#'There are an apple, many oranges, and a pear in the basket.'