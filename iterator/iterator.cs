using System;
public interface Iterator{
    bool hasNext();
    int Next();
}
public class NumberIterator:Iterator{
    private int[] _collection;
    private int _currentIndex = 0;
    public NumberIterator(int[] collection){
        _collection = collection;
    }
    public bool hasNext(){
        return _currentIndex < _collection.Length;
    }
    public int Next(){
        return _collection[_currentIndex++];
    }
}
public interface IterableCollection{
    Iterator CreateIterator();
}
public class NumberCollection:IterableCollection{
    private int[] _items;
    public NumberCollection(int[] items){
        _items = items;
    }
    public Iterator CreateIterator(){
        return new NumberIterator(_items);
    }
}
public class Program{
    public static void Main(string[] args){
        int[] numbers = {1,2,3,4};
        NumberCollection nc = new NumberCollection(numbers);
        Iterator it = nc.CreateIterator();
        while(it.hasNext()){
            int number = it.Next();
            Console.WriteLine(number);
        }
    }
}