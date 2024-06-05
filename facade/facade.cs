public interface Shape{
    void draw();
}
public class Rectangle:Shape{
    public void draw(){
        Console.WriteLine("Rectangle");
    }
}
public class Circle:Shape{
    public void draw(){
        Console.WriteLine("Circle");
    }
}
public class ShapeMaker{
    private Shape rectangle;
    private Shape circle;
    public ShapeMaker(){
        rectangle = new Rectangle();
        circle = new Circle();
    }
    public void drawCircle(){
        circle.draw();
    }
    public void drawRectange(){
        rectangle.draw();
    }
}
public class Facade{
    public static void Main(string[] args){
        ShapeMaker shape = new ShapeMaker();
        shape.drawCircle();
        shape.drawRectange();
    }
}