import os
import subprocess

def open_app(app_name):
    """Opens preinstalled applications on Windows based on simple names."""
    if not app_name:
        print("\033[91mPlease specify an app to open (e.g., notepad, calc).\033[0m")
        return

    # Map simple names to executables/URIs
    apps = {
        "notepad": "start notepad",
        "calc": "start calc",
        "calculator": "start calc",
        "paint": "start mspaint",
        "mspaint": "start mspaint",
        "explorer": "start explorer",
        "browser": "start https://www.google.com",
        "edge": "start msedge:https://www.google.com",
        "cmd": "start cmd",
        "taskmgr": "start taskmgr",
        "settings": "start ms-settings:",
        "wordpad": "start write"
    }

    app_name_lower = app_name.lower()
    
    if app_name_lower in apps:
        cmd = apps[app_name_lower]
        print(f"\033[32mOpening {app_name}...\033[0m")
        try:
            os.system(cmd)
        except Exception as e:
            print(f"\033[91mFailed to open {app_name}. Error: {e}\033[0m")
    else:
        # Try to run it generically
        print(f"\033[33m'{app_name}' not found in quick list. Attempting to start via system...\033[0m")
        try:
            os.system(f"start {app_name}")
        except Exception as e:
            print(f"\033[91mFailed to open '{app_name}'. Error: {e}\033[0m")
