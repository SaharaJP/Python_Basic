from typing import Any, Optional


class Node:
    def __init__(self, value: Optional[Any] = None, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return 'Node [{0}]'.format(str(self.value))

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self):
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{0}]'.format(' '.join(values))
        return 'LinkedList []'

    def append(self, elem: Any) -> None:
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index) -> None:
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.length -= 1

    def get(self, el_index):
        cur_node = self.head

        if el_index < 0:
            raise IndexError
        elif el_index == 0:
            return cur_node.value
        elif el_index > self.length:
            raise IndexError

        for _ in range(el_index):
            cur_node = cur_node.next
        else:
            return cur_node.value


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)