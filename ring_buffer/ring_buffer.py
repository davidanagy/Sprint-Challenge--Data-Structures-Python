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
        self.capacity = capacity
        # Initialize current at 0 because that'll be the
        # first value that gets replaced.
        self.current = 0
        # Looking at the test file, it wants the storage
        # to always have capacity values. So initaliaze
        # with only "None"s.
        self.storage = [None] * capacity

    def append(self, item):
        # Replace the item in location "self.current"
        self.storage[self.current] = item
        if self.current < self.capacity - 1:
            # Add one to current if it's not at the end of the list
            self.current += 1
        else:
            # If it is at the end of the list, set it back to 0.
            self.current = 0

    def get(self):
        storage_print = []
        for item in self.storage:
            # Only return items that aren't "None."
            if item:
                storage_print.append(item)

        return storage_print
