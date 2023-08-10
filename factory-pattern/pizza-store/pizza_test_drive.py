from pizza_store import NYPizzaStore, ChicagoPizzaStore

class PizzaTestDrive:
    @staticmethod
    def main():
        ny_store = NYPizzaStore()
        chicago_store = ChicagoPizzaStore()

        pizza = ny_store.order_pizza("cheese")
        print("Ethan ordered a " + pizza.get_name() + "\n")

        pizza = chicago_store.order_pizza("cheese")
        print("Joel ordered a " + pizza.get_name() + "\n")


if __name__ == '__main__':
    PizzaTestDrive.main()