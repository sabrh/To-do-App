FILEPATH="todos.txt"


def get_todos(filepath=FILEPATH): #function argument with default argument
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local #local variable


def write_todos(todos_arg, filepath=FILEPATH): #multiple argument, non default parameter follows default parameter
    with open(filepath, 'w') as file:
        file.writelines(todos_arg) #this function is like a procedure, dosent return anything


"""
When you want the output of a code only in functions.py but not when running main.py
print(__name__)

if __name__=="__main__":
    print("Hello")
    print(get_todos())
"""