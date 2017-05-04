import node

class MyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_top(self, data):
        new_node = node.Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert(self, data):
        if not self.head:
            self.insert_top(data)
        else:
            current = self.head
            while current and current.get_next():
                current = current.get_next()

            new_node = node.Node(data)
            current.set_next(new_node)

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()

        return count

    def print_list(self):
        current = self.head
        s = '['
        while current:
            s += str(current.get_data()) + ', '
            current = current.get_next()
        print s[:-2] + ']'

    def search(self, data):
        current = self.head
        found = False
        while found is False and current:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        if current == None:
            raise ValueError('Data is not in list')

        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while found is False and current:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current == None:
            raise ValueError('Data is not in list')
        
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


            
