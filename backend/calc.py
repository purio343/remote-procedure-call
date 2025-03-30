from func_list import *

def calc(func_name, params):
    # 関数の実行結果を辞書に格納するのではなく、関数をそのまま格納する。
    func_table = {
        "floor": floor,
        "nroot": nroot,
        "reverse": reverse,
        "validAnagram": validAnagram,
        "sort": sort
    }

    if func_name in func_table:
        return func_table[func_name](params)
    else:
        return "Unavailable function"
    



