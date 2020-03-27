from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if not self.current:
            # If self.current is None, the list isn't full yet
            self.storage.add_to_tail(item)
            if self.storage.length == self.capacity:
                # If this puts the list at capacity, set self.current
                # to the head. (self.current is basically the node
                # that will get replaced if a new value is appended.)
                self.current = self.storage.head
        else:
            if self.current is self.storage.head:
                # Replace the head
                self.current = self.storage.head.next
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
            elif self.current is self.storage.tail:
                # Replace the tail
                self.current = self.storage.head
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
            else:
                # Log self.current's next and prev, then delete it.
                current_next = self.current.next
                current_prev = self.current.prev
                self.storage.delete(self.current)
                # Set the new self.current
                self.current = current_next
                # Keep track of the tail, since we'll be adding the
                # new value as the tail temporarily.
                tail = self.storage.tail
                self.storage.add_to_tail(item)
                # Set the new node's next and prev to be the same as
                # the old self.current.
                new_node = self.storage.tail
                new_node.next = current_next
                new_node.prev = current_prev
                # Also fix the directions for the nodes that surround the new node
                current_next.prev = new_node
                current_prev.next = new_node
                # Finally, set the tail back to being the proper tail,
                # and make sure it has no "next" node.
                self.storage.tail = tail
                self.storage.tail.next = None

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next
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
