from func_list import *

def calc(func_name, params):
    func_table = {
        "floor": floor,
        "nroot": nroot,
        "reverse": reverse,
        "validAnagram": validAnagram,
        "sort": sort
    }

    # return func_table[func_name]
    if func_name in func_table:
        return func_table[func_name](params)
    else:
        return "Unavailable function"
    



