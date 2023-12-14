import sqlite3

connection = sqlite3.connect("your_database.db")  # Replace "your_database.db" with your actual database file name

def get_table1_data():
    cursor = connection.cursor()
    rows = cursor.execute("SELECT types FROM table1")
    return [row[0] for row in rows]

def get_table2_data():
    cursor = connection.cursor()
    rows = cursor.execute("SELECT types, count FROM table2")
    return [{'types': row[0], 'count': row[1]} for row in rows]

def add_to_table1(item_type):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO table1 (types) VALUES ('{item_type}')")
    connection.commit()

def add_to_table2(item_type, item_count):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO table2 (types, count) VALUES ('{item_type}', {item_count})")
    connection.commit()

def update_table1(item_type, new_type):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE table1 SET types = '{new_type}' WHERE types = '{item_type}'")
    connection.commit()

def update_table2(item_type, new_count):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE table2 SET count = {new_count} WHERE types = '{item_type}'")
    connection.commit()

def delete_item(item_type):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM table1 WHERE types = '{item_type}'")
    cursor.execute(f"DELETE FROM table2 WHERE types = '{item_type}'")
    connection.commit()

# The rest of your functions (get_courses_and_students, add_course_and_student, update_course_and_student, delete_course_and_student, set_up_database, and tests) remain the same.

if __name__ == "__main__":
    test_set_up_database()
    test_get_table1_data()
    test_get_table2_data()
    test_add_to_table1()
    test_add_to_table2()
    test_update_table1()
    test_update_table2()
    test_delete_item()
    print("done.")
