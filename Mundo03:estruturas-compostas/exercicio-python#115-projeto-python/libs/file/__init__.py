from list_of_exercises.exercise115.libs.interface import *

def exist_file(name_file):
    try:
        file = open(name_file, "rt")
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create_file(name_file):
    try:
        file = open(name_file, "wt+")
        file.close()
    except:
        print("There was an ERROR creating the file")
    else:
        print(f"File {name_file} created successfully!")

def read_file(name_file):
    try:
        file = open(name_file, "rt")
    except:
        print("Error reading the file")
    else:
        #print("Reafing file...")
        header("Registered people")
        for line in file:
            date = line.split(";")
            date[1] = date[1].replace("\n", "")
            print(f"{date[0]:<30}{date[1]:>3} anos")
    finally:
        file.close()


def register(name_file, name_person="<unknow>", age_person=0):
    try:
        file = open(name_file, "at")
    except:
        print("Error opening the file")
    else:
        try:
            file.write(f"{name_person};{age_person}\n")
        except:
            print("An error occurred while writing the data!")
        else:
            print(f"New Register {name_person} added!")



