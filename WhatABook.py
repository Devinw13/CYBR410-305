books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
]

store_locations = [
    {"id": 1, "name": "Downtown Bookstore", "location": "123 Main St"},
    {"id": 2, "name": "City Books", "location": "456 Oak St"},
]

wishlist = []
def show_menu():
    print("Menu:")
    print("1. View Books")
    print("2. View Store Locations")
    print("3. My Account")
    print("4. Exit Program")

def show_books():
    print("Available Books:")
    # Implement code to display available books

def show_locations():
    print("Store Locations:")
    # Implement code to display store locations

def show_account_menu():
    print("Account Menu:")
    print("1. Wishlist")
    print("2. Add Book")
    print("3. Main Menu")

def show_wishlist():
    print("Your Wishlist:")
    # Implement code to display user's wishlist

def show_books_to_add():
    print("Books Available to Add:")
    # Implement code to display books available to add

def add_book_to_wishlist():
    print("Book added to your Wishlist!")
    # Implement code to add a book to the user's wishlist

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_books()
        elif choice == '2':
            show_locations()
        elif choice == '3':
            show_account_menu()
            account_choice = input("Enter your choice (1-3): ")

            if account_choice == '1':
                show_wishlist()
            elif account_choice == '2':
                show_books_to_add()
                book_id = input("Enter the Book ID to add to your Wishlist: ")
                add_book_to_wishlist()
            elif account_choice == '3':
                pass
            else:
                print("Invalid choice. Please try again.")
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
