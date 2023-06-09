import sqlite3


def create_table():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    CREATE TABLE "Seat" (
        "seat_id"	TEXT,
        "taken"	INTEGER,
        "price"	REAL
    );
    """)
    connection.commit()
    connection.close()


def insert_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    INSERT INTO "Seat" ('seat_id', 'taken', 'price') VALUES ('A1', '0', '100'), ('A2', '1', '90'), ('A3', '0', '80')
    """)
    connection.commit()
    connection.close()


def select_all():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM 'Seat'
    """)
    result = cursor.fetchall()
    connection.close()
    return result


# select specific value
def select_specific_column():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id", "price" FROM 'Seat'
    """)
    result = cursor.fetchall()
    connection.close()
    return result


# select value with condition
def select_with_condition():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id", "price" FROM 'Seat' WHERE "price" > 80
    """)
    result = cursor.fetchall()
    connection.close()
    return result


# changing current values
def update_value():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    UPDATE "Seat" SET "taken"=1 WHERE "seat_id"="A3"
    """)
    connection.commit()
    connection.close()


# delete value
def delete_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    DELETE FROM "Seat" WHERE "seat_id"="A3"
    """)
    connection.commit()
    connection.close()

delete_record()