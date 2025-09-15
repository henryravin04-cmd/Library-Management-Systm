class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available " if self.is_available else "Borrowed ❌"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"📚 Added: {title} by {author}")

    def view_books(self):
        if not self.books:
            print(" No books in library.")
        else:
            print("\n===== 📚 Library Books =====")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def borrow_book(self, index):
        if 0 <= index < len(self.books) and self.books[index].is_available:
            self.books[index].is_available = False
            print(f" You borrowed: {self.books[index].title}")
        else:
            print(" Book not available.")

    def return_book(self, index):
        if 0 <= index < len(self.books) and not self.books[index].is_available:
            self.books[index].is_available = True
            print(f"🔄 Returned: {self.books[index].title}")
        else:
            print("⚠️ Invalid return.")


def menu():
    library = Library()
    while True:
        print("\n===== 📘 Library Menu =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            library.view_books()
            idx = int(input("Enter book number to borrow: ")) - 1
            library.borrow_book(idx)

        elif choice == "4":
            library.view_books()
            idx = int(input("Enter book number to return: ")) - 1
            library.return_book(idx)

        elif choice == "5":
            print(" Exiting Library System.")
            break
        else:
            print(" Invalid choice.")


if __name__ == "__main__":
    menu()
