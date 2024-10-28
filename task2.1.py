class eng_student:
    def __init__(self,name,age,grade,lang):
        self.name = name
        self.age = age
        self.grade = grade
        self.lang = lang

    def speak(self):
        return(f'{self.name} can speak {self.lang}')

    def __str__(self):
        return (f'Name: {self.name}\n'
                f'Age: {self.age}\n'
                f'Grade: {self.grade}\n'
                f'Language: {self.lang}\n')
class eng_and_spanish_student(eng_student):
    def __init__(self,name,age,grade,lang,second_lang):
        super().__init__(name,age,grade,lang)
        self.second_lang = second_lang

    def speak(self):
        return (f'{self.name} can speak {self.lang} and {self.second_lang}')

    def __str__(self):
        return super().__str__() + f'Second language: {self.second_lang}\n'
    
class teachers:
    def __init__(self,name,science,age,lang):
        self.name = name
        self.science = science
        self.age = age
        self.lang = lang

    def speak(self):
        return(f'{self.name} can speak {self.lang}')

    def __str__(self):
        return (f'Name: {self.name}\n'
                f'Age: {self.age}\n'
                f'Science: {self.science}\n'
                f'Language: {self.lang}\n')
english_st = eng_student('John', 20, 7, 'English')
half_english_stud = eng_and_spanish_student('Lenon', 19, 6, 'English', 'Spanish')
teacher = teachers('Seong', 'Math', 45, 'Korean')

print(english_st)
print(half_english_stud)
print(teacher)
print('------------------------------------------------------------------------------')
print(english_st.speak())
print(half_english_stud.speak())
print(teacher.speak())
