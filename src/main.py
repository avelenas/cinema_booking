from src.movies import show_movies, add_movie, search_movie, add_to_favourites, show_favourites
from src.booking import book_ticket, show_bookings, cancel_booking

def main():
    while True:
        print("1. View movies")
        print("2. Booking")
        print("3. Favourites")
        print("4. Show bookings")
        print("5. Cancel booking")
        print("6. Search movie")
        print("7. Add to favourites")
        print("8. Show favourites")
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
        elif choice == "5":
            cancel_booking()
        elif choice == "6":
            search_movie()
        elif choice == "7":
            add_to_favourites()
        elif choice == "8":
            show_favourites()
        elif choice == "0":
            break
        else: print("Incorrect Input")


if __name__ == "__main__":
    main()

