import os
import subprocess as sp
from subprocess import call
import datetime

def display_banner():
    print("**************************************")
    print("*            Linux Toolkit           *")
    print("**************************************")
## create Menu for our program
def menu():
    sp.call("clear", shell=True)
    display_banner()
    
    print("\nHey, what do you want to do?")
    print("""
        1. Disk Management
        2. Execute Linux Commands
        0. Exit
        """)
    while True:
        try:
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Not a valid integer! Please try again...")
    return choice

# Disk Management Menu
def disk_management_menu():
    sp.call("clear", shell=True)
    print("Disk Management")
    print("==============")
    print("""
        1. Help [Steps for creating LVM]
        2. Check how many storages are attached
        3. Create Physical Volume (PV)
        4. Get Physical Volume details
        5. Create Volume Group (VG)
        6. Get Volume Group details
        7. Create Logical Volume (LV)
        8. Format the Logical Volume (LV)
        9. Get Logical Volume details
        10. Mount Logical Volume
        11. Mount the Logical Volume permanently
        12. Set up web configuration 
        0. Go back to main menu
        """)

    while True:
        try:
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Not a valid integer! Please try again...")
    return choice

# Additional Commands Menu
def additional_commands_menu():
    sp.call("clear", shell=True)
    print("Additional Commands")
    print("===================")
    print("""
        1. Display Current Date and Time
        2. Update System Packages
        3. Check System Information
        4. Check Disk Usage
        5. Check Network Connectivity
        b. Go back to main menu
        """)

    while True:
        try:
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Not a valid integer! Please try again...")
    return choice

# Disk Management Functions
# ...

# Additional Commands Functions
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

    while (choice != 0):
        if choice == 1:
            disk_choice = disk_management_menu()
            # Handle disk management functions
            # ...
        elif choice == 2:
            commands_choice = additional_commands_menu()
            # Handle additional commands functions
            if commands_choice == 13:
                display_date_and_time()
            elif commands_choice == 14:
                update_system_packages()

               

