import os
import os.path

file_path = "./mydoc.txt"

if(os.path.exists(file_path) == True):
    print("File Exist")
else:
    print("File does not exist")
    open("./mydoc.txt","+w")


def Random_Function():
    questions = input("Please ask question to be recorded: ")
    print(f"you asked: {questions}")
    print("your question has been logged.")
    with open(file_path, 'a') as file:
        file.write(f"{questions}\n")

def What_Next_Yo():
    next_choice = input("what would you like to do next")



Random_Function()