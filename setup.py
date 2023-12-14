import sqlite3

connection = sqlite3.connect("your_database.db")  # Replace "your_database.db" with your actual database file name
cursor = connection.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS table1")
    cursor.execute("DROP TABLE IF EXISTS table2")
except Exception as e:
    print(f"Error dropping tables: {e}")

# Create the 'table1' table
try:
    cursor.execute("CREATE TABLE table1 (Types TEXT PRIMARY KEY)")
except Exception as e:
    print(f"Error creating 'table1' table: {e}")

# Create the 'table2' table
try:
    cursor.execute("CREATE TABLE table2 (Types TEXT PRIMARY KEY, Count INTEGER)")
except Exception as e:
    print(f"Error creating 'table2' table: {e}")

# Insert sample data into 'table1' table
table1_data = [('fruits',), ('vegetables',), ('powders',)]

for item_data in table1_data:
    try:
        cursor.execute("INSERT INTO table1 (Types) VALUES (?)", item_data)
    except Exception as e:
        print(f"Error inserting data into 'table1' table: {e}")

# Insert sample data into 'table2' table
table2_data = [('fruits', 10), ('vegetables', 20), ('powders', 15)]

for item_data in table2_data:
    try:
        cursor.execute("INSERT INTO table2 (Types, Count) VALUES (?, ?)", item_data)
    except Exception as e:
        print(f"Error inserting data into 'table2' table: {e}")

connection.commit()
connection.close()
print("done.")
