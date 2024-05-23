class students:
    def __init__(self,roll_name,name,class_name):
        self.roll_name = roll_name
        self.name = name
        self.class_name = class_name
        self.marks = {}

    def add_marks(self,subjects,marks):
        if subjects in self.marks:
            print(f"{self.marks} is already added{subjects}")
        else:
            self.marks[subjects] = marks

    def caculate_average_marks(self):
        if not self.marks:
            print(f"no availables marks")
        total_marks = sum(self.marks.values())
        average_marks = total_marks/len(self.marks)    
        return average_marks  

    def display_students_info(self):
        print(f"students information")
        print(f"roll number: {self.roll_name}") 
        print(f"name: {self.name}")
        print(f"class: {self.class_name}")
        print(f"marks: {self.marks}") 
        print(f"average marks: {self.caculate_average_marks()}")   

student1 = students(28, "sachin","th",  )
student2 = students(26,"sharthak","11th")


student1.add_marks("maths",100)
student1.add_marks("english",90)
student1.add_marks("science",80)

student2.add_marks("maths",100)
student2.add_marks("english",90)
student2.add_marks("science",80)



student1.display_students_info()
student2.display_students_info()

