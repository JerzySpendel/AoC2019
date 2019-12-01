def fuel_for_fuel(fuel, part):
    s = fuel // 3 - 2
    if s <= 0:
        return part

    return fuel_for_fuel(s, part + s)


data = [int(line) for line in open('data', 'r').readlines()]
s = 0
for data in data:
    part = data // 3 - 2
    s += part + fuel_for_fuel(part, 0)

print(s)
