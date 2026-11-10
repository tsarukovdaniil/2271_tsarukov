lst = ['hello', 'hell', 'bye', 'world', 'babye']
lst.sort(key=lambda w: (len(w), w))
print(lst)  # ['bye', 'hell', 'babye', 'hello', 'world']
