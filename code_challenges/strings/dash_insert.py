"""
Dash Insert

Have the function DashInsert(str) insert dashes ('-')
between each two odd numbers in str. For example: if
str is 454793 the output should be 4547-9-3. Don't
count zero as an odd number.

Examples

Input: 99946
Output: 9-9-946

Input: 56730
Output: 567-30
"""

def dash_insert(strParam):

  # code goes here
  string = strParam
  new_string = ""
  for index in range(len(string[:-1])):
    current_letter = int(string[index])
    next_letter = int(string[index + 1])
    current_letter_odd = current_letter % 2 != 0
    next_letter_odd = next_letter % 2 != 0
    new_string += str(current_letter)
    if current_letter_odd and next_letter_odd:
      new_string += "-"
  
  new_string += string[-1]

  return new_string
