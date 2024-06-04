
class Employee:
    def salary(self):
        pass

class WebDeveloper(Employee):
    def salary(self):
        return 50000

class AndroidDeveloper(Employee):
    def salary(self):
        return 60000

class EmployeeFactory:
    @staticmethod
    def get_employee(empType):
        if empType.trim() == "AndroidDeveloper":
            return AndroidDeveloper()
        elif empType.trim() == "WebDeveloper":
            return WebDeveloper()
        else:
            return None

class Client:
    @staticmethod
    def main():
        emp = EmployeeFactory.get_employee("AndroidDeveloper")
        sal = emp.salary()
        print(f"Salary: {sal}")

Client.main()
