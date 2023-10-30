list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
len_ = len(list_players)
average = len_//2
team_1 = list_players[:average]
team_2 = list_players[average:]
print(team_1)
print(team_2)