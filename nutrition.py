# ilham chagour 1597694

class FoodItem:

    def __init__(self, name, fat, carbohydrates, protein):
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

    def __init__(self, name = 'None', fat = 0.0, carbohydrates = 0.0, protein = 0.0):
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

    def enter_calories(self, servings_size):
        calories = ((self.fat * 9)) + (self.carbohydrates * 4) +(self.protein * 4) * servings_size
        return calories

    def print_food_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbohydrates))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":

    food_item1 = FoodItem()

    item_name = input()
    amount_fat = float(input())
    amount_carbohydrates = float(input())
    amount_protein = float(input())

    food_item2 = FoodItem(item_name,amount_fat,amount_carbs,amount_protein)

    servings_size = float(input())

    food_item1.print_food_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings_size,
    food_item1.enter_calories(servings_size)))

    print()

    food_item2.print_food_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings_size,
    food_item2.enter_calories(servings_size)))
