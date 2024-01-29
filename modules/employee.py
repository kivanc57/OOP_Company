class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary= emp_salary
        self.emp_department = emp_department

#If the working hours > 50, get extra hours times bonus and add it to the standard wage
    def calculate_overtime_salary(self, overtime_salary=120):
        hours_worked = int(input('How many hours did my Employee/Employer work?: '))
        if hours_worked > 50:
            overtime_hours = hours_worked - 50
            return ((overtime_hours * overtime_salary) + int(self.emp_salary))
        return 0
#Change the department if needed
    def emp_assign_department(self):
        new_department = (input('Which department would you like, Boss?: ')).upper()
        self.emp_department = new_department
        return self.emp_department
#Access the Employee details
    def print_emp_details(self):
        column_width = 30
        print(
            f'The Employee Name:       {self.emp_name.ljust(column_width)}\n'
            f'The Employee ID:         {self.emp_id.ljust(column_width)}\n'
            f'The Employee Salary:     {str(self.emp_salary).ljust(column_width)}\n'
            f'The Employee Department: {self.emp_department.ljust(column_width)}\n'
        )