import streamlit as st
import os
import datetime

# Journal file path
JOURNAL_FILE = "daily_journal.txt"

# Function to add a new journal entry
def add_entry(entry_text):
    if entry_text.strip():  # Ensure it's not empty
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        with open(JOURNAL_FILE, "a") as file:
            file.write(f"[{date}] {entry_text}\n")
        st.success("✅ Entry added successfully!")
        st.session_state["entry_text"] = ""  # Clear input field
        st.rerun()  # Refresh the UI
    else:
        st.warning("⚠️ Please write something before adding!")

# Function to view all journal entries
def view_entries():
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, "r") as file:
            content = file.readlines()
        if content:
            st.subheader("📖 Your Journal Entries:")
            unique_entries = list(set(content))  # Remove duplicate lines
            for line in unique_entries:
                st.write("📝", line.strip())
        else:
            st.info("No journal entries found. Start writing today! 😊")
    else:
        st.warning("No journal file found. Add an entry first!")

# Function to search journal entries
def search_entries(keyword):
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, "r") as file:
            content = file.readlines()
        
        results = [entry for entry in content if keyword.lower() in entry.lower()]
        if results:
            st.subheader("🔍 Search Results:")
            for result in results:
                st.write("✅", result.strip())
        else:
            st.warning("❌ No matching entries found.")
    else:
        st.warning("⚠️ No journal file found. Add an entry first!")

# Streamlit UI
st.title("📔 Daily Journal Logger")

# Ensure session state for entry input
if "entry_text" not in st.session_state:
    st.session_state["entry_text"] = ""

# Text area for writing a new journal entry
st.subheader("📝 Add a New Entry:")
entry_text = st.text_area("Write your thoughts here...", st.session_state["entry_text"])

if st.button("➕ Add Entry"):
    add_entry(entry_text)

# View Journal Entries
st.subheader("📚 View Journal Entries:")
if st.button("📖 Show All Entries"):
    view_entries()

# Search Feature
st.subheader("🔍 Search Journal Entries:")
search_query = st.text_input("Enter a keyword to search:")

if st.button("🔎 Search"):
    if search_query.strip():
        search_entries(search_query)
    else:
        st.warning("⚠️ Please enter a keyword to search.")

st.write("📌 **Tip:** Your journal entries are automatically saved with today's date.")
