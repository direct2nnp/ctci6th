'''
Return Kth to Last: Implement an algorithm to  nd the kth to last element of a singly linked list.
Example : arr = [5,3,5,7,1,3,5] and K = 2 -> return value should be 3
'''
import linkedlist

def kth_to_last(arr, n):
    if len(arr) > n:
        return arr[-n]
    else:
        raise('ValueError - array does not have that many element')

def kth_to_last_2(arr, n):
    # iterative without efficenient simple code
    length = arr.size()
    if length > n:
        count = length - n
        current = arr.head
        for i in range(count):
            current = current.get_next()
        return current.get_data()
    elif length == n:
        return arr.head.get_data()
    else:
        raise('ValueError - array does not have that many element')

def kth_to_last_3(arr, k):
    # Using two pointer concept to iterate only one time through list
    current = arr.head
    current2 = arr.head
    for i in range(k):
        if current.get_next():
            current = current.get_next()
        else:
            raise('ValueError - array does not have that many element')

    while current:
        current = current.get_next()
        current2 = current2.get_next()

    return current2.get_data()


def kth_to_last_4(current, k):
    # recursive approch
    if not current:
        return 0

    n = kth_to_last_4(current.get_next(), k) + 1
    if n == k:
        print 'kth element value - ' + str(current.get_data())

    return n


print "Case 1"
arr = [5,3,5,7,1,3,5]
print arr
print 'K = ' + str(2)
print kth_to_last(arr, 2)

print "Case 2"
l = linkedlist.MyLinkedList()
l.insert(5)
l.insert(2)
l.insert(5)
l.insert(1)
l.insert(1)
l.insert(2)
l.print_list()
print 'K = ' + str(2)
print 'kth element value - ' + str(kth_to_last_2(l, 2))
print 'kth element value - ' + str(kth_to_last_3(l, 2))
kth_to_last_4(l.head, 2)
