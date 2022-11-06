import os

def cat_func(cur_path):
    for i_el in os.listdir(cur_path):
        path = os.path.join(cur_path, i_el)

        if os.path.isfile(path):
            answer['files'] += 1
            answer['cat_size'] += os.path.getsize(path)

        if os.path.isdir(path):
            answer['in_cat'] += 1
            res = cat_func(path)
            if res:
                return


answer = {'cat_size' : 0, 'in_cat' : 0, 'files' : 0}
cat_func(os.path.abspath(os.path.join('..', '..', 'Module14')))
answer['cat_size'] /= 1024

print(os.path.abspath(os.path.join('..', '..', 'Module14')))
print('Размер каталога (в Кб):', answer['cat_size'])
print('Количество подкталогов:', answer['in_cat'])
print('Количество файлов:', answer['files'])