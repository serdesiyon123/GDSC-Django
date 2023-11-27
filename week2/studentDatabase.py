studentInfo = {

}


def addStudents (name, age, grade,sex,networth):
    studentInfo[name] = {  
        "age": age,
        "grade": grade,
        "sex": sex,
        "networth": networth
    }

def removeStudents(name):
    del studentInfo[name]
      
def viewStudents(name):
    print(studentInfo[name])


addStudents("Musk",48, "A", "Male" , 205) 
addStudents("Zuckerberg",38, "A", "Male" ,102 ) 
addStudents("Nadella",56, "A", "Male" , 2 ) 
addStudents("Gates",64, "A", "Male", 110 ) 
addStudents("Bezos",62, "A", "Male" , 159 ) 
addStudents("Lovelace",120, "A", "Female", 0.5 ) 
addStudents("Altman",120, "A", "Male", 4 ) 

viewStudents("Bezos")

removeStudents("Altman")

print(studentInfo)
