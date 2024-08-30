def insert_student(student_id, name, mobile, address, deposit):
    with open('MessData.txt', 'a') as f:
        f.write(f"{student_id},{name},{mobile},{address},{deposit},0\n")

def update_meals(student_id, meals):
    with open('MessData.txt', 'r') as f:
        data = f.readlines()

    updated_data = []
    for line in data:
        if line.startswith(student_id):
            parts = line.strip().split(',')
            parts[5] = str(int(parts[5]) + meals)
            updated_data.append(','.join(parts) + '\n')
        else:
            updated_data.append(line)

    with open('MessData.txt', 'w') as f:
        f.writelines(updated_data)

def check_balance(student_id):
    with open('MessData.txt', 'r') as f:
        data = f.readlines()

    for line in data:
        if line.startswith(student_id):
            parts = line.strip().split(',')
            return float(parts[4])

    return None

def update_balance(student_id, amount):
    with open('MessData.txt', 'r') as f:
        data = f.readlines()

    updated_data = []
    for line in data:
        if line.startswith(student_id):
            parts = line.strip().split(',')
            parts[4] = str(float(parts[4]) + amount)
            updated_data.append(','.join(parts) + '\n')
        else:
            updated_data.append(line)

    with open('MessData.txt', 'w') as f:
        f.writelines(updated_data)

def get_meals_count(student_id):
    with open('MessData.txt', 'r') as f:
        data = f.readlines()

    for line in data:
        if line.startswith(student_id):
            parts = line.strip().split(',')
            return int(parts[5])

    return None

def get_student_status(student_id):
    with open('MessData.txt', 'r') as f:
        data = f.readlines()

    for line in data:
        if line.startswith(student_id):
            parts = line.strip().split(',')
            return {
                "ID": parts[0],
                "Name": parts[1],
                "Mobile": parts[2],
                "Address": parts[3],
                "Balance": parts[4],
                "Meals": parts[5]
            }

    return None

def display_all_students():
    with open('MessData.txt', 'r') as f:
        data = f.readlines()

    for line in data:
        parts = line.strip().split(',')
        print(f"ID:{parts[0]}, Name: {parts[1]}, Mobile: {parts[2]}, Address: {parts[3]}, Deposit: {parts[4]}, Meals: {parts[5]}")

def main():
    print("Welcome to Abdullah Chatrabash Mess Management System")

    while True:
        print("\nOptions:")
        print("1. Add new student")
        print("2. Update meals for a student")
        print("3. Check balance")
        print("4. Check meals count")
        print("5. Get student status")
        print("6. Display all students")
        print("7. Update balance for a student")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            mobile = input("Enter mobile number: ")
            address = input("Enter address (city): ")
            deposit = input("Enter initial deposit amount: ")
            insert_student(student_id, name, mobile, address, deposit)
            print(f"Student added successfully! Student ID: {student_id}")

        elif choice == '2':
            student_id = input("Enter student ID: ")
            meals = int(input("Enter number of meals to add: "))
            update_meals(student_id, meals)
            print("Meals updated successfully!")

        elif choice == '3':
            student_id = input("Enter student ID: ")
            balance = check_balance(student_id)
            if balance is not None:
                print(f"Current balance for student {student_id}: {balance}")
            else:
                print("Student not found.")

        elif choice == '4':
            student_id = input("Enter student ID: ")
            meals = get_meals_count(student_id)
            if meals is not None:
                print(f"Total meals for student {student_id} this month: {meals}")
            else:
                print("Student not found.")

        elif choice == '5':
            student_id = input("Enter student ID: ")
            status = get_student_status(student_id)
            if status:
                print("Student Status:")
                for key, value in status.items():
                    print(f"{key}: {value}")
            else:
                print("Student not found.")

        elif choice == '6':
            display_all_students()

        elif choice == '7':
            student_id = input("Enter student ID: ")
            amount = float(input("Enter amount to add (use negative for deduction): "))
            update_balance(student_id, amount)
            print("Balance updated successfully!")

        elif choice == '0':
            print("Thank you for using Abdullah Chatrabash Mess Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
