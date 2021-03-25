arr = ["cat", "dog", "earthworm", "whale"]

def my_find(input_array, word):
    for element in input_array:
        if word == element:
            return True
    return False

print(my_find(arr, "cat"))
