import os
import random
import time


def make_commit(days: int):
    if days < 1:
        return os.system('git push')

    dates = f'{days} days ago'

    # Вероятность пропустить день (55%)
    if random.random() < 0.55:
        print(f'Пропуск дня: {dates}')
        return make_commit(days - 1)

    # Выбираем случайное количество коммитов от 2 до 11
    commits_per_day = random.randint(2, 11)

    for _ in range(commits_per_day):
        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')

        os.system('git add data.txt')
        os.system(f'git commit --date="{dates}" -m "Random Commit"')


    return make_commit(days - 1)


# Пример вызова функции
make_commit(365)
