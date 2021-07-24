def convert_to_binary(num, cache):
  digit = num
  if digit == 0 or digit == None:
    return cache
  cache = str(digit % 2) + cache
  digit = digit // 2
  return convert_to_binary(digit, cache)  