def calc_grade(score):
    if score < 0 or score > 100:
        print("invalid score")
    elif score >= 75:
        return "Grade A"
    elif score >= 65:
        return "Grade B"
    elif score >=55:
        return "Grade C"
    elif score >= 45:
        return "Grade D"
    else:
        return "Grade E"

def database():
    print("This is a student database")
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
    while True :
        print("Pick one option: ")
        print("1. Add student")
        print("2. Display student")
        print("3. Search for student")
        print("4. Update grade")
        print("5. Delete grade")
        print("6. Exit")
        option = int(input("Enter option: "))
        print(f"You entered: {option}")

        if option == 1:
            id = int(input("Enter student id: "))
            name = input("Enter a student name: ")
            age = int(input("Enter a student age: "))
            score = int(input("Enter a score: "))
            grade = calc_grade(score)
            student = {
                    "Id": id,
                    "Name": name,
                    "Age": age,
                    "Score": score,
                     "Grade": grade
                     }
            students.append(student)
        elif option == 2:
            print(students)
        elif option == 3:
            found = False
            print("Enter ID to search ")
            search_Id = int(input("id: "))
            for stu in students:
                if  search_Id == stu["Id"]:
                    print(stu)
                    found = True
            if not found:
                print("Invalid ID")
        elif option == 4:
            print("Enter ID ")
            update_score_id = int(input("id: "))
            new_score = int(input("Enter a new score: "))
            for s in students:
                if update_score_id == s["Id"]:
                    s["Score"] = new_score
                    s["Grade"] = calc_grade(new_score)
                    print(students)
        elif option == 5:
            user_id = int(input("Enter id to delete: "))
            found = False
            for stud in students:
                if user_id == stud["Id"]:
                    students.remove(stud)
                    print("Student deleted")
                    print(students)
                    found = True
                    break
                    
                if not found:
                    print("Invalid ID.")
        elif option == 7:
            break
        else:
            print("Invalid option. Please try again.")
database()