from doubly_linked_list import DoublyLinkedList, ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        else:
            if self.current is self.storage.head:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                if self.storage.head.next:
                    self.current = self.storage.head.next
                else:
                    self.current = self.storage.head
            elif self.current is self.storage.tail:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.head
            else:
                current_next = self.current.next
                current_prev = self.current.prev
                self.storage.delete(self.current)
                new_node = ListNode(item)
                new_node.next = current_next
                new_node.prev = current_prev
                current_next.prev = new_node
                current_prev.next = new_node
                self.storage.length += 1
                self.current = new_node.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        list_buffer_contents.append(node.value)
        while node.next:
            node = node.next
            list_buffer_contents.append(node.value)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
