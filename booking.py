class Booking:
    def __init__(self):
        from db_connection import cur_obj
        queryBooking = """
        create table if not exists booking(
        booking_id int primary key auto_increment,
        customer_id int,
        room_id int,
        status VARCHAR(20)
        )
        """
        cur_obj.execute(queryBooking)

    def book_room(self,room_id,customer_id):
        from db_connection import cur_obj, db_con_obj
        cur_obj.execute("select status from rooms where room_id=%s", (room_id,))
        status = cur_obj.fetchone()
        from room import Room
        if status and status[0] == "available":

            cur_obj.execute("insert into booking(customer_id,room_id,status) VALUES(%s,%s,'booked')",
            (customer_id, room_id))

            cur_obj.execute(
            "UPDATE rooms SET status='occupied' WHERE room_id=%s",
            (room_id,))

            db_con_obj.commit()
            print("Room Booked")
        else:
            print("Room not available")
    
    def checkout(self, room_id, check_in, check_out):

        from db_connection import cur_obj, db_con_obj
        from billing import Billing

        bill = Billing()
        bill.generate_bill(room_id, check_in, check_out)

    
        cur_obj.execute(
            "UPDATE rooms SET status='available' WHERE room_id=%s",
            (room_id,)
        )

        db_con_obj.commit()
        print("Checked out successfully")