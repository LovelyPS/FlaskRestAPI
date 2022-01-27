from datetime import datetime
import email
from flask import request,jsonify,session
from flask_restful import Resource
from werkzeug.utils import secure_filename
import os

from schemas import DepartmentSchema, EmployeeSchema
from app import db,app
from entities import Department,Employee



employee_schema=EmployeeSchema()
employees_schema=EmployeeSchema(many=True)
department_schema=DepartmentSchema()
departments_schema=DepartmentSchema(many=True)

#resouces
class DepartmentListResource(Resource):
    def get(self,departmentId):
        dept=Department.query.get_or_404(departmentId)
        return department_schema.dump(dept)
    def delete(self,departmentId):
        dept=Department.query.get_or_404(departmentId)
        db.session.delete(dept)
        db.session.commit()
        return 'Department Deleted Successfully'
   

class DepartmentResource(Resource):
    def get(self):
        departments=Department.query.all()
        return departments_schema.dump(departments)
    
    def post(self):
        departmentName=request.json['departmentName']
        new_dept=Department(departmentName)
        db.session.add(new_dept)
        db.session.commit()
        return 'Department Added Successfully'
    def put(self):
        id=request.json['departmentId']
        dept=Department.query.get_or_404(id)

        if 'departmentName' in request.json:
            dept.departmentName=request.json['departmentName']
        db.session.commit()
        return 'Department Updated Successfully'
    
        
class EmployeeListResource(Resource):
    def get(self,employeeId):
        emp=Employee.query.get_or_404(employeeId)
        return employee_schema.dump(emp)
    def delete(self,employeeId):
        emp=Employee.query.get_or_404(employeeId)
        db.session.delete(emp)
        db.session.commit()
        return 'employee Deleted Successfully'
    

class EmployeeResource(Resource):
    def get(self):
        employees=Employee.query.all()
        return employees_schema.dump(employees)
    
    def post(self):
        employeeName=request.json['employeeName']
        qualification=request.json['qualification']
        dep=request.json['department_id']
        department=Department.query.get(dep)
        doj=request.json['doj']
        date_obj = datetime. strptime(doj, '%Y-%m-%d')
        basicSalary=request.json['basicSalary']
        photoFileName=request.json['photoFileName']
        new_emp=Employee(employeeName,qualification,department,date_obj,basicSalary,photoFileName)
        db.session.add(new_emp)
        db.session.commit()
        return "Employee Added Successfully"
    
    def put(self):
        id=request.json['employeeId']
        emp=Employee.query.get_or_404(id)

        if 'employeeName' in request.json:
            emp.employeeName=request.json['employeeName']
        db.session.commit()
        return "Employee Added Successfully"


@app.route('/savefile' , methods = ['GET' , 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'File Uploaded'


   