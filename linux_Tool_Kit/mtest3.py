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
# ... (The rest of the code remains the same)

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

# Disk Management Functions
def create_physical_volume():
    # Add your code here to create a physical volume (PV)
    pass

def get_physical_volume_details():
    # Add your code here to get physical volume (PV) details
    pass

def create_volume_group():
    # Add your code here to create a volume group (VG)
    pass

# ... (Add more disk management functions as needed)


# Additional Commands Menu
def additional_commands_menu():
        sp.call("clear", shell=True)
        print("Additional Commands")
        print("===================")
        print("""
            1. Display Date and Time
            2. Update System Packages
            3. Check System Information
            4. Check Disk Usage
            5. Check Network Connectivity
            0. Go back to main menu
            """)

        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Not a valid integer! Please try again...")
        return choice

# Additional Commands Functions
def display_date_and_time():
    now = datetime.datetime.now()
    print("Current date and time:", now)
    print("hello")

def update_system_packages():
    sp.run("sudo apt-get update && sudo apt-get upgrade -y", shell=True)


def check_system_information():
   #sp.call("uname -a", shell=True)
    result = sp.call(["uname", "-a"], capture_output=True, text=True)
    print("System information:")
    print(result.stdout)

def check_disk_usage():
    sp.call("df -h", shell=True)

def check_network_connectivity():
    sp.call("ping -c 4 www.google.com", shell=True)

if __name__ == "__main__":
    print("Welcome To Python script for LVM")
    choice = menu()

    while (choice != 0):
        if choice == 1:
            disk_choice = disk_management_menu()
            if disk_choice == 1:
                # Display steps for creating LVM (add your steps here)
                print("Steps for creating LVM:")
                print("1. Step 1")
                print("2. Step 2")
                # ...

            elif disk_choice == 2:
                # Check how many storages are attached (add your code here)
                pass

            elif disk_choice == 3:
                create_physical_volume()

            elif disk_choice == 4:
                get_physical_volume_details()

            elif disk_choice == 5:
                create_volume_group()

            # ... (Add more cases for other disk management options)

        elif choice == 2:
            commands_choice = additional_commands_menu()
            # Handle additional commands functions
            if commands_choice == 1:
                 display_date_and_time()

            elif commands_choice == 2:
                update_system_packages()

            elif commands_choice == 3:
                check_system_information()

            elif commands_choice == 4:
                check_disk_usage()

            elif commands_choice == 5:
                check_network_connectivity()

        #choice = menu()

    print("Goodbye! Thank you for using Linux Toolkit.")

