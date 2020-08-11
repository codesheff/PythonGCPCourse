#!/usr/bin/env python3

import re

## Capturing Groups
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result.groups())
print(result[0])
print(result[1])


print("{} {}".format(result[2], result[1]))

def rearrange_name(name):
    pattern=r"^([\w \.-]*), ([\w \.-]*)$"
    #attern=r"^(\w*), (\w* ?\w*\.)$"
    #result = re.search(r"^(\w*), (\w* ?\w*\.)$", name)
    result = re.search(pattern, name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

## Are capture groups always 0 or more? ( why don't I need the '?' after the '.' ?)
print('rearrange_name function')
print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Kennedy, John F."))
print(rearrange_name("Hopper, Grace M."))


## Repetition Qualifiers
print('Repetition Qualifiers')

print(re.search(r"[a-zA-Z]{5}", "a ghost")) # search for 5 letters
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appears")) # search for 5 letters

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appears")) # search for 5 letters

## \b is word boundary
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appears")) # search for 5 letters exactly


## match 5-10 letters or numbers
print(re.findall(r"\w{5,10}", "a scary ghost appears.  I really like strawberries.")) # search for 5 letters exactly


## match 5 or more letters or numbers
print(re.findall(r"\w{5,}", "a scary ghost appears.  I really like strawberries.")) # search for 5 letters exactly


## match 0-5  letters or numbers
print(re.findall(r"\w{,5}", "a scary ghost appears.  I really like strawberries.")) # search for 5 letters exactly


def long_words(text):
    '''
    The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.
    '''
    pattern = r"\w{7,}"
    result = re.findall(pattern, text)
    return result

print('Long Words')
print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []


log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]" # '('  - capturing group. '\d' - digits
result = re.search(regex,log)
print(result[1])

result = re.search(regex,'A completely different string that also has numbers [34567]')
print(result[1])

#result = re.search(regex,'99 elephants in a [cage]')
#print(result[1]) # gives error as result is None


def extract_pid_orig(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex,log_line)
    if result is None:
        return ""
    return result[1]  # return the 1st capturing group

print(extract_pid_orig('99 elephants in a [cage]'))
print(extract_pid_orig('A completely different string that also has numbers [34567]'))


def extract_pid(log_line):
    '''
    Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.
    '''
    regex = r"\[(\d+)\].*(\b[A-Z]{1,}\b)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print('Extract PID')
print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
