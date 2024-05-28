def find_symmetric_pairs(pairs):
    symmetric_pairs = []
    for (x, y) in pairs:
        for (a, b) in pairs:
            if (x, y) != (a, b) and x == b and y == a:
                symmetric_pairs.append((x, y))
                break
    return symmetric_pairs

pairs = [(11, 20), (30, 40), (5, 10), (40, 30), (10, 5)]
print("Following pairs have symmetric pairs")
for pair in find_symmetric_pairs(pairs):
    print(pair)
