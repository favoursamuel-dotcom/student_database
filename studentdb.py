def calc_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 75:
        return "A"
    elif score >= 65:
        return "B"
    elif score >= 55:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "E"


def database():
    print("=== STUDENT DATABASE ===")

    students = [
        {
            "Id": 1200,
            "Name": "Favour",
            "Age": 20,
            "Score": 80,
            "Grade": "A",
        },
        {
            "Id": 1201,
            "Name": "John",
            "Age": 19,
            "Score": 50,
            "Grade": "D",
        },
        {
            "Id": 1202,
            "Name": "Sarah",
            "Age": 22,
            "Score": 70,
            "Grade": "B",
        },
    ]

    while True:
        print("\nPick one option:")
        print("1. Add student")
        print("2. Display students")
        print("3. Search for student")
        print("4. Update student score")
        print("5. Delete student")
        print("6. Calculate statistics")
        print("7. Exit")

        try:
            option = int(input("Enter option: "))
        except ValueError:
            print("Please enter a number.")
            continue

        match option:

            # ADD STUDENT
            case 1:
                student_id = int(input("Enter student ID: "))

                # Check for duplicate ID
                duplicate = False

                for student in students:
                    if student["Id"] == student_id:
                        duplicate = True
                        break

                if duplicate:
                    print("A student with this ID already exists.")
                    continue

                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                score = int(input("Enter student score: "))

                grade = calc_grade(score)

                if grade == "Invalid":
                    print("Score must be between 0 and 100.")
                    continue

                student = {
                    "Id": student_id,
                    "Name": name,
                    "Age": age,
                    "Score": score,
                    "Grade": grade
                }

                students.append(student)
                print("Student added successfully!")

            # DISPLAY STUDENTS
            case 2:
                if not students:
                    print("No students found.")
                else:
                    print("\n=== ALL STUDENTS ===")

                    for student in students:
                        print(
                            f'ID: {student["Id"]} | '
                            f'Name: {student["Name"]} | '
                            f'Age: {student["Age"]} | '
                            f'Score: {student["Score"]} | '
                            f'Grade: {student["Grade"]}'
                        )

            # SEARCH STUDENT
            case 3:
                search_id = int(input("Enter student ID to search: "))
                found = False

                for student in students:
                    if student["Id"] == search_id:
                        print("\n=== STUDENT FOUND ===")
                        print(student)
                        found = True
                        break

                if not found:
                    print("Invalid ID. Student not found.")

            # UPDATE STUDENT SCORE
            case 4:
                update_id = int(input("Enter student ID: "))
                found = False

                for student in students:
                    if student["Id"] == update_id:
                        new_score = int(input("Enter new score: "))
                        new_grade = calc_grade(new_score)

                        if new_grade == "Invalid":
                            print("Score must be between 0 and 100.")
                            break

                        student["Score"] = new_score
                        student["Grade"] = new_grade

                        print("Student score updated successfully!")
                        found = True
                        break

                if not found:
                    print("Invalid ID. Student not found.")

            # DELETE STUDENT
            case 5:
                delete_id = int(input("Enter student ID to delete: "))
                found = False

                for student in students:
                    if student["Id"] == delete_id:
                        students.remove(student)
                        print("Student deleted successfully!")
                        found = True
                        break

                if not found:
                    print("Invalid ID. Student not found.")

            # STATISTICS
            case 6:
                while True:
                    print("\n=== STATISTICS ===")
                    print("A. Total students")
                    print("B. Average score")
                    print("C. Highest score")
                    print("D. Lowest score")
                    print("E. Back to main menu")

                    pick = input("Pick a letter: ").lower()

                    match pick:
                        case "a":
                            print(f"Total students: {len(students)}")

                        case "b":
                            if students:
                                total = 0

                                for student in students:
                                    total += student["Score"]

                                average = total / len(students)
                                print(f"Average score: {average:.2f}")

                        case "c":
                            scores = []

                            for student in students:
                                scores.append(student["Score"])

                            print(f"Highest score: {max(scores)}")

                        case "d":
                            scores = []

                            for student in students:
                                scores.append(student["Score"])

                            print(f"Lowest score: {min(scores)}")

                        case "e":
                            break

                        case _:
                            print("Invalid option.")

            # EXIT
            case 7:
                print("Goodbye!")
                break

            # DEFAULT
            case _:
                print("Invalid option. Please try again.")


database()