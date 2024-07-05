import time

class cUrTube():

    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        if login in self.users.keys():
            user = self.users[login]
            password = user[0]
            age = user[1]
            if password == password:
                # print(f'Пользователь {login} вошел в систему')
                self.current_user = user
        else:
            print('Ошибка входа. Неверный логин или пароль')


    def register(self, nickname, password, age):
        global user
        user = User(nickname, password, age)
        if user.nickname in self.users.keys():
            print(f'Пользователь {user.nickname} уже существует')
        else:
            self.users[nickname] = password,age
            # print(f'Ваш аккаунт {nickname} успешно зарегистрирован. Добро пожаловать!')
            self.log_in(nickname, password)
            self.current_user = user




    def log_out(self):
        if self.current_user:
            print(f'Пользователь {self.current_user.nickname} вышел из системы')
            self.current_user = None
        else:
            print('В системе нет активных пользователей')

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
                # print(f'Видео {video.title} добавлено')


    def get_videos(self, word: str):
        return [video.title for video in self.videos if word.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if video.title == title:
                if self.current_user.nickname in self.users.keys():
                    age = self.current_user.age
                if video.adult_mode and age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)
                print('Конец видео')
                video.time_now = 0
                return
        # print('Видео не найдено')



class Video():

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __str__(self):
        return f'Ваш никнейм: {self.nickname}'

ur = cUrTube()


v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')