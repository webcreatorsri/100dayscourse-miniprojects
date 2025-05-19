import streamlit as st

def initialize_session():
    if "user_ingredients" not in st.session_state:
        st.session_state.user_ingredients = set()

def main():
    initialize_session()
    
    st.title("🍽️ Recipe Ingredient Checker")
    st.subheader("Find recipes based on the ingredients you have!")
    
    # Define recipes with their required ingredients
    recipes = {
        "Pancakes": {"flour", "milk", "eggs"},
        "Cookies": {"flour", "butter", "sugar"},
        "Omelette": {"eggs", "butter"},
        "Tomato Soup": {"tomato", "salt", "water"},
        "Fruit Salad": {"banana", "apple", "orange"},
        "Grilled Cheese": {"bread", "butter", "cheese"},
        "Spaghetti": {"pasta", "tomato", "salt", "olive oil"},
        "Vegetable Stir-Fry": {"carrot", "broccoli", "soy sauce", "garlic"},
        "Smoothie": {"banana", "milk", "honey"},
        "Fried Rice": {"rice", "egg", "soy sauce", "peas", "carrot"},
        "Mashed Potatoes": {"potato", "butter", "milk", "salt"},
        "Guacamole": {"avocado", "lime", "salt", "tomato"},
        "Scrambled Eggs": {"eggs", "butter", "milk"},
        "French Toast": {"bread", "eggs", "milk", "sugar"},
        "Chili": {"beans", "tomato", "onion", "garlic", "chili powder"}
    }
    
    # User input for available ingredients
    user_input = st.text_area("Enter the ingredients you have (separated by commas):")
    if st.button("Check Ingredients"):
        st.session_state.user_ingredients = set(map(str.strip, user_input.lower().split(",")))
    
    # Compare ingredients
    all_recipe_ingredients = set().union(*recipes.values())
    missing_ingredients = all_recipe_ingredients - st.session_state.user_ingredients
    extra_ingredients = st.session_state.user_ingredients - all_recipe_ingredients
    
    # Display results
    st.subheader("🔍 Ingredient Check Results")
    if missing_ingredients:
        st.warning(f"You're missing: {', '.join(missing_ingredients)}")
    else:
        st.success("✅ You have all the ingredients needed!")
    
    if extra_ingredients:
        st.info(f"You have extra ingredients: {', '.join(extra_ingredients)}")
    
    # Suggested recipes based on available ingredients
    st.subheader("📌 Suggested Recipes")
    suggested_recipes = [name for name, ingredients in recipes.items() if ingredients.issubset(st.session_state.user_ingredients)]
    
    if suggested_recipes:
        st.success("✅ You can make these recipes:")
        for recipe in suggested_recipes:
            st.write(f"🍽️ {recipe}")
    else:
        possible_recipes = [(name, ingredients - st.session_state.user_ingredients) for name, ingredients in recipes.items() if len(ingredients - st.session_state.user_ingredients) <= 2]
        
        if possible_recipes:
            st.warning("You can try these recipes with a few missing ingredients:")
            for recipe, missing in possible_recipes:
                st.write(f"🍽️ {recipe} (Missing: {', '.join(missing)})")
        else:
            st.error("Not enough ingredients to suggest a recipe. Try adding more!")
    
if __name__ == "__main__":
    main()
