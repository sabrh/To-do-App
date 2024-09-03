from functions import get_todos, write_todos #a local module we created
#import functions
import time #this is standard python module --python date time format codes, python module index on google

now=time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add/new, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo=user_action[4:] #list slicing
        todos=get_todos() #function calling, todos is global variables
        #todos=functions.get_todos() -- when only import functions
        todos.append(todo+'\n')
        write_todos(todos) #no need to mention the default arg here

    elif user_action.startswith("show"): #| 'display':
        todos=get_todos() #todos=get_todos("todos.txt") without the default argument

        for index, item in enumerate(todos):
            item=item.title()
            item=item.strip('\n')
            row=f"{index+1}.{item}" #removing unnecessary spaces using f- string
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number=number-1

            todos=get_todos() #assigning a text file or value here replaces the default argument

            new_todo=input("Enter new todo for edit: ")
            todos[number]=new_todo+'\n'
            write_todos(todos)

        except ValueError: #Error handling
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos=get_todos()

            index=number-1
            todo_to_remove=todos[index].strip('\n') #stripping the line break
            todos.pop(index)

            write_todos(todos)

            message=f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no such index.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, you entered an unknown command.")

print("Bye!")