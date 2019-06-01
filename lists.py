first_list = ["a", "b", "c", "d"]

print("The list is "+ str(first_list))

first_list[2] = "amended"

print("The amended list is "+ str(first_list))

first_list.remove("b")

print("The deleted list is "+ str(first_list))

first_list.pop()

print("The popped list is "+ str(first_list))

print("The items of the final list are: ")

for item in first_list:
    print(item)
