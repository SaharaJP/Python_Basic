def sort_all_class_list(all_class_list): #Сортирует список всех учеников по возрастанию
    for i_student in range(len(all_class_list)):
        for i_all_students in range(i_student, len(all_class_list)):
            if all_class_list[i_all_students] < all_class_list[i_student]:
                all_class_list[i_all_students], all_class_list[i_student] = all_class_list[i_student], all_class_list[i_all_students]
    return all_class_list


first_class_list = list(range(160, 177, 2))
second_class_list = list(range(162, 181, 3))
all_class_list = []

all_class_list.extend(first_class_list)
all_class_list.extend(second_class_list)

#all_class_list.sort()

print('Отсортированный список учеников:', sort_all_class_list(all_class_list))