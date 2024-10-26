# Creating a task class
class Task:
    def __init__(self, description, priority):
        # Initialize the task with a description and priority  
        self.description = description
        self.priority = priority
        self.completed = False   # Task starts as incomplete
     
    def mark_completed(self):
        # Mark the task as completed
        self.completed = True
    
    # Task editing function
    def edit_task(self, new_description=None, new_priority=None):
        if new_description:
            self.description = new_description
        if new_priority:
            self.priority = new_priority

    def __str__(self):
        # String representation of the task, showing status, description, and priority
        if self.completed:
            status = "Completed" 
        else:
            status = "Incomplete"

        return f"[{status}] Task: {self.description}, Priority: {self.priority}"

# Creating a To Do List class
class ToDoList:
    def __init__(self):
        self.tasks = []

    # Add Task Function
    def add_task(self, description, priority):
        # Add a new task to the to-do list
        task = Task(description, priority)

        self.tasks.append(task)  # Appends the new task to the task list.

        print("Task added successfully.")

    # Edits the List
    def edit_task(self, task_id, new_description=None, new_priority=None):
        if task_id < 0 or task_id >= len(self.tasks):
            print("Invalid task ID.")
            return
        self.tasks[task_id].edit_task(new_description, new_priority)
        print("Task updated successfully.")
    
    # Task Completion Marker 
    def mark_task_completed(self, task_id):
        if task_id < 0 or task_id >= len(self.tasks):
            print("Invalid task ID.")
            return
        self.tasks[task_id].mark_completed()
        print("Task marked as completed.")

    # Task Viewing Function
    def view_tasks(self):
        # If the list is empty
        if not self.tasks:
            print("No tasks available.")
            return
        
        # Print all tasks in the list
        for index, task in enumerate(self.tasks):    # enumerate(self.tasks) helps get both the index 
            print(f"{index + 1}. {task}")            # and the task itself. Index represents the 
                                                     # position of the task in the list,and task is the 
                                                     # actual Task object.
    # Deleting Task Function 
    def delete_task(self, task_id):
        if task_id < 0 or task_id >= len(self.tasks):
            print("Invalid task ID.")
            return
        self.tasks.pop(task_id)
        print("Task deleted successfully.")

# The main function
def main():
    todo_list = ToDoList()
    
    # List of Choices
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Delete Task")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            # Choice 1: Add Task
            if choice == 1:
                description = input("Enter task description: ")
                priority = input("Enter task priority (Low, Medium, High): ")
                todo_list.add_task(description, priority)
            
            # Choice 2: Edit Task
            elif choice == 2:
                todo_list.view_tasks()
                task_id = int(input("Enter task number to edit: ")) - 1
                new_description = input("Enter new description (leave blank to keep current): ")
                new_priority = input("Enter new priority (leave blank to keep current): ")
                todo_list.edit_task(task_id, new_description, new_priority)
             
            # Choice 3:  Mark Task as Completed
            elif choice == 3:
                todo_list.view_tasks()
                task_id = int(input("Enter task number to mark as completed: ")) - 1
                todo_list.mark_task_completed(task_id)
            
            # Choice 4: View Task
            elif choice == 4:
                todo_list.view_tasks()

            # Choice 5: Delete Task
            elif choice == 5:
                todo_list.view_tasks()
                task_id = int(input("Enter task number to delete: ")) - 1
                todo_list.delete_task(task_id)
           
            # Choice 6: Exit 
            elif choice == 6:
                print("Exiting the application. Goodbye!")
                break
            
            # Handling invalid choices
            else:
                print("Invalid choice, please try again.")
        
        # Handling user input errors(String instead of an integer.)
        except ValueError:
            print("Invalid input, please enter a number.")

# The main loop
if __name__ == "__main__":
    main()