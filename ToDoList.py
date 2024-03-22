def add_task(todo_list, completed_list):
    # Implementation for adding a task
    while True:
        task_name = input("Enter a name for your task: ")
        if any(task['name'].lower() == task_name.lower() for task in todo_list):
            print("A task with this name already exists. Please use a different name.")
            continue
        if any(task['name'].lower() == task_name.lower() for task in completed_list):
            print("Nice job! This task is already completed! Please use a different name.")
            continue
        task_description = input("Enter a description of the task: ")
        confirm_task = input(f"""Would you like to enter the following task: 
{task_name}: {task_description}
(Y or N): """).lower()
        if confirm_task == 'y':
            todo_list.append({
                'name' : task_name,
                'description' : task_description
            })
            print("Task added successfully.")
            break
        else:
            print("Task addition cancelled.")
            break

    print("")
    return todo_list
    

def view_tasks(todo_list):
    # Implementation for viewing tasks
    if not todo_list:
        print("You have no tasks.\n")
        return
    
    print("Here is a list of tasks to complete:")

    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task['name']}: {task['description']}")
    
    print("")
    return


def view_completed_tasks(completed_task):
    #Implementation for veiwing completed tasks
    if not completed_task:
        print("You have no completed tasks. Time to get to work!\n")
        return
    
    print("Here is a list of the tasks you have completed: ")
    for index, task in enumerate(completed_task, start=1):
        print(f"{index}. {task['name']}: {task['description']}")

    print("")
    return


def mark_task_complete(todo_list, completed_task):
    if not todo_list:
        print("No tasks to complete.")
        return todo_list, completed_task
    
    complete_request = input("Enter the name or number of the task you would like to mark completed: ")

    try:
        complete_index = int(complete_request) - 1
        if 0 <= complete_index < len(todo_list):
            completed_task.append(todo_list[complete_index])
            todo_list.pop(complete_index) 
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        found = False
        for i, task in enumerate(todo_list):
            if task['name'].lower() == complete_request.lower():
                completed_task.append(todo_list[i])
                todo_list.pop(i) 
                print("Task marked as complete.")
                found = True
                break
        if not found:
            print("Task not found.")

    print("")        
    return todo_list, completed_task


def delete_task(todo_list, delete_input):
    # Implementation for deleting a task
    if not todo_list:
        print("No tasks to delete.\n")
        return
    
    if delete_input:
        delete_request = delete_input
    else:
        delete_request = input("Enter the name or number of the task you want to delete: ")
 
    try:
        delete_index = int(delete_request)-1
        if 0 <= delete_index < len(todo_list):
            del todo_list[delete_index]
            print("Task removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        found = False
        for i, task in enumerate(todo_list):
            if task['name'].lower() == delete_request.lower():
                del todo_list[i]
                print("Task deleted successfully.")
                found = True
                break
            if not found:
                print("Task not found.")

    print("")
    return todo_list


def quit_app():
    print("Thank you for using the To-Do List App!\nQuitting...")
    exit(0)  # This exits the program


todo_list = []
completed_task = []

while True:
    print('''Menu:
          1. Add a task
          2. View tasks
          3. View completed tasks
          4. Mark task as complete
          5. Delete a task
          6. Quit''')
    user_input = input("What would you like to do with your To-Do List? ")
    print("")
    try:
        user_input = int(user_input)
        if user_input == 1:
            todo_list = add_task(todo_list, completed_task)
        elif user_input == 2:
            view_tasks(todo_list)
        elif user_input == 3:
            view_completed_tasks(completed_task)
        elif user_input == 4:
            todo_list, completed_task = mark_task_complete(todo_list, completed_task)
        elif user_input == 5:
            todo_list = delete_task(todo_list, "")
        elif user_input == 6:
            quit_app()
        else:
            print("Please enter a number between 1 and 6.")
    except ValueError:
        print("Please enter a valid number.\n")
