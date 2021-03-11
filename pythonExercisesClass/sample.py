

class User: 
    def __init__(self, age, name):
        print ("I am initialization")

        self.age = age
        self.name = name

        self.ageInFuture = age + 1

    def print_age(self, message):
        print(message, "age: ", self.age, self.name)


user1 = User(30, "Arek")
user2 = User(24, "Mirek")

user1.print_age("sample text)

user2.print_age("second sample text")

print (user1.ageInFuture)
