menuChoice = ""
todos = list()

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
        if not todos:
            print("You have no todos\n")
        else:
            for index, item in enumerate(todos):
                print(f"{index}: {item}")

    if option == "A":
        try:
            userInput = input("Enter your todo: ")
            if userInput == "":
                raise ValueError("Input cannot be empty")
            todos.append(userInput)
            print(f"'{userInput}' added to your todos.\n")
        except ValueError as e:
            print(e)

    if option == "D":
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

    if option == "E":
        print("Have a great day!")
        exit()