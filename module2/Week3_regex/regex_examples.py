#!/usr/bin/env python3

# https://docs.python.org/3/howto/regex.html
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy

import re

# Always use r'string'  - rawstring
result=re.search(r'^.oo','Looking glass whoopsie!')
print(result)


result=re.search(r'^p.ng','Pangea', re.IGNORECASE)
print(result)


result=re.search(r'[a-z]way','The end of the highway')
print(result)

def check_punctuation (text):
    '''Check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.'''
    result = re.search(r"[,.:;?!]", text)
    return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False


print(re.search(r'[^a-zA-z]', "This is a sentence with spaces"))
print(re.search(r'[^a-zA-z ]', "This is a sentence with spaces"))


## re.search just gives 1st match
print(re.search(r'cat|dog', "I like cats and dogs."))

## re.findall  gives all matches
print(re.findall(r'cat|dog', "I like cats and dogs."))

# The '*' is 'greedy'  - it takes as many characters as possible
print(re.search(r'Py.*n', "Pygmallion"))

print(re.search(r'Py.*n', 'Python Programming'))
print(re.search(r'Py[a-z]*n', 'Python Programming'))

## *  - Zero or more
## +  - 1 or more
## ? -  Zero or 1 occurrence

print(re.search(r'o+l+', 'goldfish'))
print(re.search(r'o+l+', 'woolly'))
print(re.search(r'o+l+', 'boil'))


def repeating_letter_a(text):
    '''The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False'''
    result = re.search(r"[aA].*[aA]", text)
    return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True


print(re.search(r'p?each', 'To each their own'))
print(re.search(r'p?each', 'peach'))

## Escape characters '\'
print(re.search(r'.com', 'welcome to www.bbc.com'))
print(re.search(r'\.com', 'welcome to www.bbc.com'))

## \w  - any alphanumeric,  - letters, numbers and underscores
## \b  
## \s 
##   and some others
print(re.search(r'\w', 'welcome to www.bbc.com'))


def check_character_groups(text):
    '''check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters'''
    result = re.search(r"\w\s\w", text)
    return result != None
print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

def check_sentence(text):
    ''''check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.'''
    result = re.search(r'^[A-Z][a-z ]+[.?!]$', text)
    return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
print(check_sentence("A.")) # False
