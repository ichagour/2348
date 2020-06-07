import math
# part 1
lemonJuice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agaveNectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print("\nLemonade ingredients - yields {0:.2f}".format(servings)+" servings")
print("{:.2f}".format(lemonJuice) + " cup(s) lemon juice")
print("{:.2f}".format(water) + " cup(s) water")
print("{:.2f}".format(agaveNectar) + " cup(s) agave nectar\n")
# part 2
newServing = float(input('How many servings would you like to make?\n'))
number = newServing/servings
num_lemon_juice = number * lemonJuice
num_water = number * water
num_agar_nectar = number * agaveNectar
print("\nLemonade ingredients - yields {0:.2f}".format(newServing)+" servings")
print("{:.2f}".format(num_lemon_juice) + " cup(s) lemon juice")
print("{:.2f}".format(num_water) + " cup(s) water")
print("{:.2f}".format(num_agar_nectar) + " cup(s) agave nectar")
# part 3
lemonJuice_gallon = num_lemon_juice/16
water_gallon = num_water/16
agaveNectar_gallon = num_agar_nectar/16
print("\nLemonade ingredients - yields {0:.2f}".format(newServing),"servings")
print("{:.2f}".format(lemonJuice_gallon) + " gallon(s) lemon juice")
print("{:.2f}".format(water_gallon) + " gallon(s) water")
print("{:.2f}".format(agaveNectar_gallon) + " gallon(s) agave nectar")
