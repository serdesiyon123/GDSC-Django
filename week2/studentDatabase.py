student_info = {

}


def add_students(name, age, grade, sex, networth):
    student_info[name] = {
        "age": age,
        "grade": grade,
        "sex": sex,
        "networth": networth
    }


def remove_students(name):
    del student_info[name]


def view_students(name):
    print(student_info[name])


add_students("Musk", 48, "A", "Male", 205)
add_students("Zuckerberg", 38, "A", "Male", 102)
add_students("Nadella", 56, "A", "Male", 2)
add_students("Gates", 64, "A", "Male", 110)
add_students("Bezos", 62, "A", "Male", 159)
add_students("Lovelace", 120, "A", "Female", 0.5)
add_students("Altman", 120, "A", "Male", 4)

view_students("Bezos")

remove_students("Altman")

print(student_info)
