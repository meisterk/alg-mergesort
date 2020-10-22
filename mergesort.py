import unittest

# Function mergesort:
# Parameter: unsortiertes Array mit Zahlen
# Result: sortiertes Array


def mergesort(unsortiert):
    return unsortiert


# Testcases


class TestMergesort(unittest.TestCase):
    def test_mergesort_1(self):
        unsortiert = [7, 12, 4, 8, 3, 9]
        sortiert = [3, 4, 7, 8, 9, 12]
        self.assertEqual(mergesort(unsortiert), sortiert)


# Run Tests
if __name__ == "__main__":
    unittest.main()
