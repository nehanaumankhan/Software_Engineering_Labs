from abc import ABC, abstractmethod

class Item(ABC):
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
        return 200

    def name(self):
        return "Chicken Biryani"

class BeefBiryani(Biryani):
    def price(self):
        return 300

    def name(self):
        return "Beef Biryani"

class ColaNext(ColdDrink):
    def price(self):
        return 60

    def name(self):
        return "ColaNext"

class Tea(ColdDrink):
    def price(self):
        return 30

    def name(self):
        return "Tea"

class MealBuilder:
    def __init__(self):
        self.biryani_menu = {
            1: ChickenBiryani,
            2: BeefBiryani,
        }
        self.drink_menu = {
            1: ColaNext,
            2: Tea,
        }

    def show_menu(self):
        print("MENU")
        print("BIRYANI:")
        print("1. Chicken Biryani - Rs. 200")
        print("2. Beef Biryani - Rs. 300")
        
        print("DRINKS")
        print("1. ColaNext - Rs. 60")
        print("2. Tea - Rs. 30")

    def take_order(self):
        total_price = 0
        order_summary = []

        # Asking if the user wants Biryani
        want_biryani = input("\nDo you want to have Biryani? (yes/no): ").strip().lower()
        if want_biryani == 'yes':
            total_biryani = int(input("How many Biryani items do you want? "))
            total_chicken_biryani = 0
            total_beef_biryani = 0
            
            # Taking order for Chicken Biryani
            if total_biryani > 0:
                total_chicken_biryani = int(input(f"How many Chicken Biryani would you like? (Max {total_biryani}): "))
                total_biryani -= total_chicken_biryani
            
            # Taking order for Beef Biryani if there's still room
            if total_biryani > 0:
                total_beef_biryani = int(input(f"How many Beef Biryani would you like? (Max {total_biryani}): "))
                total_biryani -= total_beef_biryani

            # Calculating total for Biryani
            if total_chicken_biryani > 0:
                biryani = ChickenBiryani()
                item_total = biryani.price() * total_chicken_biryani
                order_summary.append(f"{biryani.name()} x {total_chicken_biryani} - Rs.{item_total}")
                total_price += item_total
            
            if total_beef_biryani > 0:
                biryani = BeefBiryani()
                item_total = biryani.price() * total_beef_biryani
                order_summary.append(f"{biryani.name()} x {total_beef_biryani} - Rs.{item_total}")
                total_price += item_total

        # Asking for Drinks
        want_drink = input("\nDo you want a Drink? (yes/no): ").strip().lower()
        if want_drink == 'yes':
            total_drink = int(input("How many Drink items do you want? "))
            total_cola_next = 0
            total_tea = 0
            
            # Taking order for Cola Next
            if total_drink > 0:
                total_cola_next = int(input(f"How many ColaNext would you like? (Max {total_drink}): "))
                total_drink -= total_cola_next
            
            # Taking order for Tea if there's still room
            if total_drink > 0:
                total_tea = int(input(f"How many Tea would you like? (Max {total_drink}): "))
                total_drink -= total_tea

            # Calculating total for Drinks
            if total_cola_next > 0:
                drink = ColaNext()
                item_total = drink.price() * total_cola_next
                order_summary.append(f"{drink.name()} x {total_cola_next} - Rs.{item_total}")
                total_price += item_total
            
            if total_tea > 0:
                drink = Tea()
                item_total = drink.price() * total_tea
                order_summary.append(f"{drink.name()} x {total_tea} - Rs.{item_total}")
                total_price += item_total
        
        # Print the order summary
        print("\nYOUR ORDER SUMMARY:")
        for item in order_summary:
            print(f"- {item}")
        print(f"\nTOTAL BILL - Rs.{total_price}")

# Driver Code
if __name__ == "__main__":
    meal_builder = MealBuilder()
    meal_builder.show_menu()
    meal_builder.take_order()
