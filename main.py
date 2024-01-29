from modules.employee import Employee
from modules.employer import Employer

def main():
    emp_data = (
    ("ADAMS", "E7876", 50000, "ACCOUNTING"),
    ("JONES", "E7499", 45000, "RESEARCH"),
    ("MARTIN", "E7900", 50000, "SALES"),
    ("SMITH", "E7698", 55000, "OPERATIONS")
    )

    for emp in emp_data:
        emp_instance = Employee(emp_name=emp[0], emp_id=emp[1], emp_salary=emp[2], emp_department=emp[3])
        print(str(emp_instance.emp_assign_department()))
        print(str(emp_instance.calculate_overtime_salary()))
        emp_instance.print_emp_details()


    employer = ('Kivanc Gordu', '34D12', 120000, 'CEO')
    employer_instance = Employer(emp_name=employer[0], emp_id=employer[1], emp_salary=employer[2], emp_department=employer[3])
    employer_instance.calculate_overtime_salary()
    employer_instance.print_emp_details()

if __name__ == '__main__':
    main()