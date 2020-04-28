'''
    Coding various algorithms
'''
import logging


def qs_partition(array, left, right, pivot):
    logging.info("Params array=%s, left=%s, right=%s, pivot=%s", array, left, right, pivot)
    while(left <= right):
        try:
            while(array[left] < pivot):
                left+=1
        except IndexError as e:
            logging.exception("Unable to get left index %s for array %s", left, array)
            raise e

        try:
            while(array[right] > pivot):
                right+=1
        except IndexError as e:
            logging.exception("Unable to get right index %s for array %s", right, array)
            raise e

        if left <= right:
            # Perform swap
            left_element = array[left]
            right_element = array[right]
            array[left] = right_element
            array[right] = left_element
            left+=1
            right-=1

        return left

def quick_sort(array, left, right):
    if left > right:
        return
    pivot = array[(left + right)/2]
    index = qs_partition(array, left, right, pivot)
    print(index)
    print(array)
    # quick_sort(array, left, index - 1)
    quick_sort(array, index, right)


def sort(array):
    '''
        Sort arrary
    :param array:
    :return:
    '''


def binary_search_recursive(array, x, left, right):
    if left > right:
        return False

    print("Searching %s, left = %s, right = %s" % (array, left, right))
    pivot = left + right / 2

    if array[pivot] == x:
        return True
    elif left == right and array[left] == x:
        # Needed to stop max recursion
        return True
    elif left == right and array[left] != x:
        # Needed to stop max recursion
        return False
    elif x < array[pivot]:
        print("Pivot %s was less" % (pivot))
        return binary_search_recursive(array, x, left, pivot - 1)
    else:
        print("Pivot %s was more" % (pivot))
        return binary_search_recursive(array, x, pivot + 1, right)


def search(array, x):
    print(binary_search_recursive(array, x, 0, len(array) - 1))

if __name__ == "__main__":
    array = [1, 9, 7, 4]
    # quick_sort(array, 0, 3)
    # Binary Search expects a sorted datastructure
    array.sort()
    search(array, 9)
