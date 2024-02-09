import requests
def get_recipe_steps(ingredients):
    # API endpoint for recipe search
    API_URL = "https://api.spoonacular.com/recipes/findByIngredients?"
    
    # API parameters
    params = {
        'ingredients': ','.join(ingredients),  
        'number': 4,  
        "apiKey": "de8a909c7fce4648a2589f4797f1c138"
    }
    
    # Make API call to fetch recipes
    response = requests.get(API_URL, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        recipes = response.json()  # Convert JSON response to Python dictionary
        
        for recipe in recipes:
            print("Recipe:", recipe['title'])
            recipe_id = recipe['id']
            API_URL = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey=de8a909c7fce4648a2589f4797f1c138"
            response = requests.get(API_URL)
            
            if response.status_code == 200:
                instructions = response.json()  # Convert JSON response to Python dictionary
                if instructions:
                    steps = instructions[0]['steps']
                    for step in steps:
                        print("Step", step['number'], ":", step['step'])
                    print("\n")
                else:
                    print("No instructions found for the recipe.")
            else:
                print("Failed to fetch recipe instructions. Status code:", response.status_code)
    else:
        print("Failed to fetch recipes. Status code:", response.status_code)

# Example usage:
detected_ingredients = ['apple', 'cheese']
get_recipe_steps(detected_ingredients)