from typing import TypeVar, Generic, Sized, Iterable, Container, Tuple

T = TypeVar('T')

class LinkedList(Sized, Generic[T]):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._len = 0

    def append(self, value: T) -> None:
        node = _Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._len += 1

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> Iterable[T]:
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def __contains__(self, value: T) -> bool:
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False

    def __repr__(self) -> str:
        return f"{type(self).__name__}({list(self)})"


class _Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.next = None


K = TypeVar('K')
V = TypeVar('V')

class MyMapping(Iterable[Tuple[K, V]],
                Container[Tuple[K, V]],
                Generic[K, V]):
    def __init__(self) -> None:
        self.items = LinkedList[Tuple[K, V]]()

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> Iterable[Tuple[K, V]]:
        return iter(self.items)

    def __contains__(self, item: object) -> bool:
        if not isinstance(item, tuple):
            return False
        key, value = item
        for k, v in self.items:
            if k == key and v == value:
                return True
        return False

    def __getitem__(self, key: K) -> V:
        for k, v in self.items:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key: K, value: V) -> None:
        for pair in self.items:
            if pair[0] == key:
                pair[1] = value
                return
        self.items.append((key, value))

    def __repr__(self) -> str:
        items = ", ".join(f"{k!r}: {v!r}" for k, v in self.items)
        return f"{type(self).__name__}({{{items}}})"

# Example of using LinkedList class
linked_list = LinkedList[int]()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
print(len(linked_list))  # Output: 3

# Example of using MyMapping class
my_dict = MyMapping[int, str]()
my_dict[(1, 'one')] = 'first'
my_dict[(2, 'two')] = 'second'
my_dict[(3, 'three')] = 'third'
print(len(my_dict))  # Output: 3
print((1, 'one') in my_dict)  # Output: True
print(my_dict[(2, 'two')])  # Output: 'second'
