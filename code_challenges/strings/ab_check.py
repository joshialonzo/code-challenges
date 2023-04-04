def ab_check(string):

  a_index = None
  b_index = None
  string = string.lower()
  
  for index, letter in enumerate(string):
    if letter == "a":
      a_index = index
    elif letter == "b":
      b_index = index
      if (
        a_index is not None
          and
        b_index is not None
      ):
        diff = b_index
        diff -= a_index
        diff -= 1
        if diff == 3:
          return True

  return False


def main():
  string = "Laura sobs"
  assert ab_check(string)


if __name__ == "__main__":
  main()
