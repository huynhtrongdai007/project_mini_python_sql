import sqlite3
connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")

def add_entry(entry_content,entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES (?,?);",(entry_content,entry_date))

def view_entries(entries):
    for entry in entries:
        print(entry)
        print(f"{entry['date']}\n{entry['content']}\n\n")

def get_entries():
    entries = connection.execute("SELECT * FROM entries")
    return entries