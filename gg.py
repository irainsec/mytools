import os

# Function to print centered text in terminal
def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    centered_text = text.center(terminal_width)
    print(centered_text)

# Main function to run the tool
def main_menu():
    print_centered("Main Menu")
    print_centered("1. Create a Batch File")
    print_centered("2. System Information")
    print_centered("3. Exit")
    choice = input("Select an option: ")

    # Handle user choice here (like creating batch files, showing system info, etc.)
    if choice == '1':
        # Placeholder for batch file creation functionality
        print("Create a Batch File selected")
    elif choice == '2':
        # Placeholder for system info functionality
        print("System Information selected")
    elif choice == '3':
        print("Exiting...")
        exit()
    else:
        print("Invalid option, try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()
