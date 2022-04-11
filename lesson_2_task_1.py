roll = [55, 'Hello user', True, 67.4, 'good day', [5, 3], {1: 100, 2: 400}, ('Hello', 'Friend')]
print(f"The list: {roll}")
n = len(roll)
print(f"The length of the list: {n}")
i = 0
while i < n:
    i += 1
    print(f"{roll[i-1]} - {type(roll[i-1])}")
