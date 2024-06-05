using System;

public interface Coffee{
    int cost();
}

public class SimpleCoffee : Coffee{
    public int cost(){
        return 5;
    }
}

public class CoffeeDecorator : Coffee{
    protected Coffee coffee;
    public CoffeeDecorator(Coffee coffee){
        this.coffee = coffee;
    }
    public virtual int cost(){
        return coffee.cost();
    }
}

public class MilkDecorator : CoffeeDecorator{
    public MilkDecorator(Coffee coffee) : base(coffee){}
    public override int cost(){
        return base.cost() + 2;
    }
}

public class Program{
    public static void Main(string[] args){
        Coffee sc = new SimpleCoffee();
        Coffee md = new MilkDecorator(sc);
        Console.WriteLine(md.cost());
    }
}