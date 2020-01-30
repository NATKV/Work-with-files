cook_book = {}

# Takes a list of dishes and number of people as paramter,
# returns a dictionary of ingredients 
def get_shop_list_by_dishes(dishes_name_list, person_count):
    groceries = {}
    for dish_name in dishes_name_list:
        #iterating on all the recipes
        
        list_of_ingredients_for_one_dish = cook_book[dish_name]
        for ingredient_in_recipe in list_of_ingredients_for_one_dish:
            #iterating on all ingredients in recipe
            
            #fetching ingredient name 
            ingredient_name = ingredient_in_recipe['ingredient_name']
            
            quantity_of_current_ingredient = 0
            #checks if the ingredient is already in shop list
            if ingredient_name in groceries: 
                current_ingredient_in_groceries = groceries[ingredient_name]
                quantity_of_current_ingredient = current_ingredient_in_groceries['quantity']            
            
            #fetching the ingredient quantity from the recipe
            quantity_of_ingredient_in_recipe = ingredient_in_recipe['quantity']
            #adding ingredient quantity from recipe to the shop list
            quantity_of_current_ingredient += (quantity_of_ingredient_in_recipe * person_count) 
            #setting the ingredient count in the shop list
            groceries[ingredient_name] = \
                {'measure': ingredient_in_recipe['measure'], \
                'quantity': quantity_of_current_ingredient}
    return groceries


# Reads a new line from a file removing the last '\n' of the line
def my_read_line(file):
    return file.readline().split('\n')[0]
    
# Simply reads one line, suppositely the name of the recipe
def get_title(file):
    return my_read_line(file)

# Reads a number of ingredients, then formats ingredients in an list, and return them
def get_ingredients(file):
    ingredients = []
    nb_ingredients = int(file.readline())
    i = 0
    while i < nb_ingredients:
        ingredient_caracteristics_list = my_read_line(file).split(' | ')
        ingredient = {}
        ingredient['ingredient_name'] = ingredient_caracteristics_list[0]
        ingredient['quantity'] = int(ingredient_caracteristics_list[1])
        ingredient['measure'] = ingredient_caracteristics_list[2]        
        ingredients.append(ingredient)
        i = i + 1
    return ingredients

def make_cook_book():
    with open("cook_book.txt", encoding = "utf8") as file:
        first_line = True
        line = ""
        while line != "" or first_line == True:
            if first_line == True:
                first_line = False
            title = get_title(file)
            cook_book[title] = get_ingredients(file)
            line = file.readline() #skip empty line



def print_cook_book():
    for key in cook_book.keys():
        print(key)
        print("[")
        for ingredient in cook_book[key]:
            print(ingredient, ",")
        print("]")

def print_groceries(groceries_dic):
    for key in groceries_dic:
        print(key, ":", groceries_dic[key], ",")
 



def main():
    make_cook_book() 
    print_cook_book()

    groceries = get_shop_list_by_dishes(["Омлет", 'Фахитос'], 3)
    print_groceries(groceries)


         
main()
