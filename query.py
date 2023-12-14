import sqlite3

connection = sqlite3.connect("your_database.db")
cursor = connection.cursor()

# Fetch data from the 'table1' and 'table2' tables
cursor.execute("SELECT Types FROM table1")
table1_rows = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Types, Count FROM table2")
table2_rows = [{'Type': row[0], 'Count': row[1]} for row in cursor.fetchall()]

print("Table 1:")
print(table1_rows)

print("\nTable 2:")
print(table2_rows)

# Combine the data into a single list of dictionaries
combined_data = []

for item_type in table1_rows:
    related_item = next((item for item in table2_rows if item['Type'] == item_type), None)
    combined_item = {'Type': item_type, 'Count': related_item['Count'] if related_item else 0}
    combined_data.append(combined_item)

print("\nCombined Data:")
print(combined_data)
