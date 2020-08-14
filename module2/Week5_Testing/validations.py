#!/usr/bin/env python3

def validate_user(username, minlen):
    '''
    does stuff
    '''
    ## asserts, gives "message" if fails
    ##  be aware, asserts can get removed by code optimisers!
    assert type(username) == str, "username must be a string"
    
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    
    return True

## Test it in the validations_test.py instead
#print(validate_user(123,2))
#print(validate_user(['hello'],2))
#validate_user(['hello'],1)
#print(validate_user('bob',10))
#print(validate_user('bob',0))
#print(validate_user('bob',2))