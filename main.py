from inventory_manager import InventoryManager

def display_menu():
    print("\nBook Inventory Management")
    print("1. Add a new book")
    print("2. Remove a book by ISBN")
    print("3. Display current inventory")
    print("4. Exit")

def get_book_details():
    title = input("Enter title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    isbn = input("Enter ISBN: ")
    quantity = int(input("Enter quantity: "))
    return title, author, genre, isbn, quantity

def main():
    inventory = InventoryManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title, author, genre, isbn, quantity = get_book_details()
            inventory.add_book(title, author, genre, isbn, quantity)
            print("Book added successfully!")
        elif choice == '2':
            isbn = input("Enter ISBN of the book to remove: ")
            if inventory.remove_book(isbn):
                print("Book removed successfully!")
            else:
                print("Book not found!")
        elif choice == '3':
            print("Current Inventory:")
            inventory.display_inventory()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
