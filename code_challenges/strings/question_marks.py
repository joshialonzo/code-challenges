def question_marks(string):

  # code goes here
  index_1 = None
  index_2 = None
  found = False

  for index, letter in enumerate(string):

    if letter.isdigit() and index_1 is None:
      index_1 = index

    elif letter.isdigit():
      if index_2 is None:
        index_2 = index
      else:
        index_1, index_2 = index_2, index
      num_1 = int(string[index_1])
      num_2 = int(string[index_2])
      if num_1 + num_2 == 10:
        substring = string[
          index_1+1: index_2
        ]

        if len(substring) < 3:
          return False
        
        counter = 0
        for subletter in substring:
          if subletter == "?":
            counter += 1
        if  counter == 3:
          found = True
          continue
        else:
          return False
    
  if not found:
    return False

  return True
