#To-do List
class ToDoList():
    def __init__(self):
        self.list = []
        self.stored_list = []
        self.current_length = len(self.list)
        self.i = True
    def printTask(self):
        self.current_length = len(self.list)
        n = 1
        if self.current_length > 0:
            for task in self.list:
                todo = f"{n}"+". "+task
                print(todo)
                self.stored_list.append(todo)
                n= n + 1
        else:
            print("List Empty")
        print("Enter to move foward")
    def deleteTask(self):
        self.printTask()
        if len(self.list) > 0:
            self.wanted_index = input("Enter Index to delete: ")
            w = 0
            for storedtask in self.stored_list:
                print(storedtask[0])
                if storedtask[0] == self.wanted_index:
                    self.list.pop(w)
                    self.stored_list.pop(w)
                else:
                    w = w + 1
        else:
            print("List Empty")
    def newTask(self):
        self.new = input("Enter task: ")
        self.list.append(self.new)
    def mainloop(self):
        while self.i:
            menu()
def menu():
    print("=---- To-Do List Menu ----=")
    print("1. Add Task")
    print("2. Print To do list")
    print("3. Delete Task")
    print("x. Exit")
    print("=----------- GD ----------=")
    choice = input("Enter Choice: ")
    if choice == "1":
        tdl.newTask()
    if choice =="2":
        tdl.printTask()
    if choice == "3":
        tdl.deleteTask()
    if choice =="x" or choice.lower() == "exit":
        quit()
tdl = ToDoList()
tdl.mainloop()