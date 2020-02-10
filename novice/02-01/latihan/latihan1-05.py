def hof_write_repeat(message, n, action):
    for i in range(n):
        action(message)

hof_write_repeat('Hello', 5, print)

import logging
hof_write_repeat('Hello', 5, logging.error)

def add2(numbers):
    new_numbers = []
    for n in numbers:
        new_numbers.append(n + 2)
    return new_numbers

print(add2([23, 88]))

def hof_add(increment):
    def add_increment(numbers):
        new_numbers = []
        for n in numbers:
            new_numbers.append(n + increment)
        return new_numbers
    return add_increment

add5 = hof_add(5)
print(add5([23, 88]))  
add10 = hof_add(10)
print(add10([23, 88]))  