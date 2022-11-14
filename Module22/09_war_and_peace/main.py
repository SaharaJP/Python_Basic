import collections
import zipfile

def unzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for file_name in zfile.namelist():
        zfile.extract(file_name)
    zfile.close()

def collect_stats(file_name):
    result = dict()

    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))

    text_file = open(file_name, 'r', encoding = 'utf-8')
    for line in text_file:
        for sym in line:
            if sym.isalpha():
                if sym not in result:
                    result[sym] = 0
                result[sym] += 1
    text_file.close()

    return result

def print_stats(stats):
    print('+{:-^19}+'.format('+'))
    print('|{: ^9}|{: ^9}|'.format('буква', 'частота'))
    print('+{:-^19}+'.format('+'))

    for char, count in stats.items():
        print('|{: ^9}|{: ^9}|'.format(char, count))

    print('+{:-^19}+'.format('+'))

def sort_by_frequency(stats_dict):
    sorted_values = sorted(stats_dict.values())
    sorted_dict = collections.OrderedDict()

    for value in sorted_values:
        for key in stats_dict.keys():
            if stats_dict[key] == value:
                sorted_dict[key] = stats_dict[key]

    return sorted_dict


file_name = 'voyna-i-mir.zip'
stats = collect_stats(file_name)
stats = sort_by_frequency(stats)
print_stats(stats)