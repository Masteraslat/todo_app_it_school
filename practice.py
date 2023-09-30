last_todo = ""
def main_menu():
    print("TODO APP")
    print("-" * 50)
    print("Menu:\n")
    print("1. Show last TODO")
    print("2. Add new TODO\n")
    print("0. Exit\n")
    return input("Enter your choice and press ENTER: ")

u_choice = main_menu()

while u_choice != "0":
    if u_choice == "1":
        print("Last todo:", last_todo)
    elif u_choice == "2":
        last_todo = input("Enter TODO: ")
    else:
        print("ERROR!")
    u_choice = main_menu()

