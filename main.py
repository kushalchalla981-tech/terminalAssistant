import sys
import os
from commands import app_launcher, file_manager, sys_info, utilities, animation
from datetime import datetime

def print_help():
    print("\n\033[96m" + "="*40 + "\033[0m")
    print("\033[1m✨ Available Commands ✨\033[0m")
    print("\033[96m" + "="*40 + "\033[0m")
    print("  \033[93mopen <app>\033[0m        - Open an application (e.g., notepad, calc, paint, browser)")
    print("  \033[93mopen file <path>\033[0m  - Open a specific file")
    print("  \033[93mopen folder <path>\033[0m- Open a folder in File Explorer")
    print("  \033[93mcreate file <name>\033[0m- Create a file")
    print("  \033[93mdelete file <name>\033[0m- Delete a file")
    print("  \033[93mcreate folder <name>\033[0m- Create a folder")
    print("  \033[93mdelete folder <name>\033[0m- Delete a folder")
    print("  \033[93mlist\033[0m              - List files and folders in current directory")
    print("  \033[93msearch <name>\033[0m     - Search for a file in the current directory and subdirectories")
    print("  \033[93msysinfo\033[0m           - Display system information (Task Manager style)")
    print("  \033[93mtimer <seconds>\033[0m   - Run a countdown timer")
    print("  \033[93mcalc <expr>\033[0m       - Perform a basic calculation")
    print("  \033[93mtime\033[0m              - Display current date and time with animation")
    print("  \033[93mhelp\033[0m              - Show this help message")
    print("  \033[93mclear\033[0m             - Clear the terminal screen")
    print("  \033[93mexit\033[0m              - Exit the assistant")
    print("\033[96m" + "="*40 + "\033[0m\n")

def main():
    # Attempt to enable VT100 Escape Codes for Windows for color support
    if os.name == 'nt':
        os.system('color')
        
    utilities.clear_screen()
    print("\033[1;32mWelcome to your Terminal Assistant!\033[0m Type 'help' to see available commands.")
    
    while True:
        try:
            current_time = datetime.now().strftime("%H:%M:%S")
            user_input = input(f"\n\033[1;33m[{current_time}]\033[0m \033[1;36mAssistant>\033[0m ").strip()
            if not user_input:
                continue
            
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""

            if command == "exit":
                print("\033[1;32mGoodbye! Have a great day!\033[0m")
                break
            elif command == "help":
                print_help()
            elif command == "clear":
                utilities.clear_screen()
            elif command == "open":
                if args.startswith("file "):
                    file_manager.open_item(args[5:].strip())
                elif args.startswith("folder "):
                    file_manager.open_item(args[7:].strip())
                else:
                    app_launcher.open_app(args)
            elif command == "create":
                if args.startswith("file "):
                    file_manager.create_file(args[5:].strip())
                elif args.startswith("folder "):
                    file_manager.create_folder(args[7:].strip())
                else:
                    print("\033[91mUsage: create file <name> OR create folder <name>\033[0m")
            elif command == "delete":
                if args.startswith("file "):
                    file_manager.delete_file(args[5:].strip())
                elif args.startswith("folder "):
                    file_manager.delete_folder(args[7:].strip())
                else:
                    print("\033[91mUsage: delete file <name> OR delete folder <name>\033[0m")
            elif command == "list":
                file_manager.list_directory()
            elif command == "search":
                if args:
                    file_manager.search_file(args)
                else:
                    print("\033[91mUsage: search <filename>\033[0m")
            elif command == "sysinfo":
                sys_info.display_sys_info()
            elif command == "timer":
                if args.isdigit():
                    utilities.run_timer(int(args))
                else:
                    print("\033[91mUsage: timer <seconds>\033[0m")
            elif command == "calc":
                if args:
                    utilities.calculate(args)
                else:
                    print("\033[91mUsage: calc <expression>\033[0m")
            elif command == "time":
                animation.display_time()
            else:
                print(f"\033[91mUnknown command: '{command}'. Type 'help' for a list of commands.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;32mGoodbye!\033[0m")
            break
        except Exception as e:
            print(f"\033[91mAn error occurred: {e}\033[0m")

if __name__ == "__main__":
    main()
