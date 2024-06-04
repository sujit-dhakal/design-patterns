class Meal:
    def __init__(self):
        self.burger = None
        self.drink = None

class MealBuilder:
    def build_burger(self):
        pass
    def build_drink(self):
        pass

class VegMealBuilder(MealBuilder):
    def build_burger(self):
        return "veg burger"
    def build_drink(self):
        return "cocacola"

class Director:
    def construct(self,builder):
        meal = Meal()
        meal.burger = builder.build_burger()
        meal.drink = builder.build_drink()
        return meal

veg_builder = VegMealBuilder()
director = Director()
meal = director.construct(veg_builder)
print(f"{meal.burger}{meal.drink}")