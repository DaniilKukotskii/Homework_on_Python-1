length = input("Enter the length: ")
width = input("Enter the width: ")
count_of_slices = input("Enter the count of slices you want to break off: ")

def Result (length, width, count_of_slices):
    return "Yes" if int(length) * int(width) > int(count_of_slices) else "No"

print(f"Result: {Result(length, width, count_of_slices)}")