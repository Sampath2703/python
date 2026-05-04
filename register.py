class Registration:
    def __init__(self, n, mn, email, pas, c_p):
        from db_connection import cur_obj

        queryCreatingTable = """
        create table if not exists Hotel(
        customer_id int primary key auto_increment,
        name varchar(50) not null unique,
        mobile_number varchar(15) not null unique,
        email varchar(50) not null unique,
        password varchar(16) not null
        )
        """
        cur_obj.execute(queryCreatingTable)
        print("Table Created")

        if pas == c_p:
            q = "insert into Hotel(name,mobile_number,email,password) values(%s,%s,%s,%s)"
            data=(n, mn, email, pas)
            cur_obj.execute(q,data)
            from db_connection import db_con_obj
            db_con_obj.commit()
            print("user registered successfully")

            if True:
                from login import Login
                email_Login=input("enter your email id :--  ")
                p_Login=input("enter login password here :-- ")
                Login(email_Login,p_Login)
        else:
            print("password and confirm password not matched")
            