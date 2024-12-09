from random import *

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = randint(0,len(friends)-1)
chosen_one = friends[random_number]

print(f"{chosen_one} is going to buy the meal today!")