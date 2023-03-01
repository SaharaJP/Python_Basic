import json


def main_func(a, b):

    for key, val in a.items():
        if key in diff_list and a[key] != b[key]:
            diff_dict[key] = val
        elif isinstance(val, dict):
            main_func(a[key], b[key])


diff_list = ["services", "staff", "datetime"]

with open('result.json', 'w') as result,\
        open('json_new.json', 'r') as new, \
        open('json_old.json', 'r') as old:
    new_j = json.load(new)
    old_j = json.load(old)
    diff_dict = dict()

    main_func(new_j, old_j)
    print(diff_dict)

    json.dump(diff_dict, result, indent=4)
