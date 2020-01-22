
cook_book = {}

def get_shop_list_by_dishes(dishes, person_count):
    groceries = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            groceries[ingredient['ingredient_name']] = \
                {'measure': ingredient['measure'], \
                'quantity': ingredient['quantity'] * person_count}
    return groceries

def get_title(f):
    return f.readline().split('\n')[0]

def get_ingredients(f):
    ingredients = []
    nb_ingredients = int(f.readline())
    i = 0
    while i < nb_ingredients:
        ingredient_raw_line = f.readline().split('\n')[0].split(' | ')
        ingredient = {}
        ingredient['ingredient_name'] = ingredient_raw_line[0]
        ingredient['quantity'] = int(ingredient_raw_line[1])
        ingredient['measure'] = ingredient_raw_line[2]        
        ingredients.append(ingredient)
        i = i + 1
    return ingredients

with open("cook_book.txt", encoding = "utf8") as f:
    first_line = True
    recipes = []
    line = ""
    while line != "" or first_line == True:
        if first_line == True:
            first_line = False
            title = get_title(f)
            cook_book[title] = get_ingredients(f)
        elif line == '\n':
            title = get_title(f)
            cook_book[title] = get_ingredients(f)
        line = f.readline()   

    
print(cook_book)
groceries = get_shop_list_by_dishes(["Омлет", 'Утка по-пекински'], 20)
print(groceries)
