from collections import Counter


def meets_criteria(number):
    string_number = str(number)

    if len(string_number) != 6:
        return False

    dont_decrease = True

    for value, next_value in zip(string_number, string_number[1:]):
        if int(next_value) < int(value):
            dont_decrease = False
            break

    if not dont_decrease:
        return False

    counter = Counter(string_number)
    occurrences = list(counter.values())

    if 2 not in occurrences:
        return False

    return True


def how_many(r: range):
    return len([number for number in r if meets_criteria(number)])


print(
    how_many(
        range(158126, 624574)
    )
)