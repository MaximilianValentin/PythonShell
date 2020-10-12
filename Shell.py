import PythonClasses
shellCode = 1


while shellCode == 1:
    lastStatement = input("$ ")
    if lastStatement == "":
        print("")
    elif lastStatement == "square":
        PythonClasses.square()
    elif lastStatement == "commands":
        PythonClasses.commands()
    elif lastStatement == "countChars":
        PythonClasses.countChars()
    elif lastStatement == "make a note":
        PythonClasses.make_a_note()
    elif lastStatement == "show my notes":
        PythonClasses.show_my_notes()
    elif lastStatement == "delete my notes":
        PythonClasses.delete_my_notes()
    elif lastStatement == "new python script":
        PythonClasses.new_script_python()
    elif lastStatement == "create file":
        PythonClasses.create_file()
    elif lastStatement == "new text file":
        PythonClasses.new_txt_file()
    elif lastStatement == "exit":
        break
    else:
        print("!!!command not found!!!")
