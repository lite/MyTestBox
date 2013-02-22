using System;

namespace Demo{

    public interface IAnimal{
        string say();
        string sleep();
    }

    public class Dog : IAnimal{
        public string say(){
            return "wang..";
        }

        public string sleep(){
            return "zzz..";
        }
    }

    public class Cat : IAnimal{
        public string say(){
            return "miao..";
        }

        public string sleep(){
            return "";
        }
    }

    public class HelloMono{

        public static void play(IAnimal _animal){
            Console.WriteLine(_animal.say() + " " + _animal.sleep());
        }
        public static void Main(){
            play(new Dog());
            play(new Cat());
        }
    }
}
