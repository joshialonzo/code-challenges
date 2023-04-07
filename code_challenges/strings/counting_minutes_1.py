"""
Counting Minutes I
Have the function CountingMinutesI(str) take the str parameter being passed
which will be two times (each properly formatted with a colon and am or pm)
separated by a hyphen and return the total number of minutes between the two
times. The time will be in a 12 hour clock format. For example: if str is
9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am the
output should be 1320.

Examples

Input: "12:30pm-12:00am"
Output: 690

Input: "1:23am-1:08am"
Output: 1425

Tags
string manipulationsearching
"""


def counting_minutes_1(strParam):

  # code goes here
  MINUTES_PER_DAY = 24 * 60
  string = strParam
  time_1, time_2 = string.split("-")

  # retrieve integers
  hours_1 = int(time_1.split(":")[0])
  minutes_1 = int(time_1.split(":")[1][:2])
  xm_1 = time_1[-2:] # am or pm?

  hours_2 = int(time_2.split(":")[0])
  minutes_2 = int(time_2.split(":")[1][:2])
  xm_2 = time_2[-2:] # am or pm?

  # translate hours and minutes to 24-hours format

  total_1 = 0
  if xm_1 == "am" and hours_1 == 12:
    total_1 = minutes_1
  elif xm_1 == "am" and hours_1 < 12:
    total_1 = hours_1 * 60 + minutes_1
  elif xm_1 == "pm" and hours_1 == 12:
    total_1 = hours_1 * 60 + minutes_1
  elif (xm_1 == "pm") and (hours_1 < 12):
    total_1 = (12 + hours_1) * 60 + minutes_1

  total_2 = 0
  if xm_2 == "am" and hours_2 == 12:
    total_2 = minutes_2
  elif xm_2 == "am" and hours_2 < 12:
    total_2 = hours_2 * 60 + minutes_2
  elif xm_2 == "pm" and hours_2 == 12:
    total_2 = hours_2 * 60 + minutes_2
  elif xm_2 == "pm" and hours_2 < 12:
    total_2 = (12 + hours_2) * 60 + minutes_2

  # compute the difference between the two times

  total = total_2 - total_1
  if total < 0:
    total += MINUTES_PER_DAY

  return total


def main():
  string = "2:00pm-3:00pm"
  assert counting_minutes_1(string) == 60


if __name__ == "__main__":
  main()
