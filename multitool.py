import os

# Predefined Windows commands
predefined_commands = {
    1: "echo Hello World",
    2: "dir",
    3: "pause",
    4: "ipconfig",
    5: "ping www.google.com",
    6: "cls",
    7: "shutdown /s /f /t 0"
}

# Function to create a .bat file with the given commands
def create_batch_file(filename, commands):
    try:
        # Add .bat extension if not provided
        if not filename.endswith('.bat'):
            filename += '.bat'

        # Create and open the .bat file for writing
        with open(filename, 'w') as batch_file:
            # Write the commands into the .bat file
            for command in commands:
                batch_file.write(command + '\n')

        print(f"Batch file '{filename}' created successfully!")
    except Exception as e:
        print(f"Error creating batch file: {e}")

# Function to display predefined commands
def show_predefined_commands():
    print("\nPredefined Commands:")
    for key, command in predefined_commands.items():
        print(f"{key}: {command}")
    print("Type 'custom' to enter your own command or 'done' to finish.")

# Function to get commands from user
def get_user_commands():
    commands = []
    print("\nEnter the commands you want to add to the batch file.")
    
    while True:
        # Show predefined commands and prompt for user input
        show_predefined_commands()
        choice = input("Select an option (or type 'custom' to enter manually): ").lower()

        if choice == 'done':
            break
        elif choice == 'custom':
            # If the user wants to enter a custom command
            custom_command = input("Enter your custom command: ")
            commands.append(custom_command)
        elif choice.isdigit() and int(choice) in predefined_commands:
            # If a predefined command is selected
            commands.append(predefined_commands[int(choice)])
        else:
            print("Invalid choice, please try again.")
    
    return commands

# Level 1 menu - Main menu
def main_menu():
    print("\n--- Main Menu ---")
    print("1. Create a Batch File")
    print("2. System Information")
    print("3. Exit")
    choice = input("Select an option: ")
    
    if choice == '1':
        batch_file_menu()  # Go to Batch File Creation Menu
    elif choice == '2':
        system_info_menu()  # Go to System Information Menu
    elif choice == '3':
        exit_program()  # Exit the tool
    else:
        print("Invalid option, try again.")
        main_menu()

# Level 2 menu - Batch file creation menu
def batch_file_menu():
    print("\n--- Batch File Creation Menu ---")
    print("1. Use Predefined Commands")
    print("2. Enter Custom Commands")
    print("3. Go Back")
    choice = input("Select an option: ")

    if choice == '1' or choice == '2':
        create_batch_file_workflow(choice)
    elif choice == '3':
        main_menu()
    else:
        print("Invalid option, try again.")
        batch_file_menu()

# Level 3 menu - Predefined or Custom Command Workflow
def create_batch_file_workflow(choice):
    filename = input("\nEnter the name of the batch file: ")

    if choice == '1':
        print("\nYou selected predefined commands.")
        commands = get_user_commands()  # Get predefined or custom commands
    elif choice == '2':
        print("\nYou selected custom commands.")
        commands = get_user_commands()  # Get predefined or custom commands

    create_batch_file(filename, commands)  # Create the batch file with the commands
    main_menu()  # Return to main menu

# Level 2 menu - System Information Menu
def system_info_menu():
    print("\n--- System Information Menu ---")
    print("1. Show Current Directory")
    print("2. List Files in Directory")
    print("3. Go Back")
    choice = input("Select an option: ")

    if choice == '1':
        current_directory = os.getcwd()
        print(f"Current Directory: {current_directory}")
        system_info_menu()
    elif choice == '2':
        files = os.listdir('.')
        print(f"Files in Directory: {files}")
        system_info_menu()
    elif choice == '3':
        main_menu()
    else:
        print("Invalid option, try again.")
        system_info_menu()

# Exit the program
def exit_program():
    print("Exiting the tool. Goodbye!")
    exit()

# Main function to start the tool
def main():
    print("\nWelcome to the Multi-Level Multitool!")
    main_menu()

if __name__ == "__main__":
    main()
