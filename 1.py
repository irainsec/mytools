import os

# Function to print text with a small distance from the left
def print_shifted_left(text, padding=5):
    shifted_text = " " * padding + text
    print(shifted_text)

# Clear the terminal
def clear_screen():
    os.system('clear')

# Main function to display and replace menus dynamically
def dynamic_menu():
    while True:
        clear_screen()  # Clear the terminal before showing the main menu
        print_shifted_left("Main Menu")
        print_shifted_left("1. Create a Batch File")
        print_shifted_left("2. System Information")
        print_shifted_left("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == '1':
            # Replace with Batch File Creation Menu
            clear_screen()  # Clear the terminal before showing the batch file menu
            print_shifted_left("Batch File Creation Menu")
            print_shifted_left("1. Use Predefined Commands")
            print_shifted_left("2. Enter Custom Commands")
            print_shifted_left("3. Go Back")
            batch_choice = input("\nSelect an option: ")
            
            if batch_choice == '1':
                clear_screen()
                print_shifted_left("Using predefined commands...")
                input("\nPress Enter to return to the Batch File Menu")
            elif batch_choice == '2':
                clear_screen()
                print_shifted_left("Entering custom commands...")
                input("\nPress Enter to return to the Batch File Menu")
            elif batch_choice == '3':
                continue  # Go back to the main menu
            else:
                clear_screen()
                print_shifted_left("Invalid option, returning to Batch File Creation Menu...")

        elif choice == '2':
            # Replace with System Information Menu
            clear_screen()  # Clear the terminal before showing system info menu
            print_shifted_left("System Information Menu")
            print_shifted_left("1. Show Current Directory")
            print_shifted_left("2. List Files in Directory")
            print_shifted_left("3. Go Back")
            sys_info_choice = input("\nSelect an option: ")

            if sys_info_choice == '1':
                clear_screen()
                print_shifted_left(f"Current Directory: {os.getcwd()}")
                input("\nPress Enter to return to the System Information Menu")
            elif sys_info_choice == '2':
                clear_screen()
                files = os.listdir('.')
                print_shifted_left(f"Files in Directory: {files}")
                input("\nPress Enter to return to the System Information Menu")
            elif sys_info_choice == '3':
                continue  # Go back to the main menu
            else:
                clear_screen()
                print_shifted_left("Invalid option, returning to System Information Menu...")

        elif choice == '3':
            clear_screen()
            print_shifted_left("Exiting the tool. Goodbye!")
            break  # Exit the loop and end the program

        else:
            clear_screen()
            print_shifted_left("Invalid option, try again.")

# Run the tool
if __name__ == "__main__":
    dynamic_menu()
