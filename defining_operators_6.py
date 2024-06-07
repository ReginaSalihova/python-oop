class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, index, value):
        self.data[index] = value

    def __getitem__(self, index):
        return self.data.get(index, 0)


def print_elem(array, ind):
    print('arr[{}] = {}'.format(ind, array[ind]))


arr = SparseArray()
index = 1000000000
arr[index] = 123

print_elem(arr, index - 1)
print_elem(arr, index)
print_elem(arr, index + 1)
