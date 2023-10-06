
import xml.etree.ElementTree as ET

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

    def import_data(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        self.movies = []
        self.serials = []

        for movie_elem in root.findall('movies/movie'):
            title = movie_elem.find('title').text
            age = int(movie_elem.find('age').text)
            genre = movie_elem.find('genre').text
            duration = int(movie_elem.find('duration').text)
            self.movies.append(Movie(title, age, genre, duration))

        for serial_elem in root.findall('serials/serial'):
            title = serial_elem.find('title').text
            genre = serial_elem.find('genre').text
            seasons = int(serial_elem.find('seasons').text)
            age = int(serial_elem.find('age').text)
            self.serials.append(Serial(title, genre, seasons, age))

    def export_data(self, xml_file):
        root = ET.Element("cinema")

        movies_elem = ET.SubElement(root, "movies")
        for movie in self.movies:
            movie_elem = ET.SubElement(movies_elem, "movie")
            ET.SubElement(movie_elem, "title").text = movie.title
            ET.SubElement(movie_elem, "age").text = str(movie.age)
            ET.SubElement(movie_elem, "genre").text = movie.genre
            ET.SubElement(movie_elem, "duration").text = str(movie.duration)

        serials_elem = ET.SubElement(root, "serials")
        for serial in self.serials:
            serial_elem = ET.SubElement(serials_elem, "serial")
            ET.SubElement(serial_elem, "title").text = serial.title
            ET.SubElement(serial_elem, "genre").text = serial.genre
            ET.SubElement(serial_elem, "seasons").text = str(serial.seasons)
            ET.SubElement(serial_elem, "age").text = str(serial.age)

        tree = ET.ElementTree(root)
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)
           # self.movies = [Movie(m['title'], m['age'], m['genre'] ,m['duration'])   for m in data['movies']]
          #  self.serials = [Serial(s['title'], s['genre'], s['seasons'],s['age']) for s in data['serials']]


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

#try:
#   cinema.import_data('data.xml')
#except CinemaException as e:
 #   print(f"Importing error: {str(e)}")
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
    cinema.add_serial('Friends', "C", 3, 16)  # Некорректный жанр
    
except CinemaException as e:
    print(f"Error: {str(e)}")

# Удаление сериала
#cinema.remove_serial('Game of Thrones')
try:
    cinema.export_data('data.xml')
except CinemaException as e:
    print(f"Export error: {str(e)}")