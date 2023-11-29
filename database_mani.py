import sqlite3
#creating connection to database.
connection = sqlite3.connect('WORK ENVIRONMENT.db')
#create a cursor to execute statements through
cursor = connection.cursor()




# Drop the existing 'python_programming' table if it exists
cursor.execute('DROP TABLE IF EXISTS python_programming')
# Creating table
cursor.execute('CREATE TABLE python_programming (id INTERGER PRIMARY KEY, name TEXT, grade INTERGER)')
print("Table has been created.")
#creating data to be inputed into the table
data = [(55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)]
#insering cretaed data into table all at once
cursor.executemany('INSERT INTO python_programming(id,name,grade) VALUES(?,?,?)',data)
print("Table data has been inserted.")

# Select all records with a grade between 60 and 80.
cursor.execute('SELECT * FROM python_programming where grade BETWEEN 60 AND 80')
connection.commit()
# Fetch all the rows retrieved by the query.
select_rows = cursor.fetchall()
# Display the contents of the selected records
print("Retrieved results:")
for row in select_rows:
    print(row)

# Change Carl Davis’s grade to 65.
cursor.execute('UPDATE python_programming SET grade = 65 WHERE name = "Carl Davis" ')
connection.commit()
# Testing implemented changes.
cursor.execute('SELECT * FROM python_programming WHERE name = "Carl Davis" ')
update_row = cursor.fetchone()
print("Updated record for Carl Davis:", update_row)

# Delete Dennis Fredrickson’s row.
cursor.execute('DELETE FROM python_programming WHERE name = "Dennis Fredrickson" ')
connection.commit()
# Testing implemented changes.
cursor.execute('SELECT * FROM python_programming')
delete_rows = cursor.fetchall()
connection.commit()
print("Remaining data")
for row in delete_rows:
    print(row)

# Change the grade of all students, with an id greater than 55, to 80.
cursor.execute('UPDATE python_programming SET grade = 80 WHERE id > 55')
connection.commit()
# Testing implemented changes.
cursor.execute('SELECT * FROM python_programming where id > 55')
change_rows = cursor.fetchall()
print("udated grade rows:")
for row in change_rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
