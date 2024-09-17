  def last2(str):
    if len(str)<2:
      return 0
    last = str[-2:]
    counter = 0
    for i in range(len(str)-2):
      if str[i:i+2] == last:
        counter+=1
    return counter
