import functools
class Comparator:
    def __init__(self, key, direction):
        self.key = key
        self.signal = 1 if direction == 'asc' else -1

    def compare(self, left, right):
        left.setdefault(self.key, 0)
        right.setdefault(self.key, 0)
        if left[self.key] < right[self.key]:
            return -self.signal
        elif left[self.key] > right[self.key]:
            return self.signal
        else:
            return 0

def min_by_key(key, records):
    # minRecord = {}
    # minKey = float('inf')
    # for record in records:
    #     if key not in record:
    #         if minKey > 0:
    #             minRecord = record
    #             minKey = 0
    #     else:
    #         if minKey > record[key]:
    #             minRecord = record
    #             minKey = record[key]
    # return minRecord
    return sorted(records, key = lambda x : x.get(key, 0))[0]

def first_by_key(key, direction, records):
    # if direction == 'asc':
    #     return min_by_key(key, records)
    # maxRecord = {}
    # maxKey = -float('inf')
    # for record in records:
    #     if key not in record:
    #         if maxKey < 0:
    #             maxRecord = record
    #             maxKey = 0
    #     else:
    #         if maxKey < record[key]:
    #             maxRecord = record
    #             maxKey = record[key]
    # return maxRecord
    return sorted(records, key = lambda x: (1 if direction == 'asc' else -1) * x.get(key, 0))[0]

def first_by_sort_order(sortOrder, records):
    def compare(a, b):
        for order in sortOrder:
            cmp = Comparator(*order)
            result = cmp.compare(a, b)
            if result != 0:
                return cmp.compare(a, b)
        return 0
    return sorted(records, key = functools.cmp_to_key(compare))[0]

assert first_by_key("a", "asc", [{"a": 1}]) == {"a": 1}
assert first_by_key("a", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) in [{"b": 1}, {"b": -2}]
assert first_by_key("a", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"a": 10}
assert first_by_key("b", "asc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": -2}
assert first_by_key("b", "desc", [{"b": 1}, {"b": -2}, {"a": 10}]) == {"b": 1}
assert first_by_key("a", "desc", [{}, {"a": 10, "b": -10}, {}, {"a": 3, "c": 3}]) == {"a": 10, "b": -10}

cmp = Comparator("a", "asc")
assert cmp.compare({"a": 1}, {"a": 2}) == -1
assert cmp.compare({"a": 2}, {"a": 1}) == 1
assert cmp.compare({"a": 1}, {"a": 1}) == 0

assert (
    first_by_sort_order(
        [("a", "desc")],
        [{"a": 5.0}, {"a": 6.0}],
        ) == {"a": 6.0}
    )

assert (
    first_by_sort_order(
        [("b", "asc"), ("a", "asc")],
        [{"a": -5, "b": 10}, {"a": -4, "b": 9}],
        ) == {"a": -4, "b": 9}
    )

assert (
    first_by_sort_order(
        [("b", "asc"), ("a", "asc")],
        [{"a": -5, "b": 10}, {"a": -4, "b": 10}],
        ) == {"a": -5, "b": 10}
    )