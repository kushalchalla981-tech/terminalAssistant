import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    # A cute full-body ASCII cat
    cat_art = r"""
\033[1;35m
    /\_/\  (
   ( ^.^ ) _)
     \"/  (
   ( | | )
  (__d b__)
\033[0m"""
    print(cat_art)

def run_timer(seconds):
    if seconds <= 0:
        print("\033[91mPlease provide a valid time in seconds over 0.\033[0m")
        return
        
    print(f"\033[32mTimer started for {seconds} seconds...\033[0m")
    try:
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(f"\r\033[1;33m⏳ {timer}\033[0m", end="")
            time.sleep(1)
            seconds -= 1
        print("\n\033[1;32m⏰ Time's up! ⏰\033[0m\a") # \a makes a system beep sound
    except KeyboardInterrupt:
        print("\n\033[91mTimer stopped by user.\033[0m")

def calculate(expression):
    try:
        # evaluate the mathematical expression safely
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            print("\033[91mInvalid characters in math expression. Only numbers, +, -, *, /, and () are allowed.\033[0m")
            return
            
        result = eval(expression)
        print(f"\033[32mResult:\033[0m \033[1;36m{result}\033[0m")
    except ZeroDivisionError:
        print("\033[91mError: Division by zero is not allowed.\033[0m")
    except Exception as e:
        print(f"\033[91mError calculating: {e}\033[0m")
