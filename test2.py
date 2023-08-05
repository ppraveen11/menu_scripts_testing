import os
import subprocess as sp
import datetime

# ... (The rest of the code remains the same)

def additional_commands_menu():
    sp.call("clear", shell=True)
    print("Additional Commands")
    print("===================")
    print("""
        13. Display Current Date and Time
        14. Update System Packages
        15. Check System Information
        16. Check Disk Usage
        17. Check Network Connectivity
        0. Go back to main menu
        """)

    while True:
        try:
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Not a valid integer! Please try again...")
    return choice

# Disk Management Functions (Add your disk management functions here)
# ...

def display_date_and_time():
    current_datetime = datetime.datetime.now()
    print("Current Date and Time:", current_datetime)

def update_system_packages():
    sp.call("clear", shell=True)
    sp.call("sudo apt update && sudo apt upgrade -y", shell=True)
    print("System packages have been updated.")

def check_system_information():
    sp.call("clear", shell=True)
    sp.call("uname -a", shell=True)
    sp.call("lsb_release -a", shell=True)

def check_disk_usage():
    sp.call("clear", shell=True)
    sp.call("df -h", shell=True)

def check_network_connectivity():
    sp.call("clear", shell=True)
    sp.call("ping -c 5 google.com", shell=True)

if __name__ == "__main__":
    print("Welcome To Python script for LVM")
    choice = menu()

    while choice != 0:
        if choice == 1:
            disk_choice = disk_management_menu()
            # Handle disk management functions
            # ...
        elif choice == 2:
            commands_choice = additional_commands_menu()
            if commands_choice == 13:
                display_date_and_time()
            elif commands_choice == 14:
                update_system_packages()
            elif commands_choice == 15:
                check_system_information()
            elif commands_choice == 16:
                check_disk_usage()
            elif commands_choice == 17:
                check_network_connectivity()

        choice = menu()

    print("Goodbye! Thank you for using Linux Toolkit.")

