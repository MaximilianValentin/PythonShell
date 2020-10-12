# information functions
def commands():
        commandList = ["commands", "square", "countChars", "make a note", "show my notes", "delete my notes", "create file", "new txt file", "new python script"]
        print(commandList)

# math functions
def square():
        vartosquare = input("insert value to square: ")
        result = int(vartosquare) ** 2
        print(result)

def countChars():
        objectToCount = input("insert string to count: ")
        counter = int(0)
        for i in str(objectToCount):
            counter += 1
        print(int(counter))

# note system
def make_a_note():
        file = open("note.txt", "a")
        newEntry = input("Inster your new entry: ")
        file.write("\n" + "- " + newEntry)
        file.close()

def show_my_notes():
        file = open("note.txt", "r")
        notes = file.read()
        print(notes)
        file.close()

def delete_my_notes():
        authentification = input("Are you sure that you want to delete all your notes?[y/n]: ")
        if authentification == "y":
                file = open("note.txt", "w")
                delete = ""
                file.write(delete)
                print("Your notes have been deleted")
        else:
                print("Your notes are not deleted")

def new_txt_file():
        filename = input("insert the filename: ")
        file = open(filename + ".txt", "w")
        content = input("start writing: ")
        file.write(content)
        file.close()

def new_script_python():
        filename = input("insert the filename: ")
        file = open(filename + ".py", "w")
        content = input("start coding: ")
        file.write(content)
        file.close()

def create_file():
        print("supported file types:")
        sup_fileT = ["1 .txt", "2 .py"]
        print(sup_fileT)
        chosen_type = input("insert the number or the filetype it self: ")
        if chosen_type == "1":
                new_txt_file()

        elif chosen_type == "2":
                new_script_python()

        else:
                print("this filetype is not supported")
