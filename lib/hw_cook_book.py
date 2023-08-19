from pprint import pprint
cook_book = {}

with open("recipes.txt", "r") as file:
    lines = file.readlines()

index = 0

while index < len(lines):
    dish_name = lines[index].strip()  # Получаем название блюда
    index += 1

    num_of_ingredients = int(lines[index].strip())  # Получаем количество ингредиентов
    index += 1

    ingredients = []
    for i in range(num_of_ingredients):
        ingredient_data = lines[index].strip().split(" | ")
        ingredients.append({
            'ingredient_name': ingredient_data[0],
            'quantity': int(ingredient_data[1]),
            'measure': ingredient_data[2]
        })
        index += 1

    cook_book[dish_name] = ingredients

    index += 1  # Переходим к следующему рецепту
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return shop_list

shoplist = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(shoplist)
