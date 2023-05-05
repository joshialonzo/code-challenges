FIVE_NAMES = ["John", "Paul", "George", "Ringo", "Pete"]
AGES = [20, 21, 22, 23, 24]



MAP_NAME_AGE = dict(zip(FIVE_NAMES, AGES))


def average_age(age_list):
    """Return the average age of the age list."""
    return sum(age_list) / len(age_list)


print(average_age(AGES))
print(MAP_NAME_AGE)