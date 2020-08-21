#!/usr/bin/env


# dictionary in 

#(name,info), count

#dict_in = {('mdouglas', 'INFO'): 2, ('noel', 'INFO'): 6, ('breee', 'ERROR'): 5, ('ac', 'ERROR'): 2, ('blossom', 'INFO'): 2, ('mcintosh', 'ERROR'): 3, ('jackowens', 'ERROR'): 4, ('mdouglas', 'ERROR'): 3, ('oren', 'ERROR'): 7, ('bpacheco', 'ERROR'): 2, ('flavia', 'ERROR'): 3, ('sri', 'ERROR'): 2, ('breee', 'INFO'): 1, ('nonummy', 'ERROR'): 2, ('nonummy', 'INFO'): 2, ('xlg', 'ERROR'): 3, ('oren', 'INFO'): 2, ('britanni', 'INFO'): 1, ('mcintosh', 'INFO'): 4, ('montanap', 'ERROR'): 4, ('britanni', 'ERROR'): 1, ('noel', 'ERROR'): 3, ('jackowens', 'INFO'): 2, ('blossom', 'ERROR'): 4, ('ac', 'INFO'): 2, ('kirknixon', 'INFO'): 2, ('kirknixon', 'ERROR'): 1, ('sri', 'INFO'): 2}



my_dict = {
    'bob' : { 'info': 1 , 'error' : 2}
    ,'fred' : { 'info': 1 , 'error' : 2}
}



##thoughts 1
user='bob2'
if 'bob2' not in my_dict:
    my_dict['bob2'] = {}

my_dict['bob2']['info'] = my_dict.get('bobs',{}).get('info',0)

## I think you'd need to create the empty dictionary for bob2 1st

my_list=[]
new_dict=[]
for key in my_dict:
    print(my_dict[key])
    

