using System;

public interface Employee{
    int salary();
}

public class WebDeveloper : Employee
{
    public int salary(){
        return 50000;
    }
}

public class AndroidDeveloper : Employee
{
    public int salary(){
        return 60000;
    }
}

public class EmployeeFactory{
    public static Employee getEmployee(string empType){
        if (empType == "AndroidDeveloper"){
            return new AndroidDeveloper();
        }
        else if (empType == "WebDeveloper"){
            return new WebDeveloper();
        }
        else{
            return null;
        }
    }
}

public class Client{
    public static void Main(string[] args){
        Employee emp = EmployeeFactory.getEmployee(empType:"AndroidDeveloper");
        int sal = emp.salary();
        Console.WriteLine("Salary: " + sal);
    }
}
