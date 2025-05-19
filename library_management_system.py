import streamlit as st
import datetime

# Initialize session state for books and ratings
if "library_books" not in st.session_state:
    st.session_state.library_books = []
if "ratings" not in st.session_state:
    st.session_state.ratings = {}

# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrow_date = None
        self.due_date = None
        self.rating = None  # Store book rating

# Library Management System
class Library:
    def __init__(self):
        self.books = st.session_state.library_books

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        st.success(f"📚 Book '{title}' by {author} added successfully!")

    def view_books(self, filter_by=None):
        if not self.books:
            st.warning("📭 No books in the library.")
        else:
            st.subheader("📖 Library Catalog")
            for book in self.books:
                if filter_by == "available" and book.is_borrowed:
                    continue
                if filter_by == "borrowed" and not book.is_borrowed:
                    continue

                status = "✅ Available" if not book.is_borrowed else f"❌ Borrowed (Due: {book.due_date})"
                rating = f"⭐ {st.session_state.ratings.get(book.title, 'No Ratings')}"
                st.write(f"**📕 {book.title}** by {book.author} - {status} | {rating}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                book.borrow_date = datetime.date.today()
                book.due_date = book.borrow_date + datetime.timedelta(days=7)  # 7-day due period
                st.success(f"🎉 You borrowed '{title}'. Due Date: {book.due_date} 📆")
                return
        st.error(f"❌ Book '{title}' is not available or does not exist.")

    def return_book(self, title, rating=None):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                book.due_date = None
                st.success(f"🔄 Book '{title}' has been returned. Thank you!")

                # Save rating
                if rating:
                    st.session_state.ratings[book.title] = rating
                    st.success(f"⭐ Thank you for rating '{title}' {rating} stars!")

                return
        st.error(f"❌ Book '{title}' is not in our system or already available.")

# Instantiate Library
library = Library()

# Streamlit UI
st.title("📚 Library Management System")

# Sidebar Navigation
menu = ["🏠 Dashboard", "📖 View Books", "➕ Add Book", "📕 Borrow Book", "🔄 Return Book"]
choice = st.sidebar.selectbox("🔽 Choose an option", menu)

if choice == "🏠 Dashboard":
    st.subheader("📊 Library Dashboard")
    total_books = len(st.session_state.library_books)
    available_books = sum(1 for book in st.session_state.library_books if not book.is_borrowed)
    borrowed_books = total_books - available_books

    st.metric("📚 Total Books", total_books)
    st.metric("✅ Available Books", available_books)
    st.metric("❌ Borrowed Books", borrowed_books)

    # Check for due books
    today = datetime.date.today()
    for book in st.session_state.library_books:
        if book.is_borrowed and book.due_date and book.due_date < today:
            st.error(f"🚨 Overdue: '{book.title}' was due on {book.due_date}!")

elif choice == "📖 View Books":
    filter_option = st.radio("📂 Filter books", ["All", "Available", "Borrowed"])
    filter_by = None if filter_option == "All" else filter_option.lower()
    library.view_books(filter_by)

elif choice == "➕ Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author Name")
    if st.button("Add Book"):
        if title and author:
            library.add_book(title, author)
        else:
            st.error("❌ Please enter both title and author.")

elif choice == "📕 Borrow Book":
    st.subheader("📕 Borrow a Book")
    title = st.text_input("Enter the Book Title to Borrow")
    if st.button("Borrow"):
        library.borrow_book(title)

elif choice == "🔄 Return Book":
    st.subheader("🔄 Return a Book")
    title = st.text_input("Enter the Book Title to Return")
    rating = st.slider("Rate the book (1-5 ⭐)", 1, 5, 3)
    if st.button("Return"):
        library.return_book(title, rating)
