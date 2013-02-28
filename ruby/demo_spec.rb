require "./demo"

describe Demo do

  it "should return 64 if <= 64" do
  	demo = Demo.new
   	demo.transform(63).should == 64
  end

  it "should return 128 if >64 and <= 128" do
  	demo = Demo.new
   	demo.transform(65).should == 128
  end

  it "should return 256 if >128 and <= 256" do
  	demo = Demo.new
   	demo.transform(210).should == 256
  end

  it "should return 512 if >256 and <= 512" do
  	demo = Demo.new
   	demo.transform(257).should == 512
  end

  it "should return 1024 if >512 and <= 1024" do
  	demo = Demo.new
   	demo.transform(1024).should == 1024
  end

  it "should return 2048 if >1024 and <= 2048" do
  	demo = Demo.new
   	demo.transform(1025).should == 2048
  end

end