from repo.todo_repo import create_todo, print_todos, delete_todo
menuChoice = ""

def main():
    print("Select an option:")
    print("[S]how todos")
    print("[A]dd a todo")
    print("[D]elete a todo")
    print("[E]xit")

    while True:

        print("Select an option:")
        selected_option = input("=> ")
        option = selected_option.upper()
        if option == "S":
            print_todos()
        elif option == "A":
            create_todo()
        elif option == "D":
            delete_todo()
        elif option == "E":
            print("Have a great day!")
            exit()
        else:
            print("Invalid choice. Please select a valid option (S, A, D, or E).\n")

if __name__ == "__main__":
    main()