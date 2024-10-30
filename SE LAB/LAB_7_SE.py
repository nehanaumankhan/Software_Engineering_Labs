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

    @abstractmethod
    def price(self):
        pass

class ColdDrink(Item):
    def packing(self):
        return Bottle()

    @abstractmethod
    def price(self):
        pass

class ChickenBiryani(Biryani):
    def price(self):
        return 350

    def name(self):
        return "Chicken Biryani"

class VegetableRice(Biryani):
    def price(self):
        return 300

    def name(self):
        return "Vegetable Rice"

class ColaNext(ColdDrink):
    def price(self):
        return 60

    def name(self):
        return "Cola Next"

class Tea(ColdDrink):
    def price(self):
        return 60

    def name(self):
        return "Tea"

class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def get_cost(self):
        return sum(item.price() * quantity for item, quantity in self.items)

    def show_items(self):
        for item, quantity in self.items:
            print(f"Item: {item.name()}, Packing: {item.packing()}, Price: {item.price()} x {quantity} = {quantity * item.price()}")

class MealBuilder:
    def prepare_veg_meal(self, quantity):
        meal = Meal()
        meal.add_item(VegetableRice(), quantity)
        return meal

    def prepare_non_veg_meal(self, quantity):
        meal = Meal()
        meal.add_item(ChickenBiryani(), quantity)
        return meal

class DrinkBuilder:
    def prepare_drink(self, drink_type, quantity):
        if drink_type == 3:
            return ColaNext(), quantity
        elif drink_type == 4:
            return Tea(), quantity
        return None, 0

if __name__ == "__main__":
    print("***** MY RESTAURANT MENU *****\n")
    
    print("***** VEGETARIAN ITEMS *****")
    print("1. Vegetable Rice - Rs.300\n")
    
    print("***** NON-VEGETARIAN ITEMS *****")
    print("2. Chicken Biryani - Rs.350\n")
    
    print("***** DRINKS *****")
    print("3. Cola Next - Rs.60")
    print("4. Tea - Rs.60\n")
    
    meal_choice = int(input("***** PLACE YOUR ORDER *****\nDo you want VEG MEAL or NON-VEG MEAL? (Press 1 for Vegetable Rice and 2 for Chicken Biryani): "))
    
    if meal_choice == 1:
        quantity = int(input("How many Vegetable Rice do you want? "))
        meal_builder = MealBuilder()
        meal = meal_builder.prepare_veg_meal(quantity)
    elif meal_choice == 2:
        quantity = int(input("How many Chicken Biryani do you want? "))
        meal_builder = MealBuilder()
        meal = meal_builder.prepare_non_veg_meal(quantity)
    else:
        print("Invalid meal choice.")
        exit(1)
    
    drink_choice = int(input("Do you want some drinks? (Press 3 for Cola Next and 4 for Tea): "))
    if drink_choice in [3, 4]:
        drink_quantity = int(input(f"How many {('Cola Next' if drink_choice == 3 else 'Tea')} do you want? "))
        drink_builder = DrinkBuilder()
        drink, drink_quantity = drink_builder.prepare_drink(drink_choice, drink_quantity)
        if drink:
            meal.add_item(drink, drink_quantity)

    print("\nThanks for placing your order.\n")
    print("***** YOUR ORDER SUMMARY *****\n")

    if meal_choice == 1:
        print("***** VEG MEAL *****")
    elif meal_choice == 2:
        print("***** NON-VEG MEAL *****")
    
    meal.show_items()
    
    total_cost = meal.get_cost()
    print("\nTotal Bill = Rs.", total_cost)
