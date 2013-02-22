using System;
using NUnit.Framework;

namespace Demo
{
    [TestFixture]
    public class DemoTest{
        [Test]
        public void PlayTest(){
            Demo.Dog dog = new Demo.Dog();
            Demo.Cat cat = new Demo.Cat();

            Assert.AreEqual("zzz..", dog.sleep(), "Dog.sleep" );
            Assert.AreEqual("miao..", cat.say(), "Cat.say" );
        }
    }
}