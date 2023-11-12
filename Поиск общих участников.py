# TODO Напишите функцию find_common_participants

def find_common_participants(group_1, group_2, separator = ','):

    participants_1 = group_1.split(separator)
    participants_2 = group_2.split(separator)

    common_participants = list(set(participants_1).intersection(participants_2))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(common_participants)


# TODO Провеьте работу функции с разделителем отличным от запятой
