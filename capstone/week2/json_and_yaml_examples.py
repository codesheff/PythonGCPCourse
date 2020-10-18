#!/usr/bin/env python3

import os, sys

this_script_path=(os.path.dirname(sys.argv[0]))
this_script_name=(os.path.basename(sys.argv[0]))
datadir=os.path.abspath(os.path.join(this_script_path,"data"))

### csv
#name,username,phone,department,role
#Sabrina Green,sgreen,802-867-5309,IT Infrastructure,System Administrator
#Eli Jones,ejones,684-3481127,IT Infrastructure,IT specialist


# or define that as a list of dictionaries
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": "802-867-5309",
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": "684-348-1127",
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]


## this is more flexible than csv, as you can add additional elements more easily
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]




#####################
# JSON 
import json

file=os.path.join(datadir,'people.json')
with open(file, 'w') as people_json:
    json.dump(people, people_json, indent=2)


####################
# YAML

import yaml

file=os.path.join(datadir,'people.yaml')
with open(file, 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)


# JSON is used frequently for transmitting data between web services, while YAML is used the most for storing configuration values.
# JSON has strings, which are enclosed in quotes.It also has numbers, which are not.
# JSON has objects, which are key-value pair structures like Python dictionaries.
#  And a key-value pair can contain another object as a value.
# JSON elements are always comma-delimited. 
#  JSON has arrays, which are equivalent to Python lists. Arrays can contain strings, numbers, objects, or other arrays.

# e.g. 
#[
#  "apple",
#  "banana",
#  12345,
#  67890,
#  {
#    "name": "Sabrina Green",
#    "username": "sgreen",
#    "phone": {
#      "office": "802-867-5309",
#      "cell": "802-867-5310"
#    },
#    "department": "IT Infrastructure",
#    "role": "Systems Administrator"
#  }
#]



import json

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

file=os.path.join(datadir,'people_singleline.json')
with open(file, 'w') as people_json:
    json.dump(people, people_json)

file=os.path.join(datadir,'people_multiline.json')
with open(file, 'w') as people_json:
    json.dump(people, people_json, indent=2)



#Another option is to use the dumps() method, which also serializes Python objects, but returns a string instead of writing directly to a file.
people_json = json.dumps(people)
print(people_json)


# The load() method does the inverse of the dump() method. It deserializes JSON from a file into basic Python objects. The loads() method also deserializes JSON into basic Python objects, but parses a string instead of a file.
file=os.path.join(datadir,'people_multiline.json')
with open(file, 'r') as people_json:
    people = json.load(people_json)
    print(type(people))
    print(people)