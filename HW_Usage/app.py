import psutil
from colorama import Fore, Style
import time

def print_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    print()

    if 0 <= cpu_usage < 50:
        print(f"{Fore.GREEN}CPU Usage: {cpu_usage}%{Style.RESET_ALL}")
    elif 50 <= cpu_usage < 75:
        print(f"{Fore.YELLOW}CPU Usage: {cpu_usage}%{Style.RESET_ALL}")
    elif cpu_usage >= 75:
        print(f"{Fore.RED}CPU Usage: {cpu_usage}%{Style.RESET_ALL}")

    if 0 <= ram_usage < 50:
        print(f"{Fore.GREEN}RAM Usage: {ram_usage}%{Style.RESET_ALL}")
    elif 50 <= ram_usage < 75:
        print(f"{Fore.YELLOW}RAM Usage: {ram_usage}%{Style.RESET_ALL}")
    elif ram_usage >= 75:
        print(f"{Fore.RED}RAM Usage: {ram_usage}%{Style.RESET_ALL}")

    if 0 <= disk_usage < 50:
        print(f"{Fore.GREEN}Disk Usage: {disk_usage}%{Style.RESET_ALL}")
    elif 50 <= disk_usage < 75:
        print(f"{Fore.YELLOW}Disk Usage: {disk_usage}%{Style.RESET_ALL}")
    elif disk_usage >= 75:
        print(f"{Fore.RED}Disk Usage: {disk_usage}%{Style.RESET_ALL}")

    if network_usage > 0:
        print(f"{Fore.GREEN}Network Usage: {network_usage} bytes{Style.RESET_ALL}")

if __name__ == "__main__":
    while True:
        print_usage()
        time.sleep(5)