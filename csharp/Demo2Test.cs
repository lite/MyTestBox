using System;
using NUnit.Framework;

namespace Demo
{
    [TestFixture]
    public class Demo2Test{
        [Test]
        public void OutputTest(){
        	string path = "/tmp/demo";
        	Demo.Utility util = new Demo.Utility();
			string log = util.Output("/tmp/demo");
            Assert.IsNotEmpty(log, path + " log" );
        }
    }
}