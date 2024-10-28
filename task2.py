class school:
    def __init__(self,school_name):
        self.school_name = school_name

    def __str__(self):
        return (f'School name: {self.school_name}')
    
class students(school):
    def __init__(self,school_name,name,age,grade):
        super().__init__(school_name)
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return super().__str__() + f'\n'f'Name: {self.name}\n' f'Age: {self.age}\n'f'Grade: {self.grade}\n'
            
    
class male_students(students):
    def __init__(self,school_name,name,age,grade,gender):
        super().__init__(school_name,name,age,grade)
        self.gender = gender

    def __str__(self):
        return super().__str__() + (f'gender: {self.gender}\n')

class female_students(students):
    def __init__(self,school_name,name,age,grade,gender):
        super().__init__(school_name,name,age,grade)
        self.gender = gender

    def __str__(self):
        return super().__str__() +  (f'gender: {self.gender}\n')
    
students_1 = male_students('School of Science','Aman',18,2,'male')
students_2 = female_students('School of Science','Adel',20,2,'female')

print(students_1)
print(students_2)
                
        

    