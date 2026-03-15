# Write your solution here
def load_recipes(filename: str):
    recipes = {}
    current_name = None

    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            
            if line == "":
                current_name = None
            elif current_name == None:
                current_name = line
                recipes[current_name] = []
            else:
                recipes[current_name].append(line)

        for name, data in recipes.items():
            data[0] = int(data[0])
            
    return recipes

def search_by_name(filename: str, word: str):
    recipes = load_recipes(filename)
    recipe_names = []

    for name in recipes:
        if word in name.lower():
            recipe_names.append(name)

    return recipe_names

def search_by_time(filename: str, prep_time: int):
    recipes = load_recipes(filename)
    recipe_times = []

    for name, data in recipes.items():
        if data[0] <= prep_time:
            recipe_info = f"{name}, preparation time {data[0]} min"
            recipe_times.append(recipe_info)

    return recipe_times

def search_by_ingredient(filename: str, ingredient: str):
    recipes = load_recipes(filename)
    found_recipes = []

    for name, data in recipes.items():
        for item in data[1:]:
            if ingredient.lower() in item:
                recipe_info = f"{name}, preparation time {data[0]} min"
                found_recipes.append(recipe_info)
                break
    
    return found_recipes

if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "egg")

    for recipe in found_recipes:
        print(recipe)