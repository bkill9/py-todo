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

      # Prompt user for which task to complete and then change status to True
      task_to_complete = int(input("\nEnter task to complete: "))
      index_to_complete = task_to_complete - 1

      tasks[index_to_complete]["completion_status"] = True

      date = tasks[index_to_complete]["date"]
      name = tasks[index_to_complete]["name"]

      print(f"\nSuccess! [{date} - {name}] has been marked as complete.")

    elif action == 3:
      print("\n------ Remove Task -------")

    elif action == 4:
      print("\n----- View All Tasks -----")

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