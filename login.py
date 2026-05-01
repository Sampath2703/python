class Login:
    def __init__(self, email, cp):
        from db_connection import cur_obj
        fetchQuery = "select * from Hotel"
        cur_obj.execute(fetchQuery)
        usersData = cur_obj.fetchall()

        for i in usersData:
            if i[3] == email and i[4] == cp:
                print(f"login successful {i[0]}")
            else:
                print("Invalid Password")