numbers = [1996, 30, 60, 56, 87, 6, 86, 34]
def find_min():
    m = numbers[0]
    for i in numbers:
        if m > i:
            m = i
    return m
print('List number:',numbers)
m = find_min()
print('Min number of the list is:',m)