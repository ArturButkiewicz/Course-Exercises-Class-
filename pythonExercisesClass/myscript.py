from user import User
from rocket import Rocket, RocketBoard

rockets = [User() for __ in range(8)]

for rocket in rockets:
    print("Rocket nr",rocket.id)

print("ID of next rocket will be:", User.nextId)
