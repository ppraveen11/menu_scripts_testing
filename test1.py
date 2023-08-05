import os
import subprocess as sp
import datetime

def display_banner():
    print("**************************************")
    print("*            Linux Toolkit           *")
    print("**************************************")

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

def additional_commands_menu():
    sp.run("clear", shell=True)
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
    sp.run("clear", shell=True)
    sp.run("sudo apt update && sudo apt upgrade -y", shell=True)
    print("System packages have been updated.")

def check_system_information():
    sp.run("clear", shell=True)
    sp.run("uname -a", shell=True)
    sp.run("lsb_release -a", shell=True)

def check_disk_usage():
    sp.run("clear", shell=True)
    sp.run("df -h", shell=True)

def check_network_connectivity():
    sp.run("clear", shell=True)
    sp.run("ping -c 5 google.com", shell=True)

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

