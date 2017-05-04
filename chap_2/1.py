'''
Remove Dups! Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?

Example: in = [5,3,5,7,1,3,5] out = []5,3,7,1]
'''
import linkedlist

def remove_dups(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] not in new_arr:
            new_arr.append(arr[i])

    return new_arr

def remove_dups_cpp_style(l):
    current = l.head
    while current:
        current2 = current.get_next()
        previous = current
        while current2:
            if current.get_data() == current2.get_data():
                previous.set_next(current2.get_next())
                current2 = current2.get_next()
            else:
                previous = current2
                current2 = current2.get_next()

        current = current.get_next()
    return l

print "Case 1"
arr = [5,3,5,7,1,3,5]
print arr
print remove_dups(arr)
print "Case 2"
l = linkedlist.MyLinkedList()
l.insert(5)
l.insert(2)
l.insert(5)
l.insert(1)
l.insert(1)
l.insert(2)
l.print_list()
remove_dups_cpp_style(l)
l.print_list()

