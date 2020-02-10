arbitrary_numbers = map(lambda num: num ** 3, filter(lambda num: num % 3 == 0, range(1, 21)))

print(list(arbitrary_numbers))