import webbrowser
import os

try:
    from termcolor import cprint
    from pyfiglet import figlet_format
except ImportError:
    print("Installing required modules...")
    os.system("pip install termcolor pyfiglet")
    from termcolor import cprint
    from pyfiglet import figlet_format

def show_banner():
    banner = """
⢀⢀⢀⢀⢀⢀⢀⢾⠟⡇
    ⢀⢀⢀⢀⢀⢀⢀⢀⠤⢿⡧⣀⡀
    ⢀⢀⢀⢀⢀⣀⡄⠶⠶⠶⠆⠉⠿⣛⣧⣀⣀⣀⣀⣤⣀
    ⢀⡀⢀⣀⣄⣶⠷⠂⣤⣤⣴⣾⡏⠉⠉⠉⠉⠉⠁
    ⠈⠋⠉⠉⠁⢀⢀⢀⢻⣿⣿⣿⡇
    ⢀⢀⢀⢀⢀⢀⢀⢀⢸⣿⣿⣿⣇
    ⢀⢀⢀⢀⢀⢀⢀⢀⣼⣿⣿⣿⣿⡀
    ⢀⢀⢀⢀⢀⢀⢀⢀⣿⣿⣿⣿⣿⡇
    ⢀⢀⢀⢀⢀⢀⢀⢠⣿⣿⣿⣿⣿⣷
    ⢀⢀⢀⢀⢀⢀⢀⢸⣿⣿⣿⣿⣿⣿
    ⢀⢀⢀⢀⢀⢀⢀⣼⣿⣿⣿⣿⣿⣿⡇
    ⢀⢀⢀⢀⢀⢀⢀⣿⣿⣿⣿⣿⣿⣿⡇
    ⢀⢀⢀⢀⢀⢀⢀⣿⣿⣿⣿⡿⣿⣿⡇
    ⢀⢀⢀⢀⢀⢀⢀⠙⠻⣿⣿⡇⣿⣿⠇
    ⢀⢀⢀⢀⢀⢀⢀⢀⢀⠈⢿⡇⢸⣿
    ⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠘⣷⢀⣿
    ⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢹⢀⣿
    ⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠈⢠⣿⡇
    ⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⠈⠉
"""
    cprint(banner, "magenta")
    cprint(figlet_format("Instagram Reporter", font="slant"), "cyan")

def show_menu():
    print("\nChoose an option:")
    cprint("1. Report Profile", "yellow")
    cprint("2. Report Chat (DM)", "green")

def show_profile_reports():
    print("\n--- Profile Report Types ---")
    reports = [
        "It's spam", "Fake profile", "Pretending to be someone else",
        "Abusive content", "Hate speech or symbols", "Harassment or bullying",
        "Nudity or sexual activity", "Illegal goods", "Self-injury concern",
        "Intellectual property", "Other"
    ]
    for i, r in enumerate(reports, 1):
        cprint(f"{i}. {r}", "cyan")

def show_chat_reports():
    print("\n--- Chat/DM Report Types ---")
    reports = [
        "Sexual content", "Threats or violence", "Harassment or bullying",
        "Scam or phishing", "Hate speech", "Other"
    ]
    for i, r in enumerate(reports, 1):
        cprint(f"{i}. {r}", "red")

def main():
    os.system("clear")
    show_banner()
    username = input("\nEnter Instagram username (without @): ").strip()
    show_menu()
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        show_profile_reports()
        input("Choose report type and press Enter to continue...")
        webbrowser.open(f"https://www.instagram.com/{username}/")

    elif choice == "2":
        show_chat_reports()
        input("Choose report type and press Enter to continue...")
        webbrowser.open("https://help.instagram.com/504932626364572")

    else:
        cprint("Invalid choice. Try again.", "red")

if __name__ == "__main__":
    main()