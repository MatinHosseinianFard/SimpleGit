class Node:
    def __init__(self, value=None, neext=None):
        self.value = value
        self.neext = neext


class LinkedList:
    def __init__(self,  headname, head):
        self.headname = headname
        self.head = Node(head, None)

    def print(self):

        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.value) + ' <-- ' if itr.neext else str(itr.value)
            itr = itr.neext
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.neext

        return count

    def insert_at_begining(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return

        itr = self.head

        while itr.neext:
            itr = itr.neext

        itr.neext = Node(value, None)

    def insert_at(self, index, value):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(value)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(value, itr.neext)
                itr.neext = node
                break

            itr = itr.neext
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.neext
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.neext = itr.neext.neext
                break

            itr = itr.neext
            count += 1

    def search_at_value(self, value):
        # if self.head is None:
        #     return None
        itr = self.head
        index = 0
        while True:
            if itr.neext is None:
                return itr.value
            if itr.value == value:
                return [value, index]
            index += 1
            itr = itr.neext



    def insert_values(self, value_list):
        self.head = None
        for value in value_list:
            self.insert_at_end(value)


if __name__ == '__main__':
    pass

