#   Запит до штучного інтелекту (Gemini 3.1 Pro):

#	Напиши код мовою Python, який демонструє реалізацію поведінкового патерна Iterator. Використай сенсовний приклад з реального життя: систему управління музичним плеєром.
#	Реалізуй базові абстрактні класи Iterator та Aggregate. Створи клас Song для представлення пісні. Реалізуй Playlist як конкретний агрегат, що зберігає список пісень. Реалізуй PlaylistIterator як конкретний ітератор, який дозволяє послідовно перебирати пісні у плейлисті.
#	Напиши клієнтський код, який створює плейлист, додає туди кілька пісень, отримує ітератор і за допомогою циклу while виводить інформацію про кожну пісню на екран. 
#	Код має бути добре прокоментований українською мовою. Коментарі повинні пояснювати, яка частина патерна реалізується в конкретному місці.


from abc import ABC, abstractmethod
from typing import List, Optional

# --- Абстракції патерна ---

class Iterator(ABC):
    """
    ПАТЕРН: Абстрактний Ітератор
    Визначає інтерфейс для обходу елементів колекції.
    """
    @abstractmethod
    def has_next(self) -> bool:
        """Перевіряє, чи є ще елементи для обходу."""
        pass

    @abstractmethod
    def next(self):
        """Повертає наступний елемент колекції."""
        pass


class Aggregate(ABC):
    """
    ПАТЕРН: Абстрактний Агрегат
    Визначає інтерфейс для створення об'єкта-ітератора.
    """
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


# --- Сутності предметної області ---

class Song:
    """
    Клас, що представляє окремий елемент колекції (пісню).
    """
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def __str__(self) -> str:
        return f"{self.artist} - {self.title}"


# --- Конкретні реалізації патерна ---

class PlaylistIterator(Iterator):
    """
    ПАТЕРН: Конкретний Ітератор
    Реалізує алгоритм обходу конкретної колекції (плейлиста).
    Зберігає поточний стан обходу.
    """
    def __init__(self, playlist: 'Playlist'):
        # Зберігаємо посилання на агрегат, який будемо обходити
        self._playlist = playlist
        # Початковий стан ітератора
        self._current_index = 0

    def has_next(self) -> bool:
        # Перевіряємо, чи індекс не вийшов за межі списку пісень
        return self._current_index < len(self._playlist.get_songs())

    def next(self) -> Optional[Song]:
        # Повертаємо поточну пісню і зміщуємо індекс на один крок вперед
        if self.has_next():
            song = self._playlist.get_songs()[self._current_index]
            self._current_index += 1
            return song
        return None


class Playlist(Aggregate):
    """
    ПАТЕРН: Конкретний Агрегат
    Зберігає колекцію об'єктів та повертає відповідний ітератор.
    """
    def __init__(self):
        self._songs: List[Song] = []

    def add_song(self, song: Song) -> None:
        self._songs.append(song)

    def get_songs(self) -> List[Song]:
        """Допоміжний метод для доступу до списку з ітератора."""
        return self._songs

    def create_iterator(self) -> Iterator:
        """
        Реалізація фабричного методу для створення ітератора,
        пов'язаного з цим конкретним плейлистом.
        """
        return PlaylistIterator(self)


# --- Клієнтський код ---

if __name__ == "__main__":
    # 1. Створюємо конкретний агрегат (плейлист)
    my_playlist = Playlist()

    # 2. Наповнюємо агрегат даними (піснями)
    my_playlist.add_song(Song("Smells Like Teen Spirit", "Nirvana"))
    my_playlist.add_song(Song("Bohemian Rhapsody", "Queen"))
    my_playlist.add_song(Song("Hotel California", "Eagles"))

    # 3. Отримуємо ітератор через інтерфейс агрегату
    iterator = my_playlist.create_iterator()

    print("Початок відтворення плейлиста:\n")

    # 4. Використовуємо ітератор для обходу колекції
    # Клієнтський код не знає про внутрішню структуру списку плейлиста
    while iterator.has_next():
        current_song = iterator.next()
        print(f"Грає: {current_song}")

    print("\nПлейлист завершено.")