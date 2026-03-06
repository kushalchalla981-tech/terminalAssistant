import time
from datetime import datetime
import sys

def display_time():
    print("\033[36mDisplaying animated time. Press Ctrl+C to stop.\033[0m")
    try:
        # Animation states for the clock/hourglass
        spinners = ['⏳', '⌛', '🕒', '🕝', '🕑', '🕜', '🕐', '🕧']
        colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
        
        idx = 0
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_date = now.strftime("%A, %B %d, %Y")
            
            spinner = spinners[idx % len(spinners)]
            color = colors[(idx // len(spinners)) % len(colors)]
            
            frame = f"\r{color}{spinner}  {current_date}  |  {current_time} \033[0m"
            
            sys.stdout.write(frame)
            sys.stdout.flush()
            
            idx += 1
            time.sleep(0.2) # Animate the spinner quickly
            
    except KeyboardInterrupt:
        print("\n\033[32mStopped time display.\033[0m")
