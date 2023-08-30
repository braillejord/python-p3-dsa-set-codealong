class MySet:
    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        return dict.clear(self.dictionary)

    # solution branch code
    def __str__(self):
        # list will hold each key in the dictionary
        set_list = []

        for key, value in self.dictionary.items():
            # add "stringified" key to list
            set_list.append(str(key))

        # join the list at the commas and return
        return f'MySet: {{{",".join(set_list)}}}'
