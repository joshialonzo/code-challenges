"""
Have the function username_validation(str) take the str parameter
being passed and determine if the string is a valid username according to
the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true,
otherwise return the string false.
"""


def username_validation(string):

  # code goes here
  username = string
  between_4_and_25 = 4 <= len(username) <= 25
  letters = {letter for letter in username}
  start_with_a_letter = username[0].isalpha()
  has_valid_characters = all([
    letter.isalnum() or letter == "_"
    for letter in letters
  ])
  cannot_end_with_underscore = username[-1] != "_"

  if (
    between_4_and_25 and
    start_with_a_letter and
    has_valid_characters and
    cannot_end_with_underscore
  ):
    return True

  return False
