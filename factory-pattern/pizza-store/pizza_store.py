from abc import ABC, abstractmethod
from pizza import NYStyleCheesePizza, NYStyleVeggiePizza, NYStyleClamPizza, NYStylePepperoniPizza, \
    ChicagoStyleCheesePizza, ChicagoStyleVeggiePizza, ChicagoStyleClamPizza, ChicagoStylePepperoniPizza

class PizzaStore(ABC):
    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        elif pizza_type == "veggie":
            return NYStyleVeggiePizza()
        elif pizza_type == "clam":
            return NYStyleClamPizza()
        elif pizza_type == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            return None


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "veggie":
            return ChicagoStyleVeggiePizza()
        elif pizza_type == "clam":
            return ChicagoStyleClamPizza()
        elif pizza_type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            return None