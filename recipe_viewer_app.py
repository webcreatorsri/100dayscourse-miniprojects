import streamlit as st

# Function to Load Recipes from Uploaded Files
def load_recipes(uploaded_files):
    recipes = {}
    for uploaded_file in uploaded_files:
        content = uploaded_file.read().decode("utf-8")
        recipe_entries = content.strip().split("\n\n")  # Split recipes by double newlines

        for recipe in recipe_entries:
            lines = recipe.strip().split("\n")
            if len(lines) >= 3:
                name = lines[0].strip()
                ingredients = lines[1].replace("Ingredients: ", "").strip()
                instructions = lines[2].replace("Instructions: ", "").strip()
                recipes[name] = {"ingredients": ingredients, "instructions": instructions}
    
    return recipes

# Streamlit UI
st.title("📖 Recipe Viewer App")

# File Uploader (Allows multiple files)
uploaded_files = st.file_uploader("Upload Recipe Files (.txt)", type=["txt"], accept_multiple_files=True)

if uploaded_files:
    recipes = load_recipes(uploaded_files)
    
    if recipes:
        # Display Recipe Names in Sidebar
        st.sidebar.header("📜 Recipe List")
        recipe_name = st.sidebar.radio("Select a Recipe", list(recipes.keys()))

        # Display Selected Recipe
        if recipe_name:
            st.subheader(f"🍽️ {recipe_name}")
            st.write("### 🥕 Ingredients")
            st.write(recipes[recipe_name]["ingredients"])

            st.write("### 📝 Instructions")
            st.write(recipes[recipe_name]["instructions"])
    else:
        st.warning("No valid recipes found in the uploaded files.")
else:
    st.info("Please upload recipe files to view them.")
