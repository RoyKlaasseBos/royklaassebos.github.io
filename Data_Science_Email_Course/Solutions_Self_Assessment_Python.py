
# coding: utf-8

# # Data Science Self-Assessment - Solutions (Python)

# For the corresponding questions (by Galvanize) see my [Github page](https://github.com/RoyKlaasseBos/self-study-resources/blob/master/DSI-Self-Assessment.pdf).
# 
# *__Disclaimer__: Although I double checked my answers, I cannot guarantee that they are correct. So if you spot any typos or bugs let me know!*

# ## Spot the Differences

# ### For Loops

# **Script 1**  
# The program will print the value of `total` for each iteration of the `for`-loop. Since total is reset to 0 for each iteration, the output will be:
# ```python
# 1
# 2
# 3
# ```

# **Script 2**  
# After each iteration of the `for`-loop the current value of `total` is printed, which comes down to: 
# ```python
# 1
# 3
# 6
# ```

# **Script 3**  
# The difference with script 2 is that total is only printed once (after the `for`-loop). 
# ```python
# 6
# ```

# ### For Loops

# **Script 1**  
# As you can see below, only `cat` is retured since the `return`-statement immediatetely breaks the `for`-loop.

# In[15]:

# Script 1
def my_function1(my_list):
    output = []
    for item in my_list:
        output.append(item)
        return item
    
print(my_function1(['cat', 'bad', 'dad']))


# **Script 2**  
# Here is the same problem as in script 1 (the `return`-statement is part of the `for`-loop) and thus the output will only be `cat`.
# ```python
# 'cat'
# ```

# **Script 3**  
# This script returns the last item of `my_list` (`dad`) because that is the value of `item` once the `for`-loop finishes. 
# ```python
# 'dad'
# ```

# **Script 4**  
# Because the list `output` is reset to `[]` after each iteration of the `for`-loop `my_function4()` will return `dad` (an empty `output` list  appended with the last item of `my_list`).
# ```python
# 'dad'
# ```

# **Script 5**  
# This time the list is not emptied after each iteration so that the return value will be a list `output` that contains all elements of `my_list`. Note that calling `my_function5()` twice will give exactly the same output as the `output` list is emptied again.
# ```python
# ['cat', 'bad', 'dad']
# ['cat', 'bad', 'dad']
# ```

# **Script 6**  
# Now `output` has become a global variable (list) which is not reset for each `my_function6()` function call. In other words, the elements of `my_list` for the second function call are appended to the existing values of `my_list`. 
# ```python
# ['cat', 'bad', 'dad']
# ['cat', 'bad', 'dad', 'cat', 'bad', 'dad']
# ```

# ### Make a function

# (1) We want a function that takes a list of numbers and returns that list where 10 was added to each number.

# In[14]:

# using a list-comprehension
def list_add_10(list_num):
    return [num + 10 for num in list_num]

print(list_add_10([1,2,3]))


# In[3]:

# alternatively 
def list_add_10(list_num):
    output = []
    for num in list_num:
        output.append(num+10)
    return output

print(list_add_10([1,2,3]))


# (2) We want a function that takes in a list of strings and returns the list with the length of the words.

# In[4]:

# using a list-comprehension
def list_length_words(list_words):
    return [len(word) for word in list_words]

print(list_length_words(['great', 'job', 'so', 'far']))


# In[5]:

# alternatively 
def list_length_words(list_words):
    output = []
    for word in list_words:
        output.append(len(word))
    return output

print(list_length_words(['great', 'job', 'so', 'far']))


# ## More Advanced Python Challenges

# **Challenge 1**   
# Write a function that looks at the number of times the given letters appear in a document. The output should be a dictionary.

# In[13]:

def read_file(file_name):
    with open(file_name) as file_object:
        return file_object.readlines()

# dictionary comprehension
def letter_counter(file_name, letters_to_count='aeiou'):
    '''Returns the number of times specified letters appear in a file'''
    text = read_file(file_name)
    return {letter.lower(): text[0].count(letter) for letter in list(text[0])}
                             
print(letter_counter('lorem_ipsum.txt'))


# In[12]:

def read_file(file_name):
    with open(file_name) as file_object:
        return file_object.readlines()

# alternatively 
def letter_counter(file_name, letters_to_count='aeiou'):
    '''Returns the number of times specified letters appear in a file'''
    text = read_file(file_name)

    letter_frequency = {}
    for letter in list(text[0]):
        letter_frequency[letter.lower()] = letter_frequency.get(letter, 0) + 1        
    return letter_frequency
    
print(letter_counter('lorem_ipsum.txt'))


# **Challenge 2**  
# Write a function that removes one occurence of a given item from a list. Do not use methods `.pop()` or `.remove()`! If the item is not present in the list, output should be `The item is not in the list`.

# In[8]:

def remove_item(list_items, item_to_remove):
    '''Remove first occurence of item from list'''
    return list_items[0:list_items.index(item_to_remove)] + list_items[list_items.index(item_to_remove)+1:]     if item_to_remove in list_items else 'The item is not in the list'

print(remove_item([1,3,7,8,0,7], 3))
print(remove_item([1,3,7,8,0,7], 2))


# **Challenge 3**

# The simple substitution cipher basically consists of substituting every plaintext character for a different ciphertext character. The following is an example of one possible cipher from http://practicalcryptography.com/ciphers/simple-substitution-cipher/:
# 
# * Plain alphabet : abcdefghijklmnopqrstuvwxyz
# * Cipher alphabet: phqgiumeaylnofdxjkrcvstzwb

# In[9]:

def cipher(text, cipher_alphabet, option='encipher'):
    '''
    It has been assumed the option argument is always 'decipher' or 'encipher' 
    That is because the program uses 'decipher' if any argument different than 'encipher' is passed 
    '''
    try:
        return ''.join([cipher_alphabet[letter.lower()] for letter in list(text)])         if option == 'encipher' else         ''.join([key for letter in list(text) for key, value in cipher_alphabet.items() if letter.lower() == value])
    except:
        return "Please enter valid input (only a-z, A-Z and spaces allowed)"

# create cipher alphabet; note the additional space after the z / b
cipher_alphabet = dict(zip('abcdefghijklmnopqrstuvwxyz ', 'phqgiumeaylnofdxjkrcvstzwb '))

print(cipher('defend the east wall of the castle', cipher_alphabet))
print(cipher('giuifg cei iprc tpnn du cei qprcni', cipher_alphabet, 'decipher')) 


# **Challenge 4**  
# Implement a function that counts the number of isograms in a list of strings.
# 
# * An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# * Assume the empty string is an isogram and that the function should be case insensitive.

# In[10]:

def count_isograms(list_of_words):
    '''Count the number of strings without repeating characters in a list.
       A word is an isogram if all letters occur exactly 1 time.
    '''
    num_isograms = 0
    
    for word in list_of_words:
        # convert to upper() to account for case insensitivity
        if all(word.upper().count(letter.upper()) == 1 for letter in word):
            num_isograms += 1 
            
    return num_isograms


print(count_isograms(['conduct', 'letter', 'contract', 'hours', 'interview', 'Conduct']))


# **Challenge 5**  
# Write a function that returns a list of matching items. Items are defined by a tuple with a letter and a number and we consider item 1 to match item 2 if:
# 
# 1. Both their letters are vowels (aeiou), or both are consonants and,
# 2. The sum of their numbers is a multiple of 3

# In[11]:

def matching_pairs(data_list):
    pairs = []
    for index1, pair1 in enumerate(data_list): 
        for index2, pair2 in enumerate(data_list):
            
            if (((pair1[1] + pair2[1]) % 3 == 0) and # the sum of the number is a multiple of 3 
                index1 != index2 and # it must be different pairs (so not two times the same item)
                ((pair1[0] in 'aeiou' and pair2[0] in 'aeiou') or # only vowel-vowel combination
                (pair1[0] not in 'aeiou' and pair2[0] not in 'aeiou')) and # only consonant-consonant combination
                (index2, index1) not in pairs): # because (A,B) is the same as (B,A)
                    pairs.append((index1, index2))
                
    return pairs
 
print(matching_pairs([('a', 4), ('b', 5), ('c', 1), ('d', 3), ('e', 2), ('f', 6)]))

