# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой


def find_common_participants(p1, p2, d=','):
    p_list = []
    p1 = p1.split(d)
    p2 = p2.split(d)
    for p in p1:
        if p in p2:
            p_list.append(p)
    p_list=sorted(p_list)
    return p_list


