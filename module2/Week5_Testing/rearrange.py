#!/usr/bin/env python3

import re


def rearrange_name(name):
    pattern=r"^([\w \.-]*), ([\w \.-]*)$"
    #attern=r"^(\w*), (\w* ?\w*\.)$"
    #result = re.search(r"^(\w*), (\w* ?\w*\.)$", name)
    result = re.search(pattern, name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])