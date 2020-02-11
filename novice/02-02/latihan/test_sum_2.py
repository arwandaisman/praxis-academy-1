def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")


# Output
# Traceback (most recent call last):
#   File "test_sum_2.py", line 9, in <module>
#     test_sum_tuple()
#   File "test_sum_2.py", line 5, in test_sum_tuple
#     assert sum((1, 2, 2)) == 6, "Should be 6"
# AssertionError: Should be 6
