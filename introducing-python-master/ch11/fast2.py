
places = ["McDonalds", "KFC", "Burger King", "Taco Bell",
          "Wendys", "Arbys", "Pizza Hut"]


def pick():
    import random
    return random.choice(places)


print(pick())
# This is a random fast food place.

