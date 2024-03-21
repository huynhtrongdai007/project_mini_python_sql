from database import *

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

welcome = "Welcome to the programming diary!"

print(welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        entry_content = input("What have you learned today? ")
        entry_date = input("Enter the date: ")
        add_entry(entry_content,entry_date)
    elif user_input == "2":
         view_entries(get_entries())
    else:
        print('Invalid option, please try again!')