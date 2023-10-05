import json

class CinemaException(Exception):
    def __init__(self,message):
        super().__init__(message)

class Movie:
    def __init__(self, title, age, genre,duration):
        if not isinstance(title, str):
            raise CinemaException("Title should be a string")
        if not isinstance(age, int) or age not in [0, 6, 12, 16, 18]:
            raise CinemaException("Invalid age category")
        if not isinstance(genre, str) or genre not in ["Drama", "Comedy", "Action", "Horror"]:
            raise CinemaException("Invalid genre")
        if not isinstance(duration, int) or duration <= 0:
            raise CinemaException("Invalid duration")
        self.title = title
        self.age = age
        self.genre = genre
        self.duration = duration

class Serial:
    def __init__(self, title, genre, seasons,age):
        if not isinstance(title, str):
          raise CinemaException("Title should be a string")
        if not isinstance(genre, str) or genre not in ["Drama", "Comedy", "Action", "Horror"]:
          raise CinemaException("Invalid genre")
        if not isinstance(seasons, int) or seasons <= 0:
          raise CinemaException("Invalid number of seasons")
        if not isinstance(age, int) or age not in [0, 6, 12, 16, 18]:
          raise CinemaException("Invalid age category")
        self.title = title
        self.genre = genre
        self.seasons = seasons
        self.age = age

class Cinema:
    def __init__(self):
        self.movies = []
        self.serials = []

    def import_data(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            self.movies = [Movie(m['title'], m['age'], m['genre'] ,m['duration'])   for m in data['movies']]
            self.serials = [Serial(s['title'], s['genre'], s['seasons'],s['age']) for s in data['serials']]

    def export_data(self, json_file):
        data = {
            'movies': [{'title': m.title, 'age': m.age, 'genre': m.genre, 'duration': m.duration} for m in self.movies],
            'serials': [{'title': s.title, 'genre': s.genre, 'seasons': s.seasons, 'age': s.age} for s in self.serials]
        }
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)

    def add_movie(self, title, age, genre, duration):
        self.movies.append(Movie(title, age, genre, duration))

    def add_serial(self, title, genre, seasons, age):
        self.serials.append(Serial(title, genre, seasons, age))

    def remove_movie(self, title):
        self.movies = [m for m in self.movies if m.title != title]

    def remove_serial(self, title):
        self.serials = [s for s in self.serials if s.title != title]


# Пример использования

cinema = Cinema()

# Импорт данных из JSON файла

try:
   cinema.import_data('data.json')
except CinemaException as e:
    print(f"Importing error: {str(e)}")
# Добавление фильма
#cinema.add_movie('The Shawshank Redemption', 18, "Drama",120)
#cinema.add_serial('Friends', "Comedy", 3,16)

# Удаление сериала
#cinema.remove_serial('Game of Thrones')
#duration
# Экспорт данных в JSON файл
#cinema.export_data('data.json')
try:
    # Добавление фильма
    cinema.add_movie('The Shawshank Redemption', 18, "Drama", 120)
    
    # Добавление сериала с некорректными атрибутами
    cinema.add_serial('Friends', "Sitcom", 3, 16)  # Некорректный жанр
    
except CinemaException as e:
    print(f"Error: {str(e)}")

# Удаление сериала
#cinema.remove_serial('Game of Thrones')
try:
    cinema.export_data('data.json')
except CinemaException as e:
    print(f"Export error: {str(e)}")
