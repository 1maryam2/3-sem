
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.new_set = set()
        self.ignore_case = kwargs.get('ignore_case', False)


    def __next__(self):
        while True:
            try:
                item = next(self.items)
                lookup_item = item.lower() if self.ignore_case and isinstance(item, str) else item

                if lookup_item not in self.new_set:
                    self.new_set.add(lookup_item)
                    return item
            except StopIteration:
                raise StopIteration

    def __iter__(self):
        return self


data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
u = Unique(data)
print(list(u))