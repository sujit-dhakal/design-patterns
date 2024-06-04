class Coffee:
    def cost(self):
        return 5
class SimpleCoffee(Coffee):
    pass

class CoffeeDecorator(Coffee):
    def __init__(self,coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2


simple_coffee = SimpleCoffee()
milk_coffee = MilkDecorator(simple_coffee)
print(milk_coffee.cost())