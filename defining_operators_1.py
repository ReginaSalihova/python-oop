class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.carbohydrates

    def get_kcalories(self):
        return 4 * self.proteins + 9 * self.fats + 4 * self.carbohydrates

    def __add__(self, other):
        total_proteins = self.proteins + other.proteins
        total_fats = self.fats + other.fats
        total_carbohydrates = self.carbohydrates + other.carbohydrates

        return FoodInfo(total_proteins, total_fats, total_carbohydrates)


food1 = FoodInfo(1, 2, 3)
food2 = FoodInfo(10, 20, 30)

food3 = food1 + food2

print(food3.get_proteins(), food3.get_fats(),
      food3.get_carbohydrates(), food3.get_kcalories())