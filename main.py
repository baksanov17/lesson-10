my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_numbers = []
i = 0
while i < len(my_list):
    if my_list[i] > 0:
        positive_numbers = positive_numbers + [my_list[i]]
        i = i + 1
    elif my_list[i] == 0:
        i = i + 1
        continue
    else:
        break
print(','.join(map(str,positive_numbers)))



