data = [int(line) for line in open('data', 'r').readlines()]
s = 0
for data in data:
    s += data // 3 - 2

print(s)