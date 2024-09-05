#gui - graphical user interface
import functions
import PySimpleGUI #a third party module/library, can also install from terminal pypi.org PySimpleGUI 4.60.1
import time

PySimpleGUI.theme("DarkPurple4")

clock=PySimpleGUI.Text('', key="clock")
label=PySimpleGUI.Text("Type in a to-do")
input_box=PySimpleGUI.InputText(tooltip="Enter todo", key="todo")
add_button=PySimpleGUI.Button("Add", size=10)
list_box=PySimpleGUI.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[35, 10]) #list of existing items, size is the size of box
edit_button=PySimpleGUI.Button("Edit")
complete_button=PySimpleGUI.Button("Complete")
exit_button=PySimpleGUI.Button("Exit")

window=PySimpleGUI.Window('My To-Do App',
                          layout=[[clock],
                                  [label],
                                  [input_box, add_button],
                                  [list_box, edit_button, complete_button],
                                  [exit_button]],
                          font=('Helvetica', 15)) #window is a type like python data type, layout is argment, connecting all to windows instance

while True:
    event, values=window.read(timeout=200) #read() method shows the app on screen
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    #print(1, event)
    #print(2, values)
    #print(3, values['todos'])
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit=values['todos'][0]
                new_todo=values['todo']

                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                PySimpleGUI.popup("Please select and item first.", font=('Helvetica', 15))
        case "Complete":
            try:
                todo_to_complete=values['todos'][0]
                todos=functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                PySimpleGUI.popup("Please select and item first.", font=('Helvetica', 15))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
