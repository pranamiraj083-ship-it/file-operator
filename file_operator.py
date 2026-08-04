import os
from datetime import datetime

filename = "journal.txt"

while True:
    print("\nWelcome to Personal Journal Manager!")
    print("Please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nUser Input: ")

    match choice:

        case "1":
            print("\nAdd a New Entry")

            entry = input("Enter your journal entry: ")

            file = open(filename, "a")
            file.write(str(datetime.today()) + " - " + entry + "\n")
            file.close()
            print("Entry added successfully!")

        case "2":
            print("\nView All Entries")

            if os.path.exists(filename):
                file = open(filename, "r")
                data = file.read()
                file.close()

                if data == "":
                    print("No journal entries found.")
                else:
                    print("\nYour Journal Entries:")
                    print("------------------------------")
                    print(data)
            else:
                print("Error: The journal file does not exist.Start by adding a new entry.")

        case "3":
            print("\nSearch for an Entry")

            if os.path.exists(filename):
                keyword = input("Enter a keyword or date to search: ")

                file = open(filename, "r")
                lines = file.readlines()
                file.close()

                found = False

                print("\nMatching Entries:")
                print("------------------------------")

                for line in lines:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True

                if found == False:
                    print("No entries were found for the keyword:", keyword)
            else:
                print("Error: The journal file does not exist.Start by adding a new entry.")

        case "4":
            print("\nDelete All Entries")

            if os.path.exists(filename):
                answer = input("Are you sure you want to delete all entries? (yes/no): ")

                if answer.lower() == "yes":
                    os.remove(filename)
                    print("All journal entries have been deleted.")
                else:
                    print("Delete cancelled.")
            else:
                print("No journal entries to delete.")

        case "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break

        case _:
            print("Invalid option. Please select a valid option from the menu.")
