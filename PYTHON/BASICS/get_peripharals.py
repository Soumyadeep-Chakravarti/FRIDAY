import os
import psutil
import platform
import basic_functions
from datetime import datetime
import speech_recognition as s_r
from usbmonitor import USBMonitor
from usbmonitor.attributes import ID_MODEL, ID_MODEL_ID, ID_VENDOR_ID

peripharals_file = os.path.join(os.path.expanduser("~"),"Documents","FRIDAY_AI","PERIPHARALS")

data = []
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

string = "="*40, "System Information", "="*40
data.append(string)

uname = platform.uname()

data.append(f"System: {uname.system}\nNode Name: {uname.node}\nRelease: {uname.release}\nVersion: {uname.version}\nMachine: {uname.machine}\nProcessor: {uname.processor}\n")

# Boot Time
string = "="*40, "Boot Time", "="*40
data.append(string)

boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
data.append(f"\nBoot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n")

# let's print CPU information
string = "="*40, "CPU Info", "="*40
data.append(string)


# number of cores
data.append(f"\nPhysical cores: {psutil.cpu_count(logical=False)}\nTotal cores: {psutil.cpu_count(logical=True)}")

# CPU frequencies
cpufreq = psutil.cpu_freq()
data.append(f"\nMax Frequency: {cpufreq.max:.2f}Mhz\nMin Frequency: {cpufreq.min:.2f}Mhz\nCurrent Frequency: {cpufreq.current:.2f}Mhz\n")

# CPU usage

data.append("CPU Usage Per Core:\n")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    data.append(f"Core {i}: {percentage}%\n")
data.append(f"Total CPU Usage: {psutil.cpu_percent()}%\n")
# Memory Information
string = "="*40, "Memory Information", "="*40
data.append(string)
# get the memory details
svmem = psutil.virtual_memory()
data.append(f"\nTotal: {get_size(svmem.total)}\nAvailable: {get_size(svmem.available)}\nUsed: {get_size(svmem.used)}\nPercentage: {svmem.percent}%\n")

string = "="*20, "SWAP", "="*20
data.append(string)
# get the swap memory details (if exists)
swap = psutil.swap_memory()
data.append(f"\nTotal: {get_size(swap.total)}\nFree: {get_size(swap.free)}\nUsed: {get_size(swap.used)}\nPercentage: {swap.percent}%\n")

# Disk Information
string = "="*40, "Disk Information", "="*40,"\nPartitions and Usage:"
data.append(string)
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    data.append(f"\n=== Device: {partition.device} ===\n  Mountpoint: {partition.mountpoint}\n  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    data.append(f"\n  Total Size: {get_size(partition_usage.total)}\n  Used: {get_size(partition_usage.used)}\n  Free: {get_size(partition_usage.free)}\n  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
data.append(f"\nTotal read: {get_size(disk_io.read_bytes)}\nTotal write: {get_size(disk_io.write_bytes)}\n")

# Network information
string = "="*40, "Network Information", "="*40
data.append(string)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        data.append(f"\n=== Interface: {interface_name} ===\n")
        if str(address.family) == 'AddressFamily.AF_INET':
            data.append(f"\n  IP Address: {address.address}\n  Netmask: {address.netmask}\n  Broadcast IP: {address.broadcast}\n")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            data.append(f"\n  MAC Address: {address.address}\n  Netmask: {address.netmask}\n  Broadcast MAC: {address.broadcast}\n")
# get IO statistics since boot
net_io = psutil.net_io_counters()
data.append(f"\nTotal Bytes Sent: {get_size(net_io.bytes_sent)}\nTotal Bytes Received: {get_size(net_io.bytes_recv)}\n")

string = "="*40, "Connected Devices", "="*40,"\n"
data.append(string)
string = "="*20, "Connected USB Devices", "="*20,"\n"
# Create the USBMonitor instance
monitor = USBMonitor()

# Get the current devices
devices_dict = monitor.get_available_devices()

# Print them
for device_id, device_info in devices_dict.items():
    data.append(f"  {device_id} -- {device_info[ID_MODEL]} ({device_info[ID_MODEL_ID]} - {device_info[ID_VENDOR_ID]})")
string = "="*20, "Microphones", "="*20,"\n"
data.append(string)
for item in s_r.Microphone.list_microphone_names():
    data.append(f"  {item}\n")


basic_functions.write_file(1,f"peripharals_{basic_functions.date_for_file()}",peripharals_file,data)
