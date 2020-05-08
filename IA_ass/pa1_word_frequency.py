'''
처음
the_text = '"Well, I never!", said Alice.'
my_substitutions = the_text.maketrans(
  # If you find any of these
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
  # Replace them by these
  "abcdefghijklmnopqrstuvwxyz                                          ")

# Translate the text now.
cleaned_text = the_text.translate(my_substitutions)
print(cleaned_text)




new_contents = contents.maketrans(
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
  "abcdefghijklmnopqrstuvwxyz                                          ")

cleaned_contents = contents.translate(new_contents) #소문자, 공백으로 치환

word_list = cleaned_contents.split() #공백으로 split

#소유격('s) 처리
for i in range(0, len(word_list)-1):
    if (word_list[i] != 's' and word_list[i+1] == 's'): #단어와 s사이에 '는 공백처리되므로 단어에 's를 붙여준다.
        word_list[i] += "'s"
word_list.remove('s') #'s를 붙여 단어를 만들어줬으므로 s한개는 제거
#print(word_list)
word_set = set(word_list) #중복단어 제거
print(len(word_set))
'''