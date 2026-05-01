print("chooose one option below")
print("1. Register")
print("2. Login")
print("3.Add Room")
print("4.View Rooms")
print("5.Book Room")
print("6. Billing")
print("7. Checkout")

i=input("choose one from above features")

if  int(i) == 1:
    from register import Registration
    name_input=input("enter your name :-- ")
    mobile_no = input("Enter mobile number :--")
    email = input("Enter email number :--")
    p_input=input("enter password :-- ")
    c_p_input=input("enter your password again :-- ")
    Registration(name_input,mobile_no,email,p_input,c_p_input)
elif int(i)==2:
    from login import Login
    email = input("Enter Emaid id :--")
    p_input=input("enter password :-- ")
    Login(email,p_input)

elif int(i) == 3:
    from room import Room
    r_type = input("Room type: ")
    price = int(input("Price: "))
    room_obj = Room()
    room_obj.add_room(r_type, price)

elif int(i) == 4:
    from room import Room
    room_o = Room()
    room_o.view_rooms()

elif int(i) == 5:
    from booking import Booking
    cust_id = int(input("Customer ID: "))
    room_id = int(input("Room ID: "))
    booking_obj = Booking()
    booking_obj.book_room(cust_id, room_id)

elif i == 6:
    from booking import Booking
    b = Booking()

    room_id = int(input("Enter room id: "))
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")

    b.checkout(room_id, check_in, check_out)

elif int(i) == 7:
    from booking import Booking
    b = Booking()

    room_id = int(input("Room ID: "))
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")

    b.checkout(room_id, check_in, check_out)

