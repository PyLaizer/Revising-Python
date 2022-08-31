#Exercise 11.3

class Employee:
    def __init__(self,firstname,lastname,annual_salary):
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary

    # def employee_info(self):
    #     print(f"{self.firstname} {self.lastname} earns ${self.annual_salary} annually.")    

    def give_raise(self,salary_raise=5_000):
        self.annual_salary += salary_raise 
        return self.annual_salary   

# employee_instance = Employee("Eleazar","Edward",108_000)  
# employee_instance.employee_info()
# employee_instance.give_raise(10_000)
# employee_instance.employee_info()