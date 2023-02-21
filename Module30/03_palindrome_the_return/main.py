import collections


def can_be_poly(string: str) -> bool:
    result = collections.deque(string)
    while len(result) > 1:
        if not result.pop() == result.popleft():
            return False
    else:
        return True


print(can_be_poly('abcba'))
print(can_be_poly('abcbf'))
