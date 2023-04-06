def simple_symbols(string):

  # code goes here
  if string[0].isalpha() or string[-1].isalpha():
    return False

  string_len = len(string)
  valid_symbols = {"+", "="}
  for i in range(1, string_len):
    char = string[i]
    if char in valid_symbols:
      continue
    elif char.isdigit():
      continue
    elif char.isalpha():
      before = string[i-1] == "+"
      after = string[i+1] == "+"
      if before and after:
        continue
      else:
        return False
    else:
      return False
  
  return True
