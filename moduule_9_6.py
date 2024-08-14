
def all_variants(text):
    size = len(text) + 1
    for a in range(1, size):
        for b in range(size - a):
            yield text[b: b + a]

c = all_variants("adf")
for i in c:
    print(i)