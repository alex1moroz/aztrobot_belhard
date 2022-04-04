import psycopg2
import creds

conn = psycopg2.connect(host=creds.host, dbname=creds.database,
                        user=creds.user, password=creds.password)

cur = conn.cursor()


# cur.execute(f"CREATE TABLE users (id SERIAL PRIMARY KEY, user_id text, username text, "
#             f"first_name text, last_name text, sign text, day text);")
# conn.commit()


# id
# user_id
# username
# first_name
# last_name
# sign
# day

def set_user(user_id, username, first_name, last_name):
    cur.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    data = cur.fetchone()
    if data is None:
        cur.execute(f"INSERT INTO users (user_id, username, first_name, last_name) "
                    f"VALUES ('{user_id}', '{username}', '{first_name}', '{last_name}');")
        conn.commit()