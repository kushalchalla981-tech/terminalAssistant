import psutil
import platform

def get_size(bytes_num, suffix="B"):
    """Scale bytes to its proper format."""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes_num < factor:
            return f"{bytes_num:.2f}{unit}{suffix}"
        bytes_num /= factor

def display_sys_info():
    print("\n\033[96m" + "="*40 + "\033[0m")
    print("\033[1;35m📊 System Information (Task Manager)\033[0m")
    print("\033[96m" + "="*40 + "\033[0m")
    
    # System info
    uname = platform.uname()
    print(f"\033[1;36mSystem:\033[0m {uname.system} {uname.release} (Version: {uname.version})")
    print(f"\033[1;36mMachine:\033[0m {uname.machine}")
    print(f"\033[1;36mNode Name:\033[0m {uname.node}\n")
    
    # CPU
    try:
        print("\033[1;33m--- 🧠 CPU ---\033[0m")
        print(f"Physical cores: {psutil.cpu_count(logical=False)}")
        print(f"Total cores: {psutil.cpu_count(logical=True)}")
        cpufreq = psutil.cpu_freq()
        if cpufreq:
            print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
            print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        print(f"CPU Usage: \033[1;31m{psutil.cpu_percent(interval=1)}% \033[0m\n")
    except Exception as e:
        print(f"\033[91mFailed to read CPU stats: {e}\033[0m\n")

    # Memory
    try:
        print("\033[1;33m--- 💾 Memory ---\033[0m")
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: {get_size(svmem.used)}")
        print(f"Percentage: \033[1;31m{svmem.percent}% \033[0m\n")
    except Exception as e:
        print(f"\033[91mFailed to read memory stats: {e}\033[0m\n")
    
    # Disk Input/Output
    try:
        print("\033[1;33m--- 💽 Disk Information ---\033[0m")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"  \033[36mDevice:\033[0m {partition.device}")
            print(f"    Mountpoint: {partition.mountpoint}")
            print(f"    File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                print(f"    Total Size: {get_size(partition_usage.total)}")
                print(f"    Used: {get_size(partition_usage.used)}")
                print(f"    Free: {get_size(partition_usage.free)}")
                print(f"    Percentage: \033[32m{partition_usage.percent}%\033[0m\n")
            except PermissionError:
                print("    \033[91mAccess Denied\033[0m\n")
    except Exception as e:
        print(f"\033[91mFailed to read disk stats: {e}\033[0m\n")

    print("\033[96m" + "="*40 + "\033[0m\n")
