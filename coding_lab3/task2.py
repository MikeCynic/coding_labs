# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Провеьте работу функции с разделителем отличным от запятой


def find_common_participants(participant_group_1, participant_group_2, divider=','):
    common_participant_list = []
    participant_group_1 = participant_group_1.split(divider)
    participant_group_2 = participant_group_2.split(divider)
    for participant in participant_group_1:
        if participant in participant_group_2:
            common_participant_list.append(participant)
    return sorted(common_participant_list)
