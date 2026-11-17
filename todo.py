print("\nWelcome to the To-Do List!")

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

    elif action == 2:
      print("\n----- Complete Task ------")

    elif action == 3:
      print("\n------ Remove Task -------")

    elif action == 4:
      print("\n----- View All Tasks -----")

    elif action == 5:
      print("\n------- Save Tasks -------")

    elif action == 6:
      print("\n------- Load Tasks -------")

    elif action == 7:
      print("\n---------- Quit ----------")

    else:
      print("\nError: invalid input. Please enter a whole number between 1 and 7.")

  except ValueError:
    print("\nError: invalid input. Please enter a whole number between 1 and 7.")