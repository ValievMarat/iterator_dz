# task 1
class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.current_index = 0
        self.current_nested_index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if len(self.nested_list[self.current_index]) < (self.current_nested_index+1):
            self.current_index += 1
            self.current_nested_index = 0
        if len(self.nested_list) < (self.current_index+1):
            raise StopIteration
        self.current_nested_index += 1
        return self.nested_list[self.current_index][self.current_nested_index - 1]


# task2
def flat_generator(nested_list):
    for ext_item in nested_list:
        for item in ext_item:
            yield item


# task3
class FlatAllIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.current_index = 0
        self.parent = None
        self.child = None

    def __iter__(self):
        return self

    def __next__(self):

        if self.child is not None:
            return self.child.__next__()
        else:
            if len(self.nested_list) < (self.current_index + 1):
                if self.parent is None:
                    raise StopIteration
                else:
                    self.parent.child = None
                    self.parent.current_index += 1
                    return self.parent.__next__()

            if type(self.nested_list[self.current_index]) == list:
                internal_flat = FlatAllIterator(self.nested_list[self.current_index])
                internal_flat.parent = self
                self.child = internal_flat
                return internal_flat.__next__()
            else:
                self.current_index += 1
                return self.nested_list[self.current_index-1]

# task4
def flat_all_generator(nested_list):
    for item in nested_list:
        if type(item) == list:
            yield from flat_all_generator(item)
        else:
            yield item


if __name__ == '__main__':

    # task1
    print('task 1:')
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    # task2
    print()
    print('task 2:')
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    for item in flat_generator(nested_list):
        print(item)

    # task3
    print()
    print('task 3:')
    nested_list = [
        ['a', 'b', 'c'],
        [['d', 'e'], ['f', ['g', 'h']], ['k']],
        [1, 2, None],
    ]
    for item in FlatAllIterator(nested_list):
        print(item)

    # task4
    print()
    print('task 4:')

    nested_list = [
        ['a', 'b', 'c'],
        [['d', 'e'], ['f', ['g', 'h']], ['k']],
        [1, 2, None],
    ]
    for item in flat_all_generator(nested_list):
        print(item)