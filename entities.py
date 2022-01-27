from app import db

#entities

   
class Department(db.Model):
    __tablename__ = 'department'
    departmentId=db.Column(db.Integer,primary_key=True)
    departmentName=db.Column(db.String(100),unique=True)

    def __init__(self,departmentName):
        self.departmentName=departmentName

class Employee(db.Model):
    __tablename__ = 'employee'
    employeeId=db.Column(db.Integer,primary_key=True)
    employeeName=db.Column(db.String(100))
    qualification=db.Column(db.String(100))
    department_id=db.Column(db.Integer,db.ForeignKey('department.departmentId'))
    department=db.relationship('Department',backref='employees')
    doj=db.Column(db.Date)
    basicSalary=db.Column(db.Integer)
    photoFileName=db.Column(db.String(500))

    def __init__(self,employeeName,qualification,department,doj,basicSalary,photoFileName):
        self.employeeName=employeeName
        self.qualification=qualification
        self.department=department
        self.doj=doj
        self.basicSalary=basicSalary
        self.photoFileName=photoFileName

 