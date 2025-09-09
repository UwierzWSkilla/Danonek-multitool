import subprocess
import ipaddress
import json


with open("scan_options.json", "r") as f:
    scan_options = json.load(f)

logo = r"""

·▄▄▄▄   ▄▄▄·  ▐ ▄        ▐ ▄ ▄▄▄ .▄ •▄     • ▌ ▄ ·. ▄• ▄▌▄▄▌  ▄▄▄▄▄▪  ▄▄▄▄▄            ▄▄▌  
██▪ ██ ▐█ ▀█ •█▌▐█▪     •█▌▐█▀▄.▀·█▌▄▌▪    ·██ ▐███▪█▪██▌██•  •██  ██ •██  ▪     ▪     ██•  
▐█· ▐█▌▄█▀▀█ ▐█▐▐▌ ▄█▀▄ ▐█▐▐▌▐▀▀▪▄▐▀▀▄·    ▐█ ▌▐▌▐█·█▌▐█▌██▪   ▐█.▪▐█· ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  
██. ██ ▐█ ▪▐▌██▐█▌▐█▌.▐▌██▐█▌▐█▄▄▌▐█.█▌    ██ ██▌▐█▌▐█▄█▌▐█▌▐▌ ▐█▌·▐█▌ ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌
▀▀▀▀▀•  ▀  ▀ ▀▀ █▪ ▀█▄▀▪▀▀ █▪ ▀▀▀ ·▀  ▀    ▀▀  █▪▀▀▀ ▀▀▀ .▀▀▀  ▀▀▀ ▀▀▀ ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 


"""

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def run_nmap(flags, ip):
    if not is_valid_ip(ip):
        print(f"Error: '{ip}' is not a valid IP address!")
        return
    cmd = ["nmap"] + flags.split() + [ip]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("\n=== Nmap Scan Results ===")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap: {e}")
    except FileNotFoundError:
        print("Error: 'nmap' is not installed or not found in PATH!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def menu():
    while True:
        print(logo)
        print("\n=== MENU ===")
        print("1. nmap")
        print("2. exit")
        choice = input("\n> ")
        if choice == "1":
            for option in scan_options:
                print(f"{option['id']}. {option['name']} (nmap {option['flags']})")
            scan_choice = input("\n> ")
            selected_option = next((opt for opt in scan_options if opt["id"] == scan_choice), None)
            if selected_option:
                ip = input("\nType an IP address: > ")
                run_nmap(selected_option["flags"], ip)
            else:
                print("Invalid scan choice!")


        elif choice == "2":
            break


menu()