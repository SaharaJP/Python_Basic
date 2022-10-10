def text_dict():
    text_dict = {
        sym: text.count(sym)
        for sym in text
    }
    return text_dict

def original_hist_dict(text_dict):
    for sym in text_dict:
        print(sym, ':', text_dict[sym])

def invert_hist_dict(text_dict):
    for i in range(1, max(text_dict.values()) + 1):
        invert_text_dict = [sym
                            for sym in text_dict
                            if text_dict[sym] == i
                            ]
        print(i, ':', invert_text_dict)


text = input('Введите текст: ')

print('Оригинальный словарь частот:')
text_dict = text_dict()
original_hist_dict(text_dict)

print('\nИнвертированный словарь частот:')
invert_hist_dict(text_dict)