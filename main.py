"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

def foo(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        x, y = min(a, b), max(a, b)
        return foo(x, y % x)

def longest_run(mylist, key):
    longest_run = 0
    current_run = 0
    for i in range(len(mylist)):
        if mylist[i] == key:
            current_run += 1
        else:
            if current_run > longest_run:
                longest_run = current_run
            current_run = 0
    if current_run > longest_run:
        longest_run = current_run
    return longest_run

            


    


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    n = len(mylist)
    if n == 0:
        return Result(0, 0, 0, True)
    if n == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    mid = n // 2
    left = longest_run_recursive(mylist[:mid], key)
    right = longest_run_recursive(mylist[mid:], key)
    left_size = (mid + right.left_size) if left.is_entire_range else left.left_size
    right_size = ((n - mid) + left.right_size) if right.is_entire_range else right.right_size
    longest_size = max(left.longest_size, right.longest_size, left.right_size + right.left_size)
    is_entire_range = left.is_entire_range and right.is_entire_range

    return Result(left_size, right_size, longest_size, is_entire_range)