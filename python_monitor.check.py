import subprocess

def check_monitor_mode(interface):
    try:
        output = subprocess.check_output(["iwconfig", interface])
        output = output.decode("utf-8")
        if "Mode:Monitor" in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    interface = "wlan0"  # Change this to your wlan interface name
    if check_monitor_mode(interface):
        print(f"{interface} is in monitor mode.")
    else:
        print(f"{interface} is not in monitor mode.")
