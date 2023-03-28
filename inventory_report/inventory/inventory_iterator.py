from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data_list):
        self.data_list = data_list
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.data_list):
            current_item = self.get_item(index=self.current_index)
            self.current_index += 1
            return current_item
        else:
            raise StopIteration()

    def get_item(self, index):
        return self.data_list[index]
