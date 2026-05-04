class Room:
    def __init__(self):
        from db_connection import cur_obj

        query = """
        CREATE TABLE IF NOT EXISTS rooms(
        room_id INT PRIMARY KEY AUTO_INCREMENT,
        room_type VARCHAR(20),
        price INT,
        status VARCHAR(20) DEFAULT 'available'
        )
        """
        cur_obj.execute(query)

    def add_room(self, room_type, price):
        from db_connection import cur_obj, db_con_obj

        q = "INSERT INTO rooms(room_type,price) VALUES(%s,%s)"
        cur_obj.execute(q, (room_type, price))
        db_con_obj.commit()
        print("Room Added")

    def view_rooms(self):
        from db_connection import cur_obj

        cur_obj.execute("SELECT * FROM rooms")
        for i in cur_obj.fetchall():
            print(i)