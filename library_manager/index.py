
# Empty dictionary to store books
library = {}


# Function to add a book to the library
def AddBook():
    
    # Add a book to the library.
    book_title = input("Enter Book Title: ").strip()
    author = input("Enter Author: ").strip()
    genre = input("Enter Genre: ").strip()
    year = input("Enter Year Published: ").strip()
    
    
    if(book_title and author and genre and year.isdigit()):
        library[book_title] = {
            "Author": author,
            "Genre": genre,
            "Year": int(year)
        }
        
        print(f"'{book_title}' added to your library")
    else:
        print("Please enter valid details")


# Function to Display All Books
def display_books():
    # Display all books in the library.
    if library:
        print("Your Library Collection:")
        for title, details in library.items():
            print(f"{title} by {details['Author']} ({details['Year']}) - {details['Genre']}")
    else:
        print("No books added yet")
          

# Function to Remove a book from the library
def remove_book():
    # Remove a book from the library
    book_title = input("Enter the book title to remove: ").strip()
    if book_title in library:
        del library[book_title]
        print(f"'{book_title}' has been removed")
    else:
        print("Book not found in the library")
        
    
# Function to Search for a book in the library
def search_book():
    # Search for a book in the library
    search_title = input("Enter book title to search: ").strip()
    if search_title in library:
        details = library[search_title]
        print(f"Found: {search_title} by {details['Author']} ({details['Year']}) - {details['Genre']}")
    else:
        print("Book not found")
        
# Function to Display Library Statistics
def display_statistics():
   
    # Show library statistics
    total_books = len(library)
    genres = {}
    authors = {}

    for details in library.values():
        genre = details["Genre"]
        author = details["Author"]
        
        genres[genre] = genres.get(genre, 0) + 1
        authors[author] = authors.get(author, 0) + 1

    print("Library Statistics:")
    print(f"Total Books: {total_books}")
    
    if total_books > 0:
        print(f"Most Popular Genre: {max(genres, key=genres.get)} ({max(genres.values())} books)")
        print(f" Most Popular Author: {max(authors, key=authors.get)} ({max(authors.values())} books)")
        


print("Personal Library Manager")
print("1. Add a Book")
print("2. Remove a Book")
print("3. Search for a Book")
print("4. Display All Books")
print("5. Display Statistics")
print("6. Exit")

while True:  
    choice = input("Choose an option (1-6): ").strip()
    
    if choice == "1":
        AddBook()
    
    elif choice == "2":
        print("Remove a Book")
        remove_book()
    
    elif choice == "3":
        print("Search for a Book")
        search_book()
    
    elif choice == "4":
        print("Display All Books")
        display_books()
    
    elif choice == "5":
        print("Display Statistics")
        display_statistics()
    
    elif choice == "6":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 6")
