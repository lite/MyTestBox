class Demo
  def transform(i)
    return 64 if i<=64
    return 128 if i<=128
    return 256 if i<=256
    return 512 if i<=512
    return 1024 if i<=1024
    2048
  end
end