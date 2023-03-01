from typing import Dict
import json


def diff_func(new: Dict, old: Dict) -> None:
    """
    Функция, добавляющая в пустой словарь
    различающиеся в двух непустых словарях
    искомые параметры

    :param new: dict: новый словарь
    :param old: dict: старый словарь
    """

    for key, val in new.items():
        if key in diff_list and new[key] != old[key]:
            diff_dict[key] = val
        elif isinstance(val, dict):
            diff_func(new[key], old[key])


diff_list = ["services", "staff", "datetime"]

with open('result.json', 'w') as result,\
        open('json_new.json', 'r') as new, \
        open('json_old.json', 'r') as old:
    new_j = json.load(new)
    old_j = json.load(old)
    diff_dict = dict()

    diff_func(new_j, old_j)
    print(diff_dict)

    json.dump(diff_dict, result, indent=4)
