print("\nWelcome to the To-Do List!")

# Initialize empty task list
tasks = []

# Validate menu action
while True:

  try:

    # Display main menu
    print("\n1. Add Task")
    print("2. Complete Task")
    print("3. Remove Task")
    print("4. View All Tasks")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Quit")

    # Get user's action
    action = int(input("Please select an action from the menu: "))

    if action == 1:
      print("\n-------- Add Task --------")

      # Gather task info
      completion_status = False
      date = input("\nEnter task date (MM/DD/YYYY): ")
      name = input("Enter task name: ")

      # Add task info to the task list
      task_info = {"completion_status": completion_status, "date": date, "name": name}
      tasks.append(task_info)

      print(f"\nSuccess! [{date} - {name}] has been added to the task list.")

    elif action == 2:
      print("\n----- Complete Task ------\n")

      # Display task list so the user can select which one to complete
      for i, task in enumerate(tasks):
        completion_status = task["completion_status"]
        date = task["date"]
        name = task["name"]

        # Use completion status to determine how the checkbox is displayed
        if completion_status == True:
          checkbox = "[X]"
        else:
          checkbox = "[ ]"

        print(f"{i + 1}. {checkbox} {date} - {name}")

      # Ensure user's value is a number and within the list range
      while True:

        try:

          # Prompt user for which task to complete and then change status to True
          task_to_complete = int(input("\nEnter task to complete: "))
          index_to_complete = task_to_complete - 1

          tasks[index_to_complete]["completion_status"] = True

          date = tasks[index_to_complete]["date"]
          name = tasks[index_to_complete]["name"]

          print(f"\nSuccess! [{date} - {name}] has been marked as complete.")
          break

        except ValueError, IndexError:
          print(f"\nError: invalid input. Please enter a number between 1 and {len(tasks)}.")

    elif action == 3:
      print("\n------ Remove Task -------\n")

      # Display task list so the user can select which one to remove
      for i, task in enumerate(tasks):
        completion_status = task["completion_status"]
        date = task["date"]
        name = task["name"]
      
        # Use completion status to determine how the checkbox is displayed
        if completion_status == True:
          checkbox = "[X]"
        else:
          checkbox = "[ ]"
      
        print(f"{i + 1}. {checkbox} {date} - {name}")

      # Prompt user for which task they'd like to remove
      task_to_remove = int(input("\nEnter task to remove: "))
      index_to_remove = task_to_remove - 1

      removed_task = tasks.pop(index_to_remove)

      print(f"\nSuccess! [{removed_task["date"]} - {removed_task["name"]}] has been removed from the task list.")

    elif action == 4:
      print("\n----- View All Tasks -----\n")

      # Display task list
      for i, task in enumerate(tasks):
        completion_status = task["completion_status"]
        date = task["date"]
        name = task["name"]
      
        # Use completion status to determine how the checkbox is displayed
        if completion_status == True:
          checkbox = "[X]"
        else:
          checkbox = "[ ]"
      
        print(f"{i + 1}. {checkbox} {date} - {name}")

    elif action == 5:
      print("\n------- Save Tasks -------")

    elif action == 6:
      print("\n------- Load Tasks -------")

    elif action == 7:
      print("\nThanks for using the To-Do List!")
      print("Goodbye.\n")
      break

    else:
      print("\nError: invalid input. Please enter a whole number between 1 and 7.")

  except ValueError:
    print("\nError: invalid input. Please enter a whole number between 1 and 7.")

# TODO
# Error handle index and value errors on complete and remove
# Prevent the user from entering 0 or negative values on complete and remove
# Display a message if the user tries to complete a task that is already completed and don't mark it as complete again