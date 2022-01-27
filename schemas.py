from entities import Department, Employee
from app import ma


class EmployeeSchema(ma.Schema):
    class Meta:
        fields=('employeeId','employeeName','emailid','qualification','department_id','doj','basicSalary','photoFileName')
        modal=Employee
class DepartmentSchema(ma.Schema):
    class Meta:
        fields=('departmentId','departmentName')
        modal=Department

employee_schema=EmployeeSchema()
employees_schema=EmployeeSchema(many=True)
department_schema=DepartmentSchema()
departments_schema=DepartmentSchema(many=True)