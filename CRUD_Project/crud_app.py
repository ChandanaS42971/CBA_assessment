import csv
import os

FILE_NAME = "students.csv"

# Ensure CSV file exists with headers
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["StudentID", "Name", "Age", "Course", "Grade"])

# Add record
def add_record():
    student_id = input("Enter StudentID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    grade = input("Enter Grade: ")

    # Input validation: Check StudentID is not empty
    if not student_id.strip():
        print("\n❌ StudentID cannot be empty.\n")
        return

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, course, grade])
    print("\n✅ Record added successfully!\n")

# View all records
def view_records():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        records = list(reader)
        if not records:
            print("\n⚠️ No records found.\n")
            return
        print("\n📋 All Student Records:")
        print("-" * 60)
        for r in records:
            print(f"ID: {r['StudentID']} | Name: {r['Name']} | Age: {r['Age']} | Course: {r['Course']} | Grade: {r['Grade']}")
        print("-" * 60)

# Search record by StudentID
def search_record():
    student_id = input("Enter StudentID to Search: ")
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for r in reader:
            if r['StudentID'] == student_id:
                print(f"\n🔎 Found: ID: {r['StudentID']}, Name: {r['Name']}, Age: {r['Age']}, Course: {r['Course']}, Grade: {r['Grade']}\n")
                return
    print("\n❌ Record not found.\n")

# Update record
def update_record():
    student_id = input("Enter StudentID to Update: ")
    updated = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for r in reader:
            if r['StudentID'] == student_id:
                print("\nEnter new values (leave blank to keep unchanged):")
                new_name = input("New Name: ") or r['Name']
                new_age = input("New Age: ") or r['Age']
                new_course = input("New Course: ") or r['Course']
                new_grade = input("New Grade: ") or r['Grade']
                r = {"StudentID": student_id, "Name": new_name, "Age": new_age, "Course": new_course, "Grade": new_grade}
                updated = True
            rows.append(r)

    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["StudentID", "Name", "Age", "Course", "Grade"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Record updated successfully!\n")
    else:
        print("\n❌ Record not found.\n")

# Delete record
def delete_record():
    student_id = input("Enter StudentID to Delete: ")
    deleted = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for r in reader:
            if r['StudentID'] == student_id:
                deleted = True
            else:
                rows.append(r)

    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["StudentID", "Name", "Age", "Course", "Grade"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n🗑️ Record deleted successfully!\n")
    else:
        print("\n❌ Record not found.\n")

# Menu
def menu():
    init_file()
    while True:
        print("\n========= MENU =========")
        print("1. Add Record")
        print("2. View Records")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")
        print("========================")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_record()
        elif choice == '2':
            view_records()
        elif choice == '3':
            search_record()
        elif choice == '4':
            update_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            print("\n👋 Exiting... Data saved in students.csv\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    menu()
