
def convert_to_binary(num, cache):
  """
  @description:
    converts integer to its binary equivalent
  @params:
    num (INT): integer to be converted
    cache (STR): a string to recursively store resulting modullus
  @returns:
    (FUNC): itself if base case is not met
    (STR): final cache
  """
  digit = num
  if digit == 0 or digit == None:
    return cache
  cache = str(digit % 2) + cache
  digit = digit // 2
  return convert_to_binary(digit, cache)  

def count_gaps(binary_string):
  """
    @description:
     counts gaps in binary string
    @params:
      binary_string (STR)
    @returns:
      highest_count (INT): the length of the largest sequence of zeros in between ones
  """
  counter = 0
  index = 0
  highest_count = counter
  while index <  len(binary_string):
    if binary_string[index] == '0':
      counter += 1
    else:
      if highest_count < counter:
        highest_count = counter
      counter = 0
    index+=1
  return highest_count

def binary_gap(num, cache):
  """
  @description:
    counts the length of the largest sequence of zeros in between ones in a binary string
  @params:
    num(INT): the number in base 10
    cache (STR): holds the resulting modulus of the integer during binary conversion
  """
  if (type(num) != int):
    return f"{num} should be an integer"
  binary_string = convert_to_binary(num, cache)
  return binary_gap(binary_string)


if __name__ == '__main__':
  binary_gap(103, '')