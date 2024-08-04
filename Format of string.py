team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование форматирования %

print("В команде Мастера кода участников: %d ! " % (team1_num))
print("Итого сегодня в командах участников: %(count)d и %(count2)d !" % {'count':team1_num, 'count2':team2_num})

# Использование форматирования .format()

print("Команда Волшебники данных решила задач: {} !".format(score2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))

# Использование f строк

print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {score1 + score2} задач, в среднем по {round((team1_time + team2_time) / (score1 + score2),1)} секунды на задачу!')

