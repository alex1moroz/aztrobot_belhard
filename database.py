import psycopg2
from decouple import config

host = config('HOST',default='')
database = config('DATABASE',default='')
user = config('USER',default='')
password = config('PASSWORD',default='')


conn = psycopg2.connect(host=host, dbname=database,
                        user=user, password=password)

cur = conn.cursor()


def set_user(user_id, username, first_name, last_name):
    cur.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    data = cur.fetchone()
    if data is None:
        cur.execute(f"INSERT INTO users (user_id, username, first_name, last_name) "
                    f"VALUES ('{user_id}', '{username}', '{first_name}', '{last_name}');")
        conn.commit()