#import Abstract class
from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self, name, dough, sauce, toppings=None):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings if toppings is not None else []

    def prepare(self):
        print("Preparing " + self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(" " + topping)

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self.name


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__("NY Style Sauce and Cheese Pizza", "Thin Crust Dough", "Marinara Sauce",
                         ["Grated Reggiano Cheese"])


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__("Chicago Style Deep Dish Cheese Pizza", "Extra Thick Crust Dough", "Plum Tomato Sauce",
                         ["Shredded Mozzarella Cheese"])

    def cut(self):
        print("Cutting the pizza into square slices")


class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__("NY Style Veggie Pizza", "Thin Crust Dough", "Marinara Sauce",
                         ["Grated Reggiano Cheese", "Garlic", "Onion", "Mushrooms", "Red Pepper"])


class NYStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__("NY Style Clam Pizza", "Thin Crust Dough", "Marinara Sauce",
                         ["Grated Reggiano Cheese", "Fresh Clams from Long Island Sound"])


class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("NY Style Pepperoni Pizza", "Thin Crust Dough", "Marinara Sauce",
                         ["Grated Reggiano Cheese", "Sliced Pepperoni", "Garlic", "Onion", "Mushrooms", "Red Pepper"])

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__("Chicago Deep Dish Veggie Pizza", "Extra Thick Crust Dough", "Plum Tomato Sauce",
                         ["Shredded Mozzarella Cheese", "Black Olives", "Spinach", "Eggplant"])

class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__("Chicago Style Clam Pizza", "Extra Thick Crust Dough", "Plum Tomato Sauce",
                         ["Shredded Mozzarella Cheese", "Frozen Clams from Chesapeake Bay"])

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("Chicago Style Pepperoni Pizza", "Extra Thick Crust Dough", "Plum Tomato Sauce",
                         ["Shredded Mozzarella Cheese", "Black Olives", "Spinach", "Eggplant"])