menuChoice = ""
todos = list()

def print_todos():
    if not todos:
        print("You have no todos\n")
    else:
        for index, item in enumerate(todos):
            print(f"{index}: {item}")

def create_todo():
    try:
        user_input = input("Enter your todo: ")
        if user_input == "":
            raise ValueError("Input cannot be empty")
        todos.append(user_input)
        print(f"'{user_input}' added to your todos.\n")
    except ValueError as e:
        print(e)

def delete_todo():
    try:
        index_to_delete = int(
            input("Please enter the index of the todo you would like to delete: "))
        if 0 <= index_to_delete < len(todos):
            deleted_item = todos.pop(index_to_delete)
            print(f"Todo '{deleted_item}' removed.\n")
        else:
            print("Invalid index. Please enter a valid index from the list.\n")

    except ValueError:
        print("Invalid input. Please enter a number for the index.\n")


def main():
    print("Select an option:")
    print("[S]how todos")
    print("[A]dd a todo")
    print("[D]elete a todo")
    print("[E]xit")

    while (True):

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