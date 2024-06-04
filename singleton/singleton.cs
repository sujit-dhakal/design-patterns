using System;

public class SingleTon{
    private static SingleTon st;
    private SingleTon(){}
    public static SingleTon GetBike(){
        if(st == null){
            st = new SingleTon();
        }
        return st;
    }
}
public class Program
{
    public static void Main(string[] args)
    {
        SingleTon st1 = SingleTon.GetBike();
        Console.WriteLine(st1.GetHashCode());
        SingleTon st2 = SingleTon.GetBike();
        Console.WriteLine(st2.GetHashCode());
    }
}
