my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work
friend_foods = my_foods
my_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(f"{food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"{food}")