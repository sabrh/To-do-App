#gui - graphical user interface
import functions
import PySimpleGUI #a third party module/library, can also install from terminal pypi.org PySimpleGUI 4.60.1

label=PySimpleGUI.Text("Type in a to-do")
input_box=PySimpleGUI.InputText(tooltip="Enter todo")
add_button=PySimpleGUI.Button("Add")

window=PySimpleGUI.Window('My To-Do App', layout=[[label], [input_box, add_button]]) #window is a type like python data type, layout is argment, connecting all to windows instance
window.read() #read() method shows the app on screen
window.close()
