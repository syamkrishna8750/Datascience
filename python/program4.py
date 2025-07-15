def tuple_to_dict(t):
    return dict(t)


tuple_data = (("a", 1), ("b", 2), ("c", 3))
converted_dict = tuple_to_dict(tuple_data)
print("Converted dictionary:", converted_dict)