def field(goods, *args):
    for item in goods:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            filtered_item = {}
            for arg in args:
                if item.get(arg) is not None:
                    filtered_item[arg] = arg
            if filtered_item:
                yield filtered_item


