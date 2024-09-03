#gui - graphical user interface
import functions
import PySimpleGUI #a third party module/library, can also install from terminal pypi.org PySimpleGUI 4.60.1

label=PySimpleGUI.Text("Type in a to-do")
input_box=PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button=PySimpleGUI.Button("Add")

window=PySimpleGUI.Window('My To-Do App',
                          layout=[[label], [input_box, add_button]],
                          font=('Helvetica', 15)) #window is a type like python data type, layout is argment, connecting all to windows instance

while True:
    event, values=window.read() #read() method shows the app on screen
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
