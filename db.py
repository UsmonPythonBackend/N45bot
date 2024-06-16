import psycopg2 as psql

class Database:
    @staticmethod
    async def connect(query, query_type):
        db = psql.connect(
            database="n45_5_l9",
            user="postgres",
            password="sudo",
            host="localhost",
            port="5432"
        )


        cursor = db.cursor()
        data = ["insert", "delete"]
        cursor.execute(query)
        if query_type    in data:
            db.commit()
            if query_type == "insert":
                    return "inserted successfully"

        else:
            return cursor.fetchall()


    @staticmethod
    async def check_user_id(user_id: int):
        query = f"SELECT * FROM users_2 WHERE user_id = {user_id}"
        chek_user = await Database.connect(query, query_type='select'):
        if len(chek_user) == 1:
            return True
        return False