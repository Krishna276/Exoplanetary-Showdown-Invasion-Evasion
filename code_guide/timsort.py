"""Timsorts a randomly generated list."""

from random import randint

def _insertionSort(lst: list[object]) -> list[object]:
    """Perform an insertion sort on a list. Insertion sort is fast for small lists.

    Args:
        lst (list[object]): The list to sort.

    Returns:
        list[object]: The sorted list.
    """
    for i in range(1, len(lst)):
        key: object = lst[i]
        j: int = i - 1
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def _merge(left: list[object], right: list[object]) -> list[object]:
    """Merges two sublists."""
    new_list: list[object] = []
    while len(left) > 0 and len(right) > 0:
        new_list.append(left.pop(0) if right[0] > left[0] else right.pop(0))
    new_list.extend(left + right)
    return new_list

def _calculate_minrun(n: int) -> int:
    """Calculates the ideal value for the minrun parameter, based on the number of elements in the list."""
    r: int = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r

def timsort(lst: list[object], minrun: int | None = None) -> list[object]:
    """Timsort is a very fast sorting algorithm and it is stable too.
    It is a hybrid of an insertion sort and a merge sort.
    On small lists, this is just an insertion sort, but on large lists, it is optimised to become faster.

    Args:
        lst (list[object]): The list to sort. Must have comparison operators defined.
        minrun (int | None, optional): The size of a run. Defaults to None.

    Returns:
        list[object]: The sorted list.
    """
    n: int = len(lst)
    if minrun is None:
        minrun = _calculate_minrun(n)
    for start in range(0, n, minrun):
        end = min(start + minrun, n)
        lst[start:end] = _insertionSort(lst[start:end])
    size: int = minrun
    while size < n:
        for start in range(0, n, size * 2):
            mid: int = min(start + size, n)
            end: int = min(mid + size, n)
            lst[start:end] = _merge(lst[start:mid], lst[mid:end])
        size *= 2
    return lst

# For testing the timsort's stability
class Thing:
    """A thing to sort.
    """
    def __init__(self, number: int, letter: str) -> None:
        """A thing to sort.

        Args:
            number (int): A random number.
            letter (str): A letter index from the alphabet.
        """
        self._number: int = number
        self._letter: str = letter
    
    def __str__(self) -> str:
        return str(self._number) + " " + self._letter
    
    def __gt__(self, other: object) -> bool:
        return self._number > other.number
    
    @property
    def number(self) -> int:
        return self._number


lst: list[Thing] = [Thing(randint(0, 25), chr(0x41 + i)) for i in range(26)]
for item in timsort(lst, minrun=4):
    print(item)
