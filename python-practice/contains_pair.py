def check(l: list):
    seen = set()
    for item in l:
        if item in seen:
            return True
        seen.add(item)
    return False

print(check([1, 2, 3, 2]))
print(check([5, 2, -10, 44, 90]))