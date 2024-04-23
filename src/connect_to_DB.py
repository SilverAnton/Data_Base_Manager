import psycopg2


class DBConnect:
    @staticmethod
    def connect(code):
        conn = {
            "host": "localhost",
            "database": "north",
            "user": "postgres",
            "password": "KrizopolZ0505"
        }
        with psycopg2.connect(**conn) as connect:
            with connect.cursor() as cursor:
                cursor.execute(code)



obj = DBConnect

obj.connect('CREATE TABLE new_one(number varchar, name varchar)')
