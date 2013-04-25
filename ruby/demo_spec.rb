require "./demo"

describe Demo do

  before do
    @demo = Demo.new
  end

  it "should return 64 if <= 64" do
  	@demo.transform(63).should == 64
  end

  it "should return 128 if >64 and <= 128" do
  	@demo.transform(65).should == 128
  end

  it "should return 256 if >128 and <= 256" do
  	@demo.transform(210).should == 256
  end

  it "should return 512 if >256 and <= 512" do
  	@demo.transform(257).should == 512
  end

  it "should return 1024 if >512 and <= 1024" do
  	@demo.transform(1024).should == 1024
  end

  it "should return 2048 if >1024 and <= 2048" do
  	@demo.transform(1025).should == 2048
  end

  it "should return 4096 if >2048 and <= 4096" do
    @demo.transform(2049).should == 4096
  end

  it "should return Math.log" do
    (1..100).each do |n|
      @demo.my_logn(n).should == Math.log(n, 2).to_i
    end
  end
end