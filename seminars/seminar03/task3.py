# Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dict_ = {
    "V": 1,
    "R": 1,
    "T": 2,
    "A": 2
}

print(set(dict_.values()))

data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

res = set()
for d in data:
    for element in d.values():
        res.add(element)
print(res)

res = set()
for d in data:
    res = res.union(set(d.values()))
print(res)
