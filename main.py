from library.library_manager import LibraryManager  # Correct import

if __name__ == "__main__":
    library = LibraryManager()

    # Read number of books
    n = int(input().strip())

    # Add books
    for _ in range(n):
        book_input = input().strip()
        parts = book_input.split(" ", 1)  # Split at the first space
        if len(parts) < 2:
            print("Invalid book format!")
            continue

        title, author = parts[0].strip(), parts[1].strip()
        library.add_book(title, author)

    # Read number of transactions
    m = int(input().strip())

    # Process transactions
    for _ in range(m):
        transaction = input().strip()
        if len(transaction) < 3:
            print("Invalid transaction format!")
            continue  # Ignore invalid transactions

        action, title = transaction[0], transaction[2:].strip()

        if action == 'B':
            library.borrow_book(title)
        elif action == 'R':
            library.return_book(title)
        else:
            print("Invalid transaction type!")

    # Display available books
    library.show_available_books()
