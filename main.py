class Restaurant:
    def __init__(self, name, id, address, location):
        self.name = name
        self.id = id
        self.address = address
        self.location = location
        self.menu=[]

class Food:
    def __init__(self, type, name, price, vegeterian, gluten_free, restaurant_id):
        self.type = type
        self.name = name
        self.price = price
        self.vegeterian = vegeterian
        self.gluten_free = gluten_free
        self.restaurant_id=restaurant_id

def galvena_programma():
    rest1 = Restaurant("Vairāk saules", 1, "Domina shopping", (50.1234, 49.123))
    food1 = Food("Starter", "Spring rolls", 4.00, True, True)
    food2 = Food("Salad", "Cezar", 8, False, True)
    food3 = Food("Main", "Burger", 12, True, False)

    rest1.menu.append(food1)
    rest1.menu.append(food2)
    rest1.menu.append(food3)

galvena_programma()

