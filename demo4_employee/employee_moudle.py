class Employee:           #Module Level
    company_name= None  #static variable or class variable  #inside the class
    company_location= None


    def __init__(self):
        self.emp_id = None   #non-static variable or instance
        self.emp_name = None
        self.emp_salary = None
        self.emp_performance = None

    def print_author_name():
        print("Author Name: "," Dhaval Khatri")
     #staticmethod
    def display_employee_record(self):
        print(35 * "-")
        print("Employee Id:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee performance:", self.emp_performance)
        print("Company Name:", Employee.company_name)
        print("Company Location:", Employee.Compnay_Location)
        print(35 * "-")

    def calculate_bonus(self):
        if self .emp_performance == "A":
             print(self.emp_name)
             print("10%")
             print(self.emp_salary + self.emp_salary * 10 / 100)
        elif self.emp_performance == "B":
             print(self.emp_name)
             print("5%")
             print(self.emp_salary + self.emp_salary * 5 / 100)
        elif self.emp_performance == "C":
             print(self.emp_name)
             print("2%")
             print(self.emp_salary + self.emp_salary * 2 / 100)
         else:
              print(self.emp_name)
              print("No Bonus")
              print(self.emp_salary)








