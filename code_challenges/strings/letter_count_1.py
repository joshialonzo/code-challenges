def letter_count_1(string):

  # setup
  found = False
  words = string.split()
  
  # count letters per word
  words_dict = dict()
  for word in words:

    letters_dict = dict()
    for letter in word:
      if letter.isalpha():
        if letter in letters_dict:
          letters_dict[letter] += 1
        else:
          letters_dict[letter] = 1
    
    maximum = None
    for letter in letters_dict:
      number = letters_dict[letter]

      if number > 1:
        found = True

      if (
        maximum is None
        or
        letters_dict[letter] > maximum
      ):
        maximum = letters_dict[letter]
        
    words_dict[word] = maximum

  if not found:
    return -1

  # get the word
  maximum = None
  for word in words_dict:
    if (
      maximum is None
      or
      words_dict[word] > maximum
    ):
      maximum = words_dict[word]
  
  for word in words_dict:
    if words_dict[word] == maximum:
      return word
  
  return -1
