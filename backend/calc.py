from func_list import *

def calc_result(func_name, params, req_id):
    # 関数の実行結果を辞書に格納するのではなく、関数をそのまま格納する。
    func_table = {
        "floor": floor,
        "nroot": nroot,
        "reverse": reverse,
        "validAnagram": validAnagram,
        "sort": sort
    }

    if func_name in func_table:
        results = func_table[func_name](params)
        result_type = str(type(results))
        response = {"results": results, "result_type": result_type, "res_id": req_id}
        return response
    else:
        return "Unavailable function"
    



