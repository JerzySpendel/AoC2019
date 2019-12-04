def meets_criteria(number):
    string_number = str(number)

    if len(string_number) != 6:
        return False

    same_adjacent_exists = False

    for value, next_value in zip(string_number, string_number[1:]):
        if value == next_value:
            same_adjacent_exists = True
            break

    if not same_adjacent_exists:
        return False

    dont_decrease = True

    for value, next_value in zip(string_number, string_number[1:]):
        if int(next_value) < int(value):
            dont_decrease = False
            break

    if not dont_decrease:
        return False

    return True


def how_many(r: range):
    return len([number for number in r if meets_criteria(number)])


print(
    how_many(
        range(158126, 624574)
    )
)
