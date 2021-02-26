from user import User
from rocket import Rocket, RocketBoard

rockets = [User() for __ in range(8)]

for rocket in rockets:
    print("Rakieta nr",rocket.id)

print("Następny id rakiety będzie równy:", User.nextId)
