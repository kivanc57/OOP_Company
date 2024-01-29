from modules.employee import Employee
#Access the same attributes, inherit them from Employee class. Double the salary.
class Employer(Employee):
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        super().__init__(emp_id, emp_name, emp_salary, emp_department)
        self.emp_salary *= 2

#Override calculate_overtime_salary, default wage is higher for the Employer
    def calculate_overtime_salary(self, overtime_salary=200):
        return super().calculate_overtime_salary(overtime_salary)

#Print only the salary details for Employer
    def print_emp_details(self):
            column_width = 15
            print(
            f'The Employer Salary:             {str(self.emp_salary).ljust(column_width)}\n'
            f'The Overtime Gross Bonus Salary: {str(self.calculate_overtime_salary())}'
            )