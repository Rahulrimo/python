class Student:
    
    def set_name(self, name):
        self.name = name    #class attribute
        
        
    def get_name(self):
        return self.name
    
student1 = Student()
student1.set_name("John Doe")
print(student1.get_name()) # Output: John Doe
student1.eng_marks = 85  #instance attribute
print(student1.eng_marks) # Output: 85

student2 = Student()
student2.set_name(" Doremon")
print(student2.get_name())