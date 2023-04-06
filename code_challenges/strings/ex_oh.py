def ex_oh(string):

  # code goes here
  x_number = 0
  o_number = 0

  for letter in string:
    if letter == "x":
      x_number += 1
    elif letter == "o":
      o_number += 1
  
  if x_number == o_number:
    return True
  else:
    return False
