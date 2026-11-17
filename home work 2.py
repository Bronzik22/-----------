numbers = [1, 90, 6, 13, 78, -97]

for i in range(0, len(numbers), 2):
    print(numbers[i])

numbers = [1, -8, 1, 11, 78, -64]
result = []

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        result.append(numbers[i])

print(result)

rrr = ["кіт", "собака", "попугай"]
result = []

for i in range(len(rrr) - 1, -1, -1):
    result.append(rrr[i])

print(result)
