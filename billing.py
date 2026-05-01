class Billing:

    def generate_bill(self, room_id, check_in, check_out):
        from db_connection import cur_obj

        cur_obj.execute("SELECT price FROM rooms WHERE room_id=%s", (room_id,))
        price = cur_obj.fetchone()

        if not price:
            print("Invalid room")
            return

        price = price[0]

        from datetime import datetime

        d1 = datetime.strptime(check_in, "%Y-%m-%d")
        d2 = datetime.strptime(check_out, "%Y-%m-%d")

        days = (d2 - d1).days

        if days <= 0:
            print("Invalid dates")
            return

        total = days * price

        print("\n------ BILL ------")
        print("Room ID:", room_id)
        print("Price per day:", price)
        print("Days stayed:", days)
        print("Total Amount:", total)
        print("------------------")
