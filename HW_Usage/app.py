import psutil
from colorama import Fore, Style
import time

def print_device_usage(device, device_type):
    if 0 <= device < 50:
        print(f"{Fore.GREEN}{device_type} Usage: {device}%{Style.RESET_ALL}")
    elif 50 <= device < 75:
        print(f"{Fore.YELLOW}{device_type} Usage: {device}%{Style.RESET_ALL}")
    elif device >= 75:
        print(f"{Fore.RED}{device_type} Usage: {device}%{Style.RESET_ALL}")

def print_network_usage(network):
    if network > 0:
        print(f"{Fore.GREEN}Network Usage: {network} bytes{Style.RESET_ALL}\n")

def print_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    network_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    print_device_usage(cpu_usage, "CPU")
    print_device_usage(ram_usage, "RAM")
    print_device_usage(disk_usage,"Disk")
    print_network_usage(network_usage)

if __name__ == "__main__":
    while True:
        print_usage()
        time.sleep(5)