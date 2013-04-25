class Demo
  def transform(i)
  	return do_transform_log2 i
  	return 64 if i<=64
    return 128 if i<=128
    return 256 if i<=256
    return 512 if i<=512
    return 1024 if i<=1024
    2048
  end

  def do_transform(i)
  	(i <= 64)? 64 :do_transform((i+1)/2) *2 
  end

  def do_transform_log2(i)
  	1 << Math.log(i-1,2).to_i + 1
  end

  def my_logn(n)
  	(n<2)?0:(my_logn(n/2)+1) 
  end
end