import streamlit as st
import json
import os

# File to store tasks
TASK_FILE = "my_tasks.json"

# Ensure the file exists
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, "w") as file:
        json.dump([], file)

# Load tasks from JSON
def load_tasks():
    with open(TASK_FILE, "r") as file:
        return json.load(file)

# Save tasks to JSON
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

# Streamlit UI
st.title("✅ Mini To-Do App")

# Input to add a new task
task_name = st.text_input("Enter a task:")
if st.button("➕ Add Task") and task_name.strip():
    st.session_state.tasks.append({"task": task_name, "status": "Incomplete"})
    save_tasks(st.session_state.tasks)
    st.success(f'Task "{task_name}" added!')
    st.rerun()  # ✅ Corrected function

# Display tasks
st.subheader("📃 Your Tasks:")
if st.session_state.tasks:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([4, 2, 1])
        with col1:
            st.write(f"**{task['task']}** - {task['status']}")
        with col2:
            if st.button(f"✅ Mark as Complete", key=f"complete_{index}"):
                st.session_state.tasks[index]["status"] = "Complete"
                save_tasks(st.session_state.tasks)
                st.rerun()
        with col3:
            if st.button("❌", key=f"delete_{index}"):
                del st.session_state.tasks[index]
                save_tasks(st.session_state.tasks)
                st.rerun()
else:
    st.info("No tasks yet! Add one above. ✍️")

# Search functionality
st.subheader("🔍 Search Tasks:")
search_query = st.text_input("Enter keyword to search:")
if st.button("🔎 Search"):
    filtered_tasks = [task for task in st.session_state.tasks if search_query.lower() in task["task"].lower()]
    if filtered_tasks:
        st.write("### Search Results:")
        for task in filtered_tasks:
            st.write(f"- **{task['task']}** - {task['status']}")
    else:
        st.warning("No matching tasks found.")

st.write("📌 **Tip:** Tasks are saved automatically.")
