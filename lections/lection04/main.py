data = [x for x in range(10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(res)  # [0, 2, 4, 6, 8]


data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)


users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)  # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]


users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)  # [(0, 'user1'), (1, 'user2'), (2, 'user3))]
