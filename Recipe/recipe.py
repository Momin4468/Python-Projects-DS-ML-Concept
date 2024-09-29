
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Sample recipes data
recipes = {
    'veg curry': {
        'type': ['veg', 'non-diet'],
        'ingredients': ['vegetables', 'curry powder', 'coconut milk'],
        'process': 'Cook vegetables in a pan, add curry powder, pour in coconut milk, simmer for 20 mins.'
    },
    'chicken salad': {
        'type': ['non-veg', 'diet'],
        'ingredients': ['chicken breast', 'lettuce', 'tomato', 'cucumber', 'olive oil'],
        'process': 'Grill chicken, chop veggies, mix and dress with olive oil.'
    },
    'grilled cheese': {
        'type': ['veg', 'non-diet'],
        'ingredients': ['bread', 'cheese', 'butter'],
        'process': 'Butter the bread, place cheese between slices, grill until golden.'
    },
    'beef stew': {
        'type': ['non-veg', 'non-diet'],
        'ingredients': ['beef', 'potatoes', 'carrots', 'onions', 'beef broth'],
        'process': 'Brown beef, add vegetables and broth, simmer until tender.'
    },
    'quinoa salad': {
        'type': ['veg', 'diet'],
        'ingredients': ['quinoa', 'red bell pepper', 'feta cheese', 'spinach', 'lemon dressing'],
        'process': 'Cook quinoa, mix with chopped vegetables, toss with dressing.'
    },
    'fish tacos': {
        'type': ['non-veg', 'non-diet'],
        'ingredients': ['white fish', 'cabbage slaw', 'corn tortillas', 'avocado', 'lime'],
        'process': 'Grill fish, assemble tacos with slaw and avocado, serve with lime.'
    },
    'tofu stir-fry': {
        'type': ['veg', 'non-diet'],
        'ingredients': ['tofu', 'mixed vegetables', 'soy sauce', 'ginger', 'garlic'],
        'process': 'Stir-fry tofu and vegetables, add sauce and spices, cook until fragrant.'
    },
    'lentil soup': {
        'type': ['veg', 'diet'],
        'ingredients': ['lentils', 'carrots', 'celery', 'tomatoes', 'vegetable broth'],
        'process': 'Simmer lentils and vegetables in broth until cooked, season to taste.'
    },
    'chopspork ': {
        'type': ['non-veg', 'non-diet'],
        'ingredients': ['pork chops', 'apples', 'onions', 'apple cider vinegar', 'mustard'],
        'process': 'Sear pork chops, sauté apples and onions, deglaze with vinegar.'
    },
    'cauliflower pizza': {
        'type': ['veg', 'diet'],
        'ingredients': ['cauliflower crust', 'tomato sauce', 'mozzarella cheese', 'basil'],
        'process': 'Top crust with sauce and cheese, bake until melted, garnish with basil.'
    }
}

@app.route('/', methods=['GET', 'POST'])
def home():
    filtered_recipes = {}
    show_results = False
    if request.method == 'POST':
        recipe_type = request.form.getlist('type')
        ingredient_query = request.form.get('ingredient', '').lower()

        # Filter recipes based on user input
        filtered_recipes = {
            name: details for name, details in recipes.items()
            if any(t in details['type'] for t in recipe_type) and
            (ingredient_query in name.lower() or any(ingredient_query in ing.lower() for ing in details['ingredients']))
        }
        show_results = True
        
    return render_template_string(HOME_HTML, filtered_recipes=filtered_recipes, show_results=show_results)

# HTML template with placeholders for filtered recipes
HOME_HTML = '''
<!doctype html>
<html>
<head>
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f7f7f7;
    }
    .container {
        width: 90%;
        max-width: 500px;
        margin: auto;
    }
    form {
        background: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    label {
        display: block;
        margin: 5px 0;
    }
    input[type="text"] {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border-radius: 4px;
        border: 1px solid #ddd;
        box-sizing: border-box;
    }
    button {
        width: 100%;
        padding: 10px;
        border: none;
        border-radius: 4px;
        color: white;
        background-color: #007BFF;
        cursor: pointer;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        font-size: 16px;
        transition: background-color 0.2s, box-shadow 0.2s;
    }
    button:hover {
        background-color: #4CAF50;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .results {
        background: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .recipe {
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
        margin-bottom: 10px;
    }
    .recipe:last-child {
        border-bottom: none;
    }
    .recipe-title {
        font-size: 18px;
        color: #333;
    }
    .recipe-ingredients {
        color: #666;
        font-style: italic;
    }
    .recipe-process {
        margin-top: 5px;
    }
    /* Highlighted heading style */
    h1 {
        background-color: #eb9234;
        color: white;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
    }
</style>
</head>
<body>
    <div class="container">
        <form method="post">
            <h1>Create A Recipe With AI</h1>
            <label><input type="checkbox" name="type" value="veg"> Veg</label>
            <label><input type="checkbox" name="type" value="non-veg"> Non-Veg</label>
            <label><input type="checkbox" name="type" value="diet"> Diet</label>
            <label><input type="checkbox" name="type" value="non-diet"> Non-Diet</label>
            <label for="ingredient">Enter a Recipe name:</label>
            <input type="text" placeholder="Enter an ingredient" id="ingredient" name="ingredient" required>
            <button type="submit">Get Recipe</button>
        </form>
        {% if show_results %}
        <div class="results">
            {% for name, info in filtered_recipes.items() %}
            <div class="recipe">
                <div class="recipe-title">{{ name.title() }}</div>
                <div class="recipe-ingredients">Ingredients: {{ info['ingredients'] | join(', ') }}</div>
                <div class="recipe-process">Process: {{ info['process'] }}</div>
            </div>
            {% endfor %}
        </div>
        {% endif %}
    </div>
</body>
</html>
'''
if __name__ == '__main__':
    app.run(debug=True)
