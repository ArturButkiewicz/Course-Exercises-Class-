"""
OBIEKTY - to pojemniki do przechowywania zmiennych i funkcji tematycznie ze
          sobą powiązanych do dalszego łatwiejszego ponownego użycia

Klasy   - foremki (szablony) do tworzenia egzemplarzy obiektów

Atrybut - cecha opisująca obiekt
Metoda - funkcja, która operuje na obiekcie

self - z ang. 'ja', 'sam osobiście', 'siebie' w innych językach: 'this'
__init__ - ustawienie wartości startowych wartości dla atrybutólw

"""



class User:  # z dużej litery klasy

    def __init__(self, age, name):
        print ("jestem inicjalizacją")

        self.age = age
        self.name = name

        self.ageInFuture = age + 1

    def print_age(self, message):
        print(message, "wiek: ", self.age, self.name)


user1 = User(30, "Arek")
user2 = User(24, "Mirek")

user1.print_age("dodatkowy tekst całkowicie inny")

user2.print_age("dodatkowy tekst")

print (user1.ageInFuture)
