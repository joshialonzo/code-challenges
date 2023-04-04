def username_validation(string):

  # code goes here
  username = string
  letters = {letter for letter in username}
  start_with_a_letter = username[0].isalpha()
  has_valid_characters = all([
    letter.isalnum() or letter == "_"
    for letter in letters
  ])
  cannot_end_with_underscore = username[-1] != "_"

  if (
    start_with_a_letter and
    has_valid_characters and
    cannot_end_with_underscore
  ):
    return True

  return False
