import streamlit as st
import os

FILE_NAME = "myNotes.txt"

# Load existing notes
def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return file.readlines()
    return []

# Save notes
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        file.writelines(notes)

# Streamlit UI
st.title("📝 Note-Taking App")

# Sidebar Menu
menu = ["Add Note", "View Notes", "Search Note", "Edit Note", "Delete All Notes"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Note":
    st.subheader("Add a New Note")
    note = st.text_area("Enter your note:")
    category = st.text_input("Category (Optional)")
    if st.button("Save Note"):
        notes = load_notes()
        new_note = f"[{category}] {note}\n" if category else f"{note}\n"
        notes.append(new_note)
        save_notes(notes)
        st.success("Note added successfully!")

elif choice == "View Notes":
    st.subheader("📜 Your Notes")
    notes = load_notes()
    if notes:
        for i, note in enumerate(notes, 1):
            st.text(f"{i}. {note.strip()}")
    else:
        st.info("No notes available.")

elif choice == "Search Note":
    st.subheader("🔍 Search Notes")
    query = st.text_input("Enter keyword:")
    if st.button("Search"):
        notes = load_notes()
        results = [note for note in notes if query.lower() in note.lower()]
        if results:
            st.success("Found matching notes:")
            for note in results:
                st.text(note.strip())
        else:
            st.warning("No matching notes found.")

elif choice == "Edit Note":
    st.subheader("✏️ Edit a Note")
    notes = load_notes()
    if notes:
        note_index = st.number_input("Enter note number to edit:", min_value=1, max_value=len(notes), step=1) - 1
        new_note = st.text_area("Edit note:", value=notes[note_index].strip())
        if st.button("Update Note"):
            notes[note_index] = f"{new_note}\n"
            save_notes(notes)
            st.success("Note updated successfully!")
    else:
        st.info("No notes available to edit.")

elif choice == "Delete All Notes":
    st.subheader("🚨 Delete All Notes")
    if st.button("Delete Notes"):
        save_notes([])
        st.warning("All notes have been deleted!")

# Run the app using `streamlit run filename.py` in the terminal.
