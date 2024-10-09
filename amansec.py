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
" █████╗ ███╗   ███╗ █████╗ ███╗   ██╗              ███████╗███████╗ ██████╗",
"██╔══██╗████╗ ████║██╔══██╗████╗  ██║              ██╔════╝██╔════╝██╔════╝",
"███████║██╔████╔██║███████║██╔██╗ ██║    █████╗    ███████╗█████╗  ██║     ",
"██╔══██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ╚════╝    ╚════██║██╔══╝  ██║     ",
"██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║              ███████║███████╗╚██████╗",
"╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝              ╚══════╝╚══════╝ ╚═════╝",
                                                                           
]

    terminal_width = os.get_terminal_size().columns
    print()  # Add space above the banner

    # Print each line of the banner with a fade effect
    for i, line in enumerate(banner_text):
        padding = (terminal_width - len(line)) // 2
        print(f"{colors[i]}{' ' * padding}{line}\033[0m")
        time.sleep(0.1)  # Optional delay for fade effect

    print()  # Add space below the banner
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

# ---------------------------------------Main Functions----------------------------------------

def main():
    print_fade_banner()  # Show fade banner on startup

if __name__ == "__main__":
    main()
