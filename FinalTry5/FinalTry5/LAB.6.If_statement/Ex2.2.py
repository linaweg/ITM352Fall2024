myLists = [
    [1, 2, "a", (1, 2, 3,), True, [-1], False],  # 7 elements: "The list has at least 5 but at most 10 elements"
    [1, 2, "a"],  # 3 elements: "The list has fewer than 5 elements"
    [1, 2, "a", (1, 2, 3,), True, [-1], False, 1, 2, 4, 5, 6, 6],  # 14 elements: "The list has more than 10 elements"
]

mylist = myLists[2]

if len(mylist) < 5:
    print("This list has fewer than 5 elements")
elif 5 <= len(mylist) <= 10:
    print("The list has at least 5 but at most 10 elements")
else:
    print("The list has more than 10 elements")
