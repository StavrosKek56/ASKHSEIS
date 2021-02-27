testcases = [
    {},  # 0
    {"x": 5},  # 1
    {"x": 5, "y": [1, 2, 3]},  # 2
    {"x": 5, "y": {"a": 2, "b": 67}},  # 2
    {"x": 5, "y": [[1, 2], [3, 4]]}  # 3
]


def dict_depth(coll):
    if isinstance(coll, dict):
        if coll == {}:
            return 0
        else:
            return 1 + (max(map(dict_depth, coll.values())))

    elif isinstance(coll, list):
        if coll == []:
            return 0
        else:
            return 1 + (max(map(dict_depth, coll)))
    return 0


# testing
count = 0
depths = []
for t in testcases:
    #d = dict_depth(t)
    depths.insert(count,dict_depth(t))
    count += 1


depths.sort(reverse=True)
print(depths)
print(depths[0])
