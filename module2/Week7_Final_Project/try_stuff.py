#!/usr/bin/env


# dictionary in 

#(name,info), count

#dict_in = {('mdouglas', 'INFO'): 2, ('noel', 'INFO'): 6, ('breee', 'ERROR'): 5, ('ac', 'ERROR'): 2, ('blossom', 'INFO'): 2, ('mcintosh', 'ERROR'): 3, ('jackowens', 'ERROR'): 4, ('mdouglas', 'ERROR'): 3, ('oren', 'ERROR'): 7, ('bpacheco', 'ERROR'): 2, ('flavia', 'ERROR'): 3, ('sri', 'ERROR'): 2, ('breee', 'INFO'): 1, ('nonummy', 'ERROR'): 2, ('nonummy', 'INFO'): 2, ('xlg', 'ERROR'): 3, ('oren', 'INFO'): 2, ('britanni', 'INFO'): 1, ('mcintosh', 'INFO'): 4, ('montanap', 'ERROR'): 4, ('britanni', 'ERROR'): 1, ('noel', 'ERROR'): 3, ('jackowens', 'INFO'): 2, ('blossom', 'ERROR'): 4, ('ac', 'INFO'): 2, ('kirknixon', 'INFO'): 2, ('kirknixon', 'ERROR'): 1, ('sri', 'INFO'): 2}



per_user={
    'ac': {'ERROR': 2, 'INFO': 2, 'user': 'ac'}, 'ahmed.miller': {'ERROR': 4, 'INFO': 2, 'user': 'ahmed.miller'}, 'blossom': {'ERROR': 4, 'INFO': 2, 'user': 'blossom'}, 'bpacheco': {'ERROR': 2, 'user': 'bpacheco'}, 'breee': {'ERROR': 5, 'INFO': 1, 'user': 'breee'}, 'britanni': {'ERROR': 1, 'INFO': 1, 'user': 'britanni'}, 'enim.non': {'ERROR': 2, 'INFO': 2, 'user': 'enim.non'}, 'flavia': {'ERROR': 3, 'user': 'flavia'}, 'jackowens': {'ERROR': 4, 'INFO': 2, 'user': 'jackowens'}, 'kirknixon': {'ERROR': 1, 'INFO': 2, 'user': 'kirknixon'}, 'mai.hendrix': {'ERROR': 3, 'user': 'mai.hendrix'}, 'mcintosh': {'ERROR': 3, 'INFO': 4, 'user': 'mcintosh'}, 'mdouglas': {'ERROR': 3, 'INFO': 2, 'user': 'mdouglas'}, 'montanap': {'ERROR': 4, 'user': 'montanap'}
    }

per_user_list=[]
for item in per_user.items():
    per_user_list.append(item[1])


print(per_user)