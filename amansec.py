import os
import subprocess
import time
import random
import shutil

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

# ---------------------------------------centering menu | clear screen----------------------------------------

def print_centered(text):
    terminal_width = 80
    for _ in range(3):
        try:
            terminal_width = shutil.get_terminal_size().columns
            break  # Break if successful
        except OSError:
            time.sleep(0.1)  # Wait and try again
    else:
        terminal_width = 80

    centered_text = text.center(terminal_width)
    print(centered_text)

def clear_screen():
    os.system('clear')

# list of anime quotes

anime_quotes = [
    "If you can't hack it, then get out of the game.",
    "In the world of hackers, the only law is the law of the jungle.",
    "I don't need a backup plan; I am the plan.",
    "Hacking is like a chess game; every move counts.",
    "I'm not a criminal; I'm a programmer with attitude.",
    "The only thing standing between me and my goal is the code.",
    "Data is power, and I'm the one holding the key.",
    "You think you can stop me? I laugh in the face of your firewalls.",
    "I can turn your world upside down with a single line of code.",
    "The real world is just a simulation; I’m the one holding the controller.",
    "When you think you've secured everything, that's when I strike.",
    "You're just a user; I’m the master of this domain.",
    "I'm not breaking the rules; I'm redefining them.",
    "You play with fire, you get burned. I play with data, and I always win.",
    "A true hacker doesn't need permission.",
    "What’s a little breach in security? Just a chance to show off.",
    "Your encryption means nothing to me.",
    "I live in the code; I thrive in the chaos.",
    "You call it hacking; I call it digital exploration.",
    "In the realm of zeros and ones, I am the king."
]

# Get a random savage anime quote
def get_anime_quote():
    return random.choice(anime_quotes)

def main():
    clear_screen()
    print_fade_banner()  # Show fade banner on startup
    quote = get_anime_quote()  # Get a random quote
    print_centered(quote)
    print()

if __name__ == "__main__":
    main()
