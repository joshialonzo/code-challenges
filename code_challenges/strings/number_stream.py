def number_stream(string):

  # code goes here
  current_number = None
  counter = 0

  for letter in string:
    if current_number is None:
      current_number = letter
      counter = 1
    elif letter == current_number:
      counter += 1
      if int(letter) == counter:
        return True
    else:
      current_number = letter
      counter = 1

  return False
