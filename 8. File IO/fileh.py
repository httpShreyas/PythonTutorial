# ======================================================
# Simple File Handling Program in Python
# ======================================================
# This program demonstrates basic file handling operations
# such as creating, writing, reading, copying, counting, and deleting files.
# It uses Python’s built-in open(), read(), write(), seek(), tell(), and os.remove() functions.

import os  # Importing 'os' module for performing delete operation on files

while True:
    # Displaying menu options to the user
    print("\n===== FILE HANDLING MENU =====")
    print("1. Create a new file")
    print("2. Write to an existing file (Append mode)")
    print("3. Overwrite existing content in a file")
    print("4. Read the contents of a file")
    print("5. Find and change file cursor position")
    print("6. Count number of characters, words & lines")
    print("7. Copy contents to another file")
    print("8. Delete a file")
    print("0. Exit")

    # Taking user input for the operation
    choice = int(input("\nEnter your choice (0-8): "))

    # ------------------------------------------------------
    # 0. Exit
    # ------------------------------------------------------
    if choice == 0:
        print("Exiting program. Goodbye!")
        break

    # ------------------------------------------------------
    # 1. Create a new file
    # ------------------------------------------------------
    elif choice == 1:
        fname = input("Enter file name: ")
        try:
            f = open(fname, "x")
            print("File created successfully!")
            f.close()
        except FileExistsError:
            print("Error: File already exists.")

    # ------------------------------------------------------
    # 2. Write to an existing file (Append mode)
    # ------------------------------------------------------
    elif choice == 2:
        fname = input("Enter file name: ")
        try:
            with open(fname, "a") as f:
                data = input("Enter text to write to the file: ")
                f.write(data + "\n")
                print("Data written successfully!")
        except FileNotFoundError:
            print("Error: File not found.")

    # ------------------------------------------------------
    # 3. Overwrite the existing content in the file
    # ------------------------------------------------------
    elif choice == 3:
        fname = input("Enter file name: ")
        with open(fname, "w") as f:
            data = input("Enter new content: ")
            f.write(data + "\n")
            print("File content overwritten!")

    # ------------------------------------------------------
    # 4. Read the contents of a file
    # ------------------------------------------------------
    elif choice == 4:
        fname = input("Enter file name: ")
        try:
            with open(fname, "r") as f:
                print("\nFile contents:\n")
                print(f.read())
        except FileNotFoundError:
            print("Error: File not found.")

    # ------------------------------------------------------
    # 5. Find and change the file cursor position
    # ------------------------------------------------------
    elif choice == 5:
        fname = input("Enter file name: ")
        try:
            with open(fname, "r") as f:
                print("Current cursor position:", f.tell())
                pos = int(input("Enter new cursor position (byte offset): "))
                f.seek(pos)
                print("Cursor moved to:", f.tell())
                print("Data from new position:\n", f.read())
        except FileNotFoundError:
            print("Error: File not found.")

    # ------------------------------------------------------
    # 6. Count number of characters, words, and lines
    # ------------------------------------------------------
    elif choice == 6:
        fname = input("Enter file name: ")
        try:
            with open(fname, "r") as f:
                data = f.read()
                lines = data.split('\n')
                words = data.split()
                print("No. of characters:", len(data))
                print("No. of words:", len(words))
                print("No. of lines:", len(lines))
        except FileNotFoundError:
            print("Error: File not found.")

    # ------------------------------------------------------
    # 7. Copy contents from one file to another
    # ------------------------------------------------------
    elif choice == 7:
        src = input("Enter source file name: ")
        dst = input("Enter destination file name: ")
        try:
            with open(src, "r") as f1, open(dst, "w") as f2:
                f2.write(f1.read())
                print("File copied successfully!")
        except FileNotFoundError:
            print("Error: Source file not found.")

    # ------------------------------------------------------
    # 8. Delete a file
    # ------------------------------------------------------
    elif choice == 8:
        fname = input("Enter file name to delete: ")
        if os.path.exists(fname):
            os.remove(fname)
            print("File deleted successfully!")
        else:
            print("Error: File not found.")

    else:
        print("Invalid choice! Please enter a number between 0 and 8.")
