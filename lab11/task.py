import psycopg2


yourpassword = '3028789'

# Database connection
conn = psycopg2.connect(f"dbname=postgres user=postgres password={yourpassword}")

# Procedure to insert or update user
def insert_or_update_user(conn, first_name, last_name, phone):
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO phonebook (first_name, last_name, phone) 
            VALUES (%s, %s, %s)
            ON CONFLICT (first_name) 
            DO UPDATE SET phone = EXCLUDED.phone;
        """, (first_name, last_name, phone))
        conn.commit()
        print("User inserted or updated successfully")
    except psycopg2.Error as e:
        print("Error inserting or updating user:", e)

# Procedure to delete data from tables by username or phone
def delete_data(conn, pattern):
    try:
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM phonebook 
            WHERE first_name LIKE %s 
            OR last_name LIKE %s
            OR phone LIKE %s;
        """, (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
        conn.commit()
        print("Data deleted successfully")
    except psycopg2.Error as e:
        print("Error deleting data:", e)

# Function to search for records based on a pattern
def search_records(conn, pattern):
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM phonebook 
            WHERE first_name LIKE %s 
            OR last_name LIKE %s
            OR phone LIKE %s;
        """, (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("Search completed successfully")
    except psycopg2.Error as e:
        print("Error searching records:", e)


def main():


    insert_or_update_user(conn, "TTTT", "BBBB", "12345")


    search_records(conn, "Anuar")


    delete_data(conn, "Anuar")


    conn.close()
    print("Connection to the database closed")


if __name__ == "__main__":
    main()