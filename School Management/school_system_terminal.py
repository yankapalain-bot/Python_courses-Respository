"""
SCHOOL MANAGEMENT SYSTEM - STUDENT TEMPLATE
===========================================
Instructions: Fill in the missing code in the methods marked with TODO.
Follow the comments to complete each class.
"""
import json

# ============================================
# Challenge : TEACHER CLASS
# ============================================

class Teacher:

    def __init__(self, teacher_id, name, subjects):
        self.teacher_id = teacher_id
        self.name = name
        self.subjects = subjects

    def display_info(self):
        print(f"ID: {self.teacher_id}   | Name: {self.name} | Subects: {', '.join(self.subjects)}")
    
    def __str__(self):
        return f"Teacher(ID: {self.teacher_id}, Name: {self.name}, Subjects: {self.subjects})"



# ============================================
# STEP 1: STUDENT CLASS
# ============================================

class Student:
    """
    TODO: Create a class to represent a student.
    
    Instructions:
    1. Create the __init__ method with parameters: self, student_id, name, grade_level
    2. Store these as instance variables
    3. Create a display_info method that prints student details
    4. Create __str__ method for string representation
    """
    
    def __init__(self, student_id, student_name, grade_level):
        # TODO: Initialize the attributes
        self.student_id = student_id
        self.student_name = student_name
        self.grade_level = grade_level
        self.attendance = {}        #{class_id: [True, False]}
        self.schedule = {}          #{"Monday": ["Math", "Science]"}

    
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "student_name": self.student_name,
            "grade_level": self.grade_level,
            "attendance": self.attendance,
            "schedule": self.schedule
        }
    
    def display_info(self):
        # TODO: Print student information in a formatted way
        # Example: "ID: 1001 | Name: Alice | Grade: 10"
        print(f"ID:  {self.student_id} |  Name:  {self.student_name}  |  Grade:  {self.grade_level}")
        
    
    def __str__(self):
        # TODO: Return a string representation of the student
        # Example: "Student(ID: 1001, Name: Alice, Grade: 10)"
        return f"\n Student(ID: {self.student_id}, Name: {self.student_name}, Grade: {self.grade_level} )"
        


# ============================================
# STEP 2: CLASS CLASS (School Course)
# ============================================

class Class:
    """
    TODO: Create a class to represent a school course.
    
    Instructions:
    1. Initialize with class_id, class_name, teacher
    2. Create an empty list for enrolled_students
    3. Create methods to add/remove students
    4. Create method to list all students in the class
    """
    
    def __init__(self, class_id, class_name, teacher):
        # TODO: Initialize attributes and an empty list for enrolled students
        self.class_id = class_id
        self.class_name = class_name
        self.class_teacher = teacher
        self.enrolled_students = []

    
    def add_student(self, student):
        # TODO: Add a student to the enrolled_students list
        # Check if student is already enrolled to avoid duplicates
        # Print success or warning message
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"\n✅ The student: {student.student_name} added successfully")
        else:
            print(f"\n⚠️ The student: {student.student_name} is already enroll in class")
    
    def remove_student(self, student):
        # TODO: Remove a student from the enrolled_students list
        # Check if student exists before removing
        # Print appropriate messages
        if student in self.enrolled_students:
            confirm = input(f"\nAre you sure you want to delete student '{student.student_name}'? (y/n)")
            if confirm == 'y':
                self.enrolled_students.remove(student)
                print(f"\n✅ The student: {student.student_name} deleted successfully")
            elif confirm == 'n':
                pass
        else:
            print("\n❌ Sorry - We can not delete an unrolled student")

                  
    def list_students(self):
        # TODO: Display all students enrolled in this class
        # Handle case when no students are enrolled
        if not self.enrolled_students:
            print("\n❌ Sorry - you should enroll student first")
        else:
            print(f"Class - {self.class_name} - Have Number of enrolled students: {len(self.enrolled_students)}")            
            for i, item in enumerate(self.enrolled_students, 1):
                #item.display_info()
                print(f"{i}. ID:  {item.student_id} |  Name: {item.student_name} ")

    
    def __str__(self):
        # TODO: Return string representation of the class
        # Include class ID, name, teacher, and number of students
        return f"Class ID: {self.class_id}  | Name: {self.class_name} | Teacher: {self.class_teacher}   | Number of enrolled students: {len(self.enrolled_students)}"
    


# ============================================
# STEP 3: GRADE CLASS
# ============================================

class Grade:

    """
    TODO: Create a class to represent a student's grade in a class.
    
    Instructions:
    1. Initialize with grade_id, student, class_obj, score
    2. Create a method to convert numerical score to letter grade
    3. Create a method to display grade information
    """
    
    def __init__(self, grade_id, student, class_obj, score):
        # TODO: Initialize all attributes
        self.grade_id = grade_id
        self.student = student
        self.class_obj = class_obj
        self.score = score
        self.grade_letter = self.get_letter_grade()
    
    def get_letter_grade(self):
        """
        Convert numerical score to letter grade.
        Use this scale:
        90-100: A
        80-89: B
        70-79: C
        60-69: D
        Below 60: F
        """
        # TODO: Return the appropriate letter grade based on self.score
        if self.score < 0 or self.score > 100:
            print("Score should be between [1 - 100]")
        if self.score >= 90:
            return "A"
        
        if self.score >= 80:
            return "B"
        
        if self.score >= 70:
            return "C"
        
        if self.score >= 60:
            return "D"
        
        if self.score < 60:
            return "F"
        
            
    def display_grade(self):
        # TODO: Print grade information including letter grade
        # Example: "Grade ID: 301 | Student: Alice | Class: Math | Score: 95 | Letter: A"        
        print(f"\nGrade ID: {self.grade_id} | Student: {self.student.student_name} | Class: {self.class_obj.class_name} | Score: {self.score} | Letter: {self.grade_letter}")
    
    def __str__(self):
        # TODO: Return string representation of the grade
        # Include letter grade in the string        
        return f"\nGrade ID: {self.grade_id} | Student: {self.student.student_name} | Class: {self.class_obj.class_name} | Score: {self.score} | Letter: {self.grade_letter}"
    
    def get_gpa_points(self):
        mapping = {
            "A": 4.0,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }
        return mapping.get(self.grade_letter, 0.0)

        

# ============================================
# STEP 4: SCHOOL MANAGEMENT SYSTEM
# ============================================

class School:
    """
    TODO: Create the main school management class.
    
    This class will manage all students, classes, and grades.
    """
    
    def __init__(self, school_name):
        # TODO: Initialize school name and empty lists for students, classes, and grades
        self.school_name = school_name
        self.students = []
        self.classes = []
        self.grades = []
        self.teachers = []
    
    # ---------- STUDENT MANAGEMENT ----------
    
    def add_student(self, student_id, name, grade_level):
        # TODO: Create a new Student object and add to students list
        # Check if student_id already exists
        # Return the new student or None if failed
        check =False
        for item in self.students:
            if student_id == item.student_id:
                check = True                                
                
        if check == False:
            student = Student(student_id, name, grade_level)
            self.students.append(student)
            print(f"\n✅ New student -ID: {student.student_id} : successfuly added")
            return student        
        else:
            print(f"\n❌  student -ID: {student.student_id} : Already exist in {self.school_name}")
            return None                
            
    
    def find_student(self, student_id)->Student:
        # TODO: Find and return a student by ID
        # Return None if not found
        founded_student = None
        for item in self.students:
            if item.student_id == student_id:
                founded_student = item 
                return founded_student
            
        return None            
    
    
    def list_all_students(self):
        # TODO: Display all students in the school
        # Handle empty list case
        print("="*40)
        print(f"\n {self.school_name} : List of all students: {len(self.students)}")
        print("="*40)
        for i, item in enumerate(self.students):            
            print(f"{i}")
            item.display_info()
           
        print("="*40)
    

    def find_students_by_name(self, name):

        results = []
        for item in self.students:
            if item.student_name.lower() == name.lower():
                results.append(item)
        
        if not results:
            print(f"Sorry, No students found with this name : {name}")
            return None
        else:
            print("="*40)
            print(f"\n 🔍 {self.school_name} : List of all students with name: {name} --- {len(self.students)} - founded")
            print("="*40)
            for student in results:
                student.display_info()        

        return results
    

    def mark__attendance(self, student_id, class_id, present=True):
        student = self.find_student(student_id)
        if not student:
            return
        
        if class_id not in student.attendance:
            student.attendance[class_id] = []
        
        student.attendance[class_id].append(present)

    
    def attendance_percentage(self, student_id, class_id):
        student = self.find_student(student_id)
        if not student:
            return None
        
        records = student.attendance.get(class_id, [])

        if not records:
            return 0
        
        percentage = (sum(records) / len(records)) * 100
        print(f"Attendance: {percentage:.2f}%")
        return percentage
    

    def add_schedule(self, student_id, day, class_name):
        student = self.find_student(student_id)
        if not student:
            return None
        
        if day not in student.schedule:
            student.schedule[day] = []
        
        student.schedule[day].append(class_name)
    

    def view_schedule(self, student_id):
        student = self.find_student(student_id)
        if not student:
            return 
        
        print(f"\n📅 Schedule for {student.student_name}")
        for day, classes in student.schedule.items():
            print(f"{day}:  {', '.join(classes)}")
        
        



    # ---------- TEACHER MANAGEMENT ----------
    
    def add_teacher(self, teacher_id, name, subjects):
        teacher = Teacher(teacher_id, name, subjects)
        self.teachers.append(teacher)
        return teacher
    
    
   

    # ---------- CLASS MANAGEMENT ----------
    
    def add_class(self, class_id, class_name, teacher):
        # TODO: Create a new Class object and add to classes list
        # Check if class_id already exists
        # Return the new class or None if failed
        check = False
        class_use = Class(class_id, class_name, teacher)
        for i, item in enumerate(self.classes):
            if item.class_id == class_use.class_id:
                check = True

        if check:
            print(f"❌ Class with ID {class_id} already exists!")
            return None
        else:
            self.classes.append(class_use)
            print(f"✅ Class {class_name} added successfully!")
            return class_use       
            
            
    def find_class(self, class_id)->Class:
        # TODO: Find and return a class by ID
        # Return None if not found
        founded = None
        for item in self.classes:
            if item.class_id == class_id:
                founded = item
        
        if not founded:
            return None             
        else:
            return founded              
         
    
    def list_all_classes(self):
        # TODO: Display all classes in the school
        # Include number of students enrolled in each class
        print("="*40)
        print(f"{self.school_name} School - List aff class")
        print("="*40)
        if not self.classes:
            return
        else:
            for i, item in enumerate(self.classes):
                print(f"{i}. Class ID: {item.class_id}  | Name: {item.class_name} | Teacher: {item.class_teacher}")

    
    def calculate_class_average(self, class_id):
        clace = self.find_class(class_id)
        if not clace:
            return None
        
        class_grade = []
        for item in self.grades:
            if item.class_obj.class_id == class_id:
                class_grade.append(item.score)
        
        if not class_grade:
            print("Sorry, Noo grade for this class")
            return None
        
        moy = sum(class_grade) / len(class_grade)
        print(f"Average for {clace.class_name}: {moy:.2f}")
        return moy
     
     # ---------- ENROLLMENT MANAGEMENT ----------
    
    def enroll_student_in_class(self, student_id, class_id):
        # TODO: Enroll a student in a class
        # Find both student and class first
        # Use the class's add_student method
        # Return True if successful, False otherwise
        student = self.find_student(student_id)
        clace = self.find_class(class_id)
        if not student:
            return False
        
        if not clace:
            return False
        
        clace.add_student(student) 
        return True
        
    
    # ---------- GRADE MANAGEMENT ----------
    
    def add_grade(self, grade_id, student_id, class_id, score):
        # TODO: Add a grade for a student in a class
        # Verify student and class exist
        # Verify student is enrolled in the class
        # Check if grade_id already exists
        # Create and add new Grade object
        student = self.find_student(student_id)
        if not student:
            return None
        
        class_obj = self.find_class(class_id)
        if not class_obj:
            return None
        
        # Check if student is enrolled in the class
        if student not in class_obj.enrolled_students:
            print(f"❌ {student.student_name} is not enrolled in {class_obj.class_name}!")
            return None
        
        # Check if grade ID already exists
        for grade in self.grades:
            if grade.grade_id == grade_id:
                print(f"❌ Grade with ID {grade_id} already exists!")
                return None
        
        # Create and add grade
        new_grade = Grade(grade_id, student, class_obj, score)
        self.grades.append(new_grade)
        print(f"✅ Grade added for {student.student_name} in {class_obj.class_name}: {score}")
        return new_grade
        
       
    
    def list_grades_for_student(self, student_id):
        # TODO: Display all grades for a specific student
        student = self.find_student(student_id)
        if not student:
            return
        
        
        print("="*40)
        print(f" All grades of student {student.student_id} - {student.student_name}")
        print("="*40)
        # i = 1
        # student_grad_list = []      
        # for item in self.grades:
        #     if item.student.student_id == student_id:
        #         student_grad_list.append(item)

        student_grad_list = [g for g in self.grades if g.student.student_id == student_id]

        if not student_grad_list:
            print("❌ Actualy, No grades recorded for this student")
        else:
            for grad in student_grad_list:
                grad.display_grade()
                    
    
    def list_grades_for_class(self, class_id):
        # TODO: Display all grades for a specific class
        clace = self.find_class(class_id)
        if not clace:
            return
        
        print("="*40)
        print(f" All grades of student {clace.class_id} - {clace.class_name}")
        print("="*40)
        
        # grad_list = []
        # for item in self.grades:
        #     if item.class_obj.class_id == class_id:
        #         grad_list.append(item)
        grad_list = [g for g in self.grades if g.class_obj.class_id == class_id]

        if not grad_list:
            print("Sorry, no recorded grades")
        else:
            for grad in grad_list:
                grad.display_grade()
                #grad.display_grade()
        
    
    def calculate_student_average(self, student_id):
        # TODO: Calculate and display average grade for a student
        # Return the average or None if no grades
        student = self.find_student(student_id)
        if not student:
           return None
       
        # student_grad_list = []
        # for item in self.grades:
        #    if item.student.student_id == student_id:
        #        student_grad_list.append(item)

        
        student_grad_list = [g for g in self.grades if g.student.student_id == student_id]

        if not student_grad_list:
           print("SORRY")
           return None     

        somme = sum(grad.score for grad in student_grad_list)     
        moy = somme / len(student_grad_list)  
        print(f"The average grade fromt student - {student.student_name} is : {moy}")
        return moy
    

    def calculate_gpa(self, student_id):
        
        #student_grades = [item for item in self.grades if item.student.student_id == student_id]

        student_grades = []
        for item in self.grades:
            if item.student.student_id == student_id:
                student_grades.append(item)
        
        if not student_grades:
            return None
        
        #total = sum(item.get_gpa_points() for item in student_grades)
        total = 0
        for item in student_grades:
            total += item.get_gpa_points()
        
        gpa = total / len(student_grades)

        print(f"GPA: {gpa:.2f}")
        return gpa 
    

    #
    #  Generate Report Card
    #
    def generate_report_card(self, student_id):
        student = self.find_student(student_id)
        if not student:
            return
        
        print("\n" + "="*40)
        print(f"📄 REPORT CARD - Student: {student.student_name}")
        print("="*40)

        student_grades = []
        for item in self.grades:
            if item.student.student_id == student_id:
                student_grades.append(item)
        
        for data in student_grades:
            print(f"{data.class_obj.class_name}: {data.score} - grade ({data.grade_letter})")
        
        moy = self.calculate_student_average(student_id)
        print(f"\nAverage: {moy:.2f}")
    

    ###################################################
    # SAVE and LOAD DATA from file
    ###################################################
     
    
    def save_data(self, filename="school_data.json"):
        data = {
            "students": [s.to_dict() for s in self.students],
            "classes": [
                {
                    "class_id": c.class_id,
                    "class_name": c.class_name,
                    "teacher": c.class_teacher,
                    "students": [s.student_id for s in c.enrolled_students]
                }
                for c in self.classes
            ],
            "grades": [
                {
                    "grade_id": g.grade_id,
                    "student_id": g.student.student_id,
                    "class_id": g.class_obj.class_id,
                    "score": g.score
                }
                for g in self.grades
            ]
        }

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        
        print("✅ Data saved successfully")
    


    def load_data(self, filename="school_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            # Load students
            for s in data["students"]:
                student = Student(
                    s["student_id"],
                    s["student_name"],
                    s["grade_level"]
                )            
                # restore extra attributes
                student.attendance = s.get("attendance", {})
                student.schedule = s.get("schedule", {})

                self.students.append(student)

            # Load classes
            for c in data["classes"]:
                class_obj = Class(c["class_id"], c["class_name"], c["teacher"])
                self.classes.append(class_obj)

            # Re-link students to classes
            for c_data, class_obj in zip(data["classes"], self.classes):
                for student_id in c_data["students"]:
                    student = self.find_student(student_id)
                    if student:
                        class_obj.enrolled_students.append(student)

            # Load grades
            for g in data["grades"]:
                student = self.find_student(g["student_id"])
                class_obj = self.find_class(g["class_id"])
                if student and class_obj:
                    self.grades.append(Grade(g["grade_id"], student, class_obj, g["score"]))

            print("✅ Data loaded successfully")

        except FileNotFoundError:
            print("⚠️ No saved data found")
        




####################################################################################
#       MAIN PART and DATA
#####################################################################################

def main():
    """
    Main function to run the School Management System.
    """

    def seed_data(school):
        print("\n🌱 Seeding full test data...\n")
        
        # =========================
        # STUDENTS
        # =========================
        s1 = school.add_student(1001, "Alice Johnson", 10)
        s2 = school.add_student(1002, "Bob Smith", 11)
        s3 = school.add_student(1003, "Charlie Brown", 9)
        s4 = school.add_student(1004, "Diana Prince", 12)
        s5 = school.add_student(1005, "Evan Wright", 10)

        # =========================
        # TEACHERS
        # =========================
        t1 = school.add_teacher(501, "Dr. Smith", ["Mathematics"])
        t2 = school.add_teacher(502, "Ms. Davis", ["Science"])
        t3 = school.add_teacher(503, "Mr. Johnson", ["English"])
        t4 = school.add_teacher(504, "Mrs. Williams", ["History"])

        # =========================
        # CLASSES
        # =========================
        c1 = school.add_class(201, "Mathematics", t1.name)
        c2 = school.add_class(202, "Science", t2.name)
        c3 = school.add_class(203, "English Literature", t3.name)
        c4 = school.add_class(204, "History", t4.name)

        # =========================
        # ENROLLMENTS
        # =========================
        school.enroll_student_in_class(1001, 201)
        school.enroll_student_in_class(1001, 202)

        school.enroll_student_in_class(1002, 201)
        school.enroll_student_in_class(1002, 203)

        school.enroll_student_in_class(1003, 201)
        school.enroll_student_in_class(1003, 204)

        school.enroll_student_in_class(1004, 202)
        school.enroll_student_in_class(1004, 203)

        school.enroll_student_in_class(1005, 201)
        school.enroll_student_in_class(1005, 204)

        # =========================
        # GRADES
        # =========================
        school.add_grade(301, 1001, 201, 95)
        school.add_grade(302, 1001, 202, 88)

        school.add_grade(303, 1002, 201, 78)
        school.add_grade(304, 1002, 203, 92)

        school.add_grade(305, 1003, 201, 85)
        school.add_grade(306, 1003, 204, 90)

        school.add_grade(307, 1004, 202, 96)
        school.add_grade(308, 1004, 203, 89)

        school.add_grade(309, 1005, 201, 82)
        school.add_grade(310, 1005, 204, 75)

        # =========================
        # ATTENDANCE
        # =========================
        school.mark__attendance(1001, 201, True)
        school.mark__attendance(1001, 201, False)
        school.mark__attendance(1001, 201, True)

        school.mark__attendance(1002, 201, True)
        school.mark__attendance(1002, 201, True)

        school.mark__attendance(1003, 204, False)
        school.mark__attendance(1003, 204, True)

        # =========================
        # SCHEDULES
        # =========================
        school.add_schedule(1001, "Monday", "Mathematics")
        school.add_schedule(1001, "Monday", "Science")
        school.add_schedule(1001, "Wednesday", "English Literature")

        school.add_schedule(1002, "Tuesday", "Mathematics")
        school.add_schedule(1002, "Thursday", "English Literature")

        school.add_schedule(1003, "Monday", "History")
        school.add_schedule(1004, "Friday", "Science")
        school.add_schedule(1005, "Wednesday", "Mathematics")

        print("✅ Data seeding completed!\n")
    
    school = School("Python High School")

    # First run → seed data
    #seed_data(school)
    #school.save_data()

    

    # LOAD DATA
    school.load_data()

   


####################################################################################
#      ===== INTERACTIVE MENU =====
#####################################################################################

    while True:
        print("\n" + "=" * 60)
        print("🏫 MAIN MENU")
        print("=" * 60)
        print("1. List all students")
        print("2. List all classes")
        print("3. Add a new student")
        print("4. Add a new class")
        print("5. Enroll student in class")
        print("6. Add a grade")
        print("7. View student grades")
        print("8. View class grades")
        print("9. Calculate student average")
        print("0. Exit")
        print("-" * 60)
        
        choice = input("Enter your choice (0-9): ")
        
        if choice == "1":
            school.list_all_students()
        
        elif choice == "2":
            school.list_all_classes()
        
        elif choice == "3":
            print("\n➕ Add New Student")
            try:
                student_id = int(input("Enter student ID: "))
                name = input("Enter student name: ")
                grade_level = int(input("Enter grade level (9-12): "))
                school.add_student(student_id, name, grade_level)
            except ValueError:
                print("❌ Invalid input! Please enter numbers for ID and grade level.")
        
        elif choice == "4":
            print("\n➕ Add New Class")
            try:
                class_id = int(input("Enter class ID: "))
                class_name = input("Enter class name: ")
                teacher = input("Enter teacher name: ")
                school.add_class(class_id, class_name, teacher)
            except ValueError:
                print("❌ Invalid input! Please enter a number for class ID.")
        
        elif choice == "5":
            print("\n📝 Enroll Student")
            try:
                student_id = int(input("Enter student ID: "))
                class_id = int(input("Enter class ID: "))
                school.enroll_student_in_class(student_id, class_id)
            except ValueError:
                print("❌ Invalid input! Please enter numbers for IDs.")
        
        elif choice == "6":
            print("\n📝 Add Grade")
            try:
                grade_id = int(input("Enter grade ID: "))
                student_id = int(input("Enter student ID: "))
                class_id = int(input("Enter class ID: "))
                score = float(input("Enter score (0-100): "))
                if 0 <= score <= 100:
                    school.add_grade(grade_id, student_id, class_id, score)
                else:
                    print("❌ Score must be between 0 and 100!")
            except ValueError:
                print("❌ Invalid input! Please check your entries.")
        
        elif choice == "7":
            print("\n📊 View Student Grades")
            try:
                student_id = int(input("Enter student ID: "))
                school.list_grades_for_student(student_id)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        elif choice == "8":
            print("\n📊 View Class Grades")
            try:
                class_id = int(input("Enter class ID: "))
                school.list_grades_for_class(class_id)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        elif choice == "9":
            print("\n📈 Calculate Student Average")
            try:
                student_id = int(input("Enter student ID: "))
                school.calculate_student_average(student_id)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        elif choice == "0":
             # Save it
            #school.save_data()  
            print("\n👋 Thank you for using the School Management System. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

# This is the standard way to run the main function
if __name__ == "__main__":
    main()

   