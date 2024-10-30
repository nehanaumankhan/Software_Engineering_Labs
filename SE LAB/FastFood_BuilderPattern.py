from abc import ABC, abstractmethod
class Item(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def packing(self):
        pass

    @abstractmethod
    def price(self):    
        pass

class Wrapper:
    def __str__(self):
        return "Wrapper"
    
class Bottle:
    def __str__(self):
        return "Bottle"
    
class Biryani(Item):
    def packing(self):
        return Wrapper()
    
    def price(self):
        pass

class ColdDrink(Item):
    def packing(self):
        return Bottle()
    
    def price(self):
        pass

class ChickenBiryani(Biryani):
    def price(self):
        return 350
    
    def name(self):
        return "Chicken Biryani"
    
class BeefBiryani(Biryani):
    def price(self):
        return 400
    
    def name(self):
        return "Beef Biryani"
    
class ColaNext(ColdDrink):
    def price(self):
        return 60
    
    def name(self):
        return "Cola Next"
    
class Fanta(ColdDrink):
    def price(self):
        return 60
    
    def name(self):
        return "Fanta"
    
class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def get_cost(self):
        return sum(item.price() * quantity for item, quantity in self. items)
    
    def show_items(self):
        for item, quantity in self.items:
            print(f"Item: {item.name()}, Packing: {item.packing()}, Price: {quantity * item.price()}")

class MealBuilder:
    def prepare_meal(self, meal_type, quantity):
        meal = Meal()
        if meal_type == "Chicken":
            meal.add_item(ChickenBiryani(), quantity)
        elif meal_type == "Beef":
            meal.add_item(BeefBiryani(), quantity)
        return meal

class DrinkBuilder:
    def prepare_drink(self, drink_type, quantity):
        if drink_type == "Cola Next":
            return ColaNext(), quantity
        elif drink_type == "Fanta":
            return Fanta(), quantity
        return None, 0
    
if __name__ == "__main__":
    print("***** MY RESTAURANT MENU *****\n")
    
    print("***** MEALS *****")
    print("1. Beef Biryani - Rs.400")
    print("2. Chicken Biryani - Rs.350\n")
    
    print("***** DRINKS *****")
    print("3. Cola Next - Rs.60")
    print("4. Fanta - Rs.70\n")
    
    meal_choice = int(input("***** PLACE YOUR ORDER *****\nChoose your meal (Press 1 for Beef Biryani or 2 for Chicken Biryani): "))
    
    if meal_choice == 1:
        quantity = int(input("How many Beef Biryani do you want? "))
        meal_builder = MealBuilder()
        meal = meal_builder.prepare_meal("Beef", quantity)
    elif meal_choice == 2:
        quantity = int(input("How many Chicken Biryani do you want? "))
        meal_builder = MealBuilder()
        meal = meal_builder.prepare_meal("Chicken", quantity)
    else:
        print("Invalid meal choice.")
        exit(1)
    
    drink_choice = int(input("Do you want some drinks? (Press 3 for Cola Next and 4 for Fanta): "))
    if drink_choice in [3, 4]:
        drink_quantity = int(input(f"How many {('Cola Next' if drink_choice == 3 else 'Fanta')} do you want? "))
        drink_builder = DrinkBuilder()
        drink, drink_quantity = drink_builder.prepare_drink("Cola Next" if drink_choice == 3 else "Fanta", drink_quantity)
        if drink:
            meal.add_item(drink, drink_quantity)

    print("\nThanks for placing your order.\n")
    print("***** YOUR ORDER SUMMARY *****\n")

    meal.show_items()
    
    total_cost = meal.get_cost()
    print("\nTotal Bill = Rs.", total_cost)
