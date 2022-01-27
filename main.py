from app import api,app
from restresources import DepartmentListResource,DepartmentResource,EmployeeListResource,EmployeeResource       

api.add_resource(DepartmentResource,'/department')
api.add_resource(DepartmentListResource,'/department/<int:departmentId>')
api.add_resource(EmployeeListResource,'/employee/<int:employeeId>')
api.add_resource(EmployeeResource,'/employee')

if __name__=="__main__":
    app.run(debug=True)

