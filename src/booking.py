bookings = []

def book_ticket():
    title = input("Enter title: ")
    quantity = int(input("Enter quantity of tickets: "))
    booking = {"title": title, "quantity": quantity,}
    bookings.append(booking)
    print("Successfully booked")

def show_bookings():
    if not bookings:
        print("No bookings")
        return
    for booking in bookings:
        print(f"{booking['title']} - {booking['quantity']}")

def cancel_booking():
    title = input("Enter title: ")
    for booking in bookings:
        if booking['title'] == title:
            bookings.remove(booking)
            print("Successfully canceled")
            return
    print("Not found")

def apply_discount(price):
    return price * 0.9


