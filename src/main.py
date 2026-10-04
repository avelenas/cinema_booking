from src.movies import show_movies, add_movie
from src.booking import book_ticket, show_bookings


def main():
    while True:
        print("1. Show movies")
        print("2. Add movie")
        print("3. Book ticket")
        print("4. Show bookings")
        print("0. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            show_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            book_ticket()
        elif choice == "4":
            show_bookings()
        elif choice == "0":
            break
        else:
            print("Incorrect Input")

if __name__ == "__main__":
    main()

