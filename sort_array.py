def sort_array(source_array):
	'''
	Function that takes in a list, and only sorts the odd numbers from smallest to largest
	Even numbers maintain their position in the list
	'''
    if len(source_array) == 0:
        return source_array
    a = source_array
    b = sorted([x for x in source_array if x % 2 != 0], reverse = True)
    for i in range(len(a)):
        if a[i] % 2 != 0:
            a[i] = b.pop()
    return a