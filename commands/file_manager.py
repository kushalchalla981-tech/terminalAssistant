import os
import shutil
from pathlib import Path

def create_file(filename):
    if not filename:
        print("\033[91mFilename cannot be empty.\033[0m")
        return
    try:
        path = Path(filename)
        path.touch(exist_ok=False)
        print(f"\033[32mFile created successfully: {filename}\033[0m")
    except FileExistsError:
        print(f"\033[93mFile already exists: {filename}\033[0m")
    except Exception as e:
        print(f"\033[91mError creating file: {e}\033[0m")

def delete_file(filename):
    if not filename:
        print("\033[91mFilename cannot be empty.\033[0m")
        return
    try:
        path = Path(filename)
        if path.is_file():
            path.unlink()
            print(f"\033[32mFile deleted successfully: {filename}\033[0m")
        else:
            print(f"\033[93mFile not found: {filename}\033[0m")
    except Exception as e:
        print(f"\033[91mError deleting file: {e}\033[0m")

def create_folder(foldername):
    if not foldername:
        print("\033[91mFolder name cannot be empty.\033[0m")
        return
    try:
        path = Path(foldername)
        path.mkdir(parents=True, exist_ok=False)
        print(f"\033[32mFolder created successfully: {foldername}\033[0m")
    except FileExistsError:
        print(f"\033[93mFolder already exists: {foldername}\033[0m")
    except Exception as e:
        print(f"\033[91mError creating folder: {e}\033[0m")

def delete_folder(foldername):
    if not foldername:
        print("\033[91mFolder name cannot be empty.\033[0m")
        return
    try:
        path = Path(foldername)
        if path.is_dir():
            shutil.rmtree(path)
            print(f"\033[32mFolder deleted successfully: {foldername}\033[0m")
        else:
            print(f"\033[93mFolder not found: {foldername}\033[0m")
    except Exception as e:
        print(f"\033[91mError deleting folder: {e}\033[0m")

def list_directory():
    try:
        current_dir = Path.cwd()
        print(f"\033[96mContents of {current_dir}:\033[0m")
        for item in current_dir.iterdir():
            if item.is_dir():
                print(f"  \033[1;34m[DIR]\033[0m {item.name}")
            else:
                print(f"  \033[37m[FILE]\033[0m {item.name}")
    except Exception as e:
        print(f"\033[91mError listing directory: {e}\033[0m")

def search_file(filename):
    print(f"\033[36mSearching for '{filename}' in current directory and subdirectories...\033[0m")
    found = False
    try:
        current_dir = Path.cwd()
        # rglob enables recursive searching
        for path in current_dir.rglob(f"*{filename}*"):
            print(f"  \033[32mFound:\033[0m {path}")
            found = True
            
        if not found:
            print(f"\033[93mNo files matching '{filename}' were found.\033[0m")
    except Exception as e:
        print(f"\033[91mError searching for file: {e}\033[0m")

def open_item(item_path):
    if not item_path:
        print("\033[91mPath cannot be empty.\033[0m")
        return
    try:
        path = Path(item_path)
        if path.exists():
            print(f"\033[32mOpening:\033[0m {path.absolute()}")
            os.startfile(path)
        else:
            # Try to find it in the current directory tree
            print(f"\033[33mPath '{item_path}' not found directly. Searching...\033[0m")
            current_dir = Path.cwd()
            found = False
            for p in current_dir.rglob(f"*{item_path}*"):
                if p.is_dir() or p.is_file():  # Open first match (prioritizes how rglob yields)
                    print(f"\033[32mFound and Opening:\033[0m {p.absolute()}")
                    os.startfile(p)
                    found = True
                    break
            
            if not found:
                print(f"\033[91mCould not find any file or folder matching '{item_path}'.\033[0m")
    except AttributeError:
        # Fallback for non-Windows systems (though project is Windows-only)
        try:
            os.system(f"start \"\" \"{item_path}\"")
        except Exception as e:
            print(f"\033[91mError opening item: {e}\033[0m")
    except Exception as e:
        print(f"\033[91mError opening item: {e}\033[0m")
